"""
Zadanie zaliczeniowe z języka Python  
Imię i nazwisko ucznia: Tomasz Gradowski
Data wykonania zadania: 19.05.2025
Treść zadania: Sprzedaż biletów w kinie  
Opis funkcjonalności aplikacji: Zawiera logikę widoków odpowiedzialnych za stronę główną, szczegóły filmu, rezerwację miejsc, generowanie PDF z biletem oraz pobieranie zajętych miejsc.
"""


import qrcode
from io import BytesIO
import base64
import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from .models import Movie, Showing

# API: Zwraca listę zajętych miejsc na podstawie ID seansu
def get_taken_seats(request, showing_id):
    showing = get_object_or_404(Showing, pk=showing_id)
    taken_seats = showing.seats_taken.split(',') if showing.seats_taken else []
    return JsonResponse({'taken_seats': taken_seats})

# Widok: Strona "Wkrótce w kinach"
def coming_soon(request):
    upcoming_movies = Movie.objects.filter(movie_type='soon')
    return render(request, 'coming_soon.html', {'movies': upcoming_movies})

# Widok: Strona główna z aktualnie dostępnymi filmami
def home(request):
    movies = Movie.objects.filter(movie_type='current')[:3]
    return render(request, 'home.html', {'movies': movies})

# Widok: Szczegóły filmu i obsługa rezerwacji miejsc
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    showings = Showing.objects.filter(movie=movie).order_by('date', 'time')
    
    # Obsługa formularza POST (rezerwacja miejsc)
    if request.method == 'POST':
        showing_id = request.POST.get('showing')
        selected_seats = request.POST.get('seats', '').split(',')
        selected_seats = [s for s in selected_seats if s]  # Usuwa puste wartości

        showing = get_object_or_404(Showing, pk=showing_id)
        taken_seats = showing.seats_taken.split(',') if showing.seats_taken else []

        # Walidacja: Sprawdzenie czy wybrane miejsca są już zajęte
        if any(seat in taken_seats for seat in selected_seats):
            return render(request, 'movie_detail.html', {
                'error': 'Niektóre miejsca są już zajęte!',
                'movie': movie,
                'showings': showings
            })

        # Aktualizacja listy zajętych miejsc i zapis do bazy
        showing.seats_taken = ','.join(taken_seats + selected_seats)
        showing.save()

        # Generowanie linku do biletu (do użytku w QR)
        ticket_url = request.build_absolute_uri(f'/movie/{movie.id}/')

        # Tworzenie kodu QR z linkiem
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(ticket_url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Konwersja obrazu QR do formatu base64
        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        qr_img_base64 = base64.b64encode(buffer.getvalue()).decode()

        # Kontekst dla szablonu PDF
        context = {
            'movie': movie,
            'showing': showing,
            'seats': selected_seats,
            'total_price': len(selected_seats) * movie.price,
            'qr_img': qr_img_base64,
            'ticket_url': ticket_url,
        }

        # Renderowanie HTML z szablonu PDF
        template = get_template('pdf_template.html')
        html = template.render(context)

        # Ścieżka zapisu PDF na serwerze
        pdf_dir = os.path.join(settings.MEDIA_ROOT, 'tickets')
        os.makedirs(pdf_dir, exist_ok=True)  # Tworzy folder, jeśli nie istnieje
        pdf_path = os.path.join(pdf_dir, f'ticket_{movie.id}.pdf')

        # Zapis PDF do pliku
        with open(pdf_path, 'wb') as f:
            pisa.CreatePDF(html, dest=f)

        # Wysyłka PDF jako odpowiedź do przeglądarki (generujemy jeszcze raz do response)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename=bilet_{movie.id}.pdf'
        pisa.CreatePDF(html, dest=response)
        return response

    # Widok GET — wyświetlenie strony filmu
    return render(request, 'movie_detail.html', {
        'movie': movie,
        'showings': showings
    })


# Przekierowanie użytkownika do wcześniej wygenerowanego PDF z biletem
def ticket_redirect(request, movie_id):
    ticket_url = request.build_absolute_uri(f'/media/tickets/ticket_{movie_id}.pdf')
    return redirect(ticket_url)
