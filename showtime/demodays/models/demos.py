from django.db import models
from django.utils import timezone

from .users import ProjectTeam
from .companies import Company
from .techs import Tech


class Demoday(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT,
                                blank=True, null=True)
    planned_date = models.DateField()
    did_take_place = models.BooleanField(default=False)
    just_field = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.planned_date}"


class Demo(models.Model):
    demoday = models.ForeignKey(Demoday, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=100)
    team = models.ForeignKey(ProjectTeam, on_delete=models.PROTECT)
    used_techs = models.ManyToManyField(Tech, blank=True)
    about = models.TextField(blank=True)
    presentation = models.FileField(upload_to='demodays/presentation_files',
                                    blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Team {self.team}, {self.demoday}"
