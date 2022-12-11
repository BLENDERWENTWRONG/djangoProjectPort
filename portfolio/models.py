from django.db import models
from django import forms
from django.conf import settings
# Create your models here.
class Accomplishments(models.Model):
    title = models.CharField(max_length=70, null=True, blank=True, default="")
    OPTIONS = (
        ("SCH", "Scholarships"),
        ("HR", "Honor Roll"),
        ("AW", "Awards Won"),
        ("SR", "Student Related"),
        ("PA", "Perfect Attendance Awards")
    )
    # type = models.Choices(null=False, choices=OPTIONS)
    uploads = models.ImageField(upload_to='images')
    class Meta:
        db_table = "ProfessionalAccomplishments"


class Awards(models.Model):
    title = models.CharField(max_length=70, null=True, blank=True, default="")
    date = models.DateTimeField(auto_now=True)
    uploads = models.ImageField(upload_to='images/awards')

    class Meta:
        db_table = "Awards"

class DLC(models.Model):
    title = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=100, null=False)
    startDate = models.DateTimeField(auto_now=True, null=False)
    endDate = models.DateTimeField(auto_now=True, null=False)
    uploads = models.ImageField(upload_to='images', null=False)

    class Meta:
        db_table = "DLC"

class VCS(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    startDate = models.DateTimeField(auto_now=True, null=False)
    endDate = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = "VCS"

class portfolio(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,default=None,on_delete=models.CASCADE)
    bio = models.CharField (max_length=4000, null=False)
    workField = models.CharField (max_length=4000, null=False , blank=True)
    careersum = models.CharField (max_length=4000, null=False,blank=True)
