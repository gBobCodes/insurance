from __future__ import unicode_literals

from django.db import models

from .state import State


class Address(models.Model):
	"""Mailing address"""
	street = models.CharField(max_length=50, blank=False)
	building = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=50, blank=False)
	county = models.CharField(max_length=50, blank=True)
	state = models.ForeignKey('State')
	zip_code = models.CharField(max_length=15, blank=False)

	def __unicode__(self):
		return u'{}'.format(self.street)