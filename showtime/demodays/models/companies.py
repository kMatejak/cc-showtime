from django.db import models

from .techs import Tech


class Representative(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Company(models.Model):
    name = models.CharField(max_length=40)
    representatives = models.ManyToManyField(Representative, blank=True)
    sought_techs = models.ManyToManyField(Tech, blank=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
