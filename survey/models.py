# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=100,unique=True)
    favorite_color = models.CharField(max_length=7)
    ANIMAL_CHOICES = (
        ('cats', 'Cats'),
        ('dogs', 'Dogs'),
    )
    animal = models.CharField(max_length=4, choices=ANIMAL_CHOICES)
