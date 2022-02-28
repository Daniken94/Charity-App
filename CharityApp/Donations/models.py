from django.db import models
from django.forms import NullBooleanField
from django.conf import settings



class Category(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"





class Institution(models.Model):
    type_choices = (
        ("fundacja", 'fundacja'),
        ("organizacja pozarządowa", "organizacja pozarządowa"),
        ("zbiórka lokalna", "zbiórka lokalna"),
    )

    name = models.CharField(max_length=120)
    description = models.TextField(default="", blank=True)
    type = models.CharField(max_length=24, choices=type_choices, default="fundacja")
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return f"{self.name}"




class Donations(models.Model):
    quantity = models.IntegerField(verbose_name="Podal liczbe worków 60l z podarunkami.")
    city = models.CharField(max_length=120, verbose_name="Podaj miasto.")
    street = models.CharField(max_length=120, verbose_name="Podaj nazwę ulicy.")
    home_number = models.IntegerField(verbose_name="Podaj numer domu/mieszkania.")
    phone_number = models.IntegerField()
    zip_code = models.CharField(max_length=5, default="42680", verbose_name="Podaj kod pocztowy.")
    pick_up_date = models.DateField(auto_now_add=False, verbose_name="Paczka będzie gotowa do odbioru dnia: ")
    pick_up_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Paczka będzie gotowa do odbioru o godzinie: ")
    pick_up_comment = models.TextField(max_length=240, verbose_name="Komentarz dla kuriera")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True) 
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    categories = models.ManyToManyField("Category")
  
    class Meta:
        verbose_name_plural = "Donations"


    def __str__(self):
        return f"{self.user} przekazał {self.quantity} worków dla {self.institution}"