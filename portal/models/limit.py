from __future__ import unicode_literals

from django.db import models


class Limit(models.Model):
	"""Liability Limit"""
	min = models.PositiveIntegerField()
	max = models.PositiveIntegerField()

	class Meta:
		ordering = ('min', 'max',)

	def __unicode__(self):
		return u'{:,d} / {:,d}'.format(self.min, self.max)
