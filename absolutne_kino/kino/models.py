from django.db import models
from PIL import Image

# Model reprezentujący film
class Movie(models.Model):
    # Możliwe typy filmu (do wyboru przy dodawaniu w adminie)
    TYPES = (
        ('current', 'Aktualny'),  # Film aktualnie grany
        ('soon', 'Wkrótce'),      # Film nadchodzący
    )

    title = models.CharField(max_length=200)                     # Tytuł filmu
    description = models.TextField()                             # Opis filmu
    image = models.ImageField(upload_to='movies/')               # Plakat filmu (zdjęcie)
    price = models.DecimalField(max_digits=6, decimal_places=2,  # Cena biletu
                                null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)       # Data premiery
    movie_type = models.CharField(max_length=10, choices=TYPES,  # Typ filmu: aktualny lub wkrótce
                                  default='current')

    def __str__(self):
        return self.title  # Widoczna reprezentacja filmu w panelu admina

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Po zapisaniu filmu — zmniejsz obraz jeśli jest zbyt duży
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)  # Maksymalny rozmiar
                img.thumbnail(output_size, Image.Resampling.LANCZOS)
                img.save(self.image.path, quality=95)  # Nadpisz plik zmniejszoną wersją

# Model reprezentujący konkretny seans filmowy
class Showing(models.Model):
    # Z góry ustalone możliwe godziny rozpoczęcia seansu
    TIME_CHOICES = [
        ('14:00', '14:00'),
        ('16:00', '16:00'),
        ('18:00', '18:00'),
        ('20:00', '20:00'),
    ]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Powiązanie z filmem
    date = models.DateField()                                   # Data seansu (np. 2025-05-22)
    time = models.CharField(max_length=5, choices=TIME_CHOICES) # Godzina seansu do wyboru z listy
    seats_taken = models.TextField(blank=True)                  # Zajęte miejsca (np. "A1,A2,B5")

    def __str__(self):
        # Reprezentacja tekstowa seansu widoczna w panelu admina
        return f"{self.movie.title} - {self.date} {self.time}"

    def save(self, *args, **kwargs):
        # Domyślnie zachowujemy oryginalne działanie save()
        super().save(*args, **kwargs)
