from django.db import models


class Tech(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
