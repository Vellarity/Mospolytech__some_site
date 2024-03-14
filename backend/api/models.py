import datetime
from email.policy import default
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from simple_history.models import HistoricalRecords
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User as AuthUser

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

@receiver(post_save, sender=AuthUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=AuthUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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
    info_text = models.TextField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

class WearType(models.Model):
    name = models.TextField(null=False)

    def __str__(self):
        return f"{self.name}"


class WearComment(models.Model):
    wear = models.ForeignKey("Wear", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    author = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True)
    date = models.DateField(default=datetime.date.today())
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0, null=False)

class WearSize(models.Model):
    name = models.TextField(null=False)

    def __str__(self):
        return f"{self.name}"