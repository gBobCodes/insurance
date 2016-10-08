from __future__ import unicode_literals

from django.db import models


class County(models.Model):
	"""A State has many counties. Each county is in a territory."""
	name = models.CharField(max_length=30)
	territory = models.CharField(max_length=5, blank=False, default='A')

	class Meta:
		ordering = ('name',)

	def __unicode__(self):
		return u'{}'.format(self.name)

