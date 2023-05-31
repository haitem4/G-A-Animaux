from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.headerregistry import Address
from msilib.schema import Class
from operator import mod
from pyexpat import model
from statistics import mode
from tabnanny import check
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Animal(models.Model):
    IdA = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=25)
    Categorie_Choice = [
        ('CHAT', 'Chat'), ('CHIEN', 'Chien'), ('Oiseau', 'Oiseau')]
    Categorie = models.CharField(
        max_length=50, choices=Categorie_Choice, blank=True)
    Age = models.IntegerField()
    BOOL_Choice = [
        ('OUI', 'OUI'), ('NON', 'NON')]
    StatutVaccinal = models.CharField(
        max_length=50, choices=BOOL_Choice, blank=True)

    Adopte = models.BooleanField()
    Sterilization = models.CharField(
        max_length=50, choices=BOOL_Choice, blank=True)

    Photo = models.ImageField(upload_to='static/images/animals/')

    def __str__(self):
        return self.Nom


class Adopteur(models.Model):
    Nom = models.CharField(max_length=25)
    Prenom = models.CharField(max_length=25)
    Cin = models.CharField(max_length=8)
    SalaireMensuelle = models.FloatField()
    Logement = models.CharField(max_length=25)
    Jardin = models.BooleanField()
    SituationFamiliale = models.CharField(max_length=50)
    Address = models.TextField()
    phoneNumber = models.CharField(max_length=12)
    IdA = models.IntegerField()

    def __str__(self):
        return self.Nom
