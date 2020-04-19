from django.db import models

from .users import ProjectTeam
from .companies import Company
from .techs import Tech


class Demoday(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT,
                                blank=True, null=True)
    planned_date = models.DateField()

    def __str__(self):
        if not self.company:
            return f"{self.planned_date}, guest not declared"
        return f"{self.planned_date}, {self.company}"


    # def is_future_demoday(self):
    #     return self.planned_date > timezone.now()


class Demo(models.Model):
    demoday = models.ForeignKey(Demoday, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=100)
    team = models.ForeignKey(ProjectTeam, on_delete=models.PROTECT)
    used_techs = models.ManyToManyField(Tech, blank=True)
    presentation = models.FileField(upload_to='demodays/presentation_files',
                                    blank=True)

    def __str__(self):
        return f"Team {self.team}, {self.demoday}"
