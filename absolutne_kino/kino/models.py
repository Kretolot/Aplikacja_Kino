from django.db import models
from PIL import Image
import os

# Model reprezentujący film
class Movie(models.Model):
    # Typ filmu: aktualny repertuar lub "wkrótce"
    TYPES = (
        ('current', 'Aktualny'),
        ('soon', 'Wkrótce'),
    )

    title = models.CharField(max_length=200)  # Tytuł filmu
    description = models.TextField()          # Opis filmu
    image = models.ImageField(upload_to='movies/')  # Plakat filmu
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Cena biletu (opcjonalna)
    release_date = models.DateField(null=True, blank=True)  # Data premiery (opcjonalna)
    movie_type = models.CharField(max_length=10, choices=TYPES, default='current')  # Typ filmu: aktualny lub nadchodzący

    def __str__(self):
        return self.title  # Reprezentacja tekstowa w panelu admina

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Zmniejszenie rozmiaru obrazu jeśli jest za duży
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size, Image.Resampling.LANCZOS)  # Zmniejszenie z zachowaniem proporcji
                img.save(self.image.path, quality=95)  # Nadpisanie oryginału

# Model reprezentujący konkretny seans filmowy
class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Powiązanie z filmem (gdy film usunięty, seans też)
    date = models.DateField()          # Data seansu
    time = models.TimeField()          # Godzina seansu
    seats_taken = models.TextField(blank=True)  # Zajęte miejsca zapisane jako tekst (np. "A1,A2,B5")

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time}"  # Reprezentacja tekstowa w adminie

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Standardowe zapisanie modelu
