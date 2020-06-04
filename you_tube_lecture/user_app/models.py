# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Paradigm(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length = 200)
    paradigm = models.ForeignKey(Paradigm , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length = 50)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
