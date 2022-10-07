from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Things(models.Model):
    name = models.CharField(
        unique=True,
        blank=False,
        max_length=30
    )
    description = models.CharField(
        unique=False,
        blank=True,
        max_length=120
    )
    quantity = models.IntegerField(
        unique=False,
        blank=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
