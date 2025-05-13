from django.db import models
from PIL import Image
import os

class Movie(models.Model):
    TYPES = (
        ('current', 'Aktualny'),
        ('soon', 'Wkrótce'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    movie_type = models.CharField(max_length=10, choices=TYPES, default='current')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size, Image.Resampling.LANCZOS)
                img.save(self.image.path, quality=95)

class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    seats_taken = models.TextField(blank=True)

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)