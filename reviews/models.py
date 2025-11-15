from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name="reviews",
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Avaliação nao pode ser inferior a zero estrelas."),
            MaxValueValidator(5, "Avaliação nao pode ser superior a cinco estrelas."),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.movie.title
