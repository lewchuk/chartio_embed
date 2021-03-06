# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _

# Subclass AbstractUser
class Chart(models.Model):

    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title
