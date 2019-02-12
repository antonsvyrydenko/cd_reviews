# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	date = models.DateTimeField()
	img = models.ImageField(null=True, blank=True, upload_to="news/")

	def __str__(self):
		return self.title

	def __unicode__(self):
		return smart_unicode(self.title)
