from django.db import models

from .techs import Tech


class Company(models.Model):
    name = models.CharField(max_length=40)
    website = models.CharField(max_length=60, blank=True, null=True)
    sought_techs = models.ManyToManyField(Tech, blank=True)
    open_positions = models.PositiveSmallIntegerField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'companies'


class Representative(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
