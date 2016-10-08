from __future__ import unicode_literals

from django.db import models

from portal.fields.percentage import PercentageField


class Specialty(models.Model):
	"""Doctors practice in specific areas of medicine known as Specialties."""
	name = models.CharField(max_length=80, blank=False, unique=True)
	practice_percentage = PercentageField(default=0)

	class Meta:
		ordering = ('name',)

	def __unicode__(self):
		return u'{}'.format(self.name)