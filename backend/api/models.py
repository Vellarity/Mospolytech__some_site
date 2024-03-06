from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from simple_history.models import HistoricalRecords

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    
    fio = models.CharField(max_length=240, blank=True)
    number = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    geo = models.TextField(blank=True)
    history = HistoricalRecords()


class Wear(models.Model):

    WEARSIZES = (
        ("XXS","XXS"),
        ("XS","XS"),
        ("S","S"),
        ("M","M"),
        ("L","L"),
        ("XL", "XL")
    )

    COLORS = {
        "BLACK": "Чёрный",
        "WHITE": "Белый",
        "BLUE": "Синий",
        "RED": "Красный",
        "GREEN": "Зелёный",
        "PURPLE": "Фиолетовый"
    }

    name = models.TextField(max_length=32, null=False)
    cost = models.IntegerField(default=0)
    type = models.ForeignKey("WearType", on_delete=models.CASCADE)
    size = models.ManyToManyField("WearSize") # TextField(choises=WEARSIZES, default = "XXS")
    image = models.ImageField(upload_to="wear_images", null=True)
    color = models.TextField(choices=COLORS, default="BLACK")
    history = HistoricalRecords()

class WearType(models.Model):
    name = models.TextField(null=False)

    def __str__(self):
        return f"{self.name}"


class WearComment(models.Model):
    wear_id = models.ForeignKey("Wear", on_delete=models.CASCADE)
    user_id = models.ForeignKey("Profile", on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0, null=False)

class WearSize(models.Model):
    name = models.TextField(null=False)

    def __str__(self):
        return f"{self.name}"