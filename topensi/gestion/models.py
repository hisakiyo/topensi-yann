from django.db import models
from month.models import MonthField

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50, unique=True)

class Partenaire(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    
class Type(models.Model):
    nom = models.CharField(max_length=50, unique=True)

class Etat(models.Model):
    nom = models.CharField(max_length=50, unique=True)

class Info(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    partenaire = models.ForeignKey(Partenaire, on_delete=models.CASCADE)
    typ = models.ForeignKey(Type, on_delete=models.CASCADE)
    marge = models.FloatField(null=True)
    recurrent = models.FloatField(null=True)
    etat = models.ForeignKey(Etat, on_delete=models.CASCADE)
    facture = models.BooleanField()
    dateCreation = MonthField()
    dateCloture = MonthField()
    dateInstallation = models.DateField(null=True)
    
    def __unicode__(self):
        return unicode(self.month)