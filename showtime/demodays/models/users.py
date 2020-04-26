from django.db import models


class Student(models.Model):
    PROG_BASICS = 'PRB'
    SECOND_MODULE = 'SEC'
    THIRD_MODULE = 'TRD'
    ADVANCE_MODULE = 'ADV'
    JOB_HUNT = 'JBH'
    ALUMNI = 'ALU'
    MODULE_IN_SCHOOL_CHOICES = [
        (PROG_BASICS, 'ProgBasics'),
        (SECOND_MODULE, 'Second Module'),
        (THIRD_MODULE, 'Third Module'),
        (ADVANCE_MODULE, 'Advance Module'),
        (JOB_HUNT, 'Job Hunt'),
        (ALUMNI, 'Alumni'),
    ]
    module_in_school = models.CharField(
        max_length=3,
        choices=MODULE_IN_SCHOOL_CHOICES,
        default=ADVANCE_MODULE
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    nick = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    took_demos = models.PositiveSmallIntegerField(default=0, editable=False)

    def __str__(self):
        if self.nick:
            return f"{self.name} {self.surname} \"{self.nick}\""
        return f"{self.name} {self.surname}"

    def full_name(self):
        return self.__str__()

    def is_obliged_to_present(self):
        return self.module_in_school in {self.ADVANCE_MODULE, self.JOB_HUNT}


class ProjectTeam(models.Model):
    name = models.CharField(max_length=30)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
