from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Lecturer(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=13)
    lecturer_code = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.lecturer_code


class LecturerAvailability(models.Model):
    lecturer = models.ForeignKey(Lecturer, )
    day = models.CharField(max_length=15, null=True)
    from_hr = models.CharField(max_length=10, null=True)
    to_hr = models.CharField(max_length=10, null=True)

    def __unicode__(self):
        return str(self.lecturer)

