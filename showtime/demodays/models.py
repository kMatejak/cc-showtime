from django.db import models


class DemoDay(models.Model):
    test_text = models.CharField(max_length=200)
    date = models.DateTimeField('date planned')


class Demo(models.Model):
    demoday = models.ForeignKey(DemoDay, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    team_name = models.CharField(max_length=66)
    student_names = models.CharField(max_length=300)

