from __future__ import unicode_literals

from django.db import models


class Title(models.Model):
	"""Doctors have titles such as MD DO etc."""
	name = models.CharField(max_length=10, blank=False, unique=True)

	class Meta:
		ordering = ('name',)

	def __unicode__(self):
		return u'{}'.format(self.name)