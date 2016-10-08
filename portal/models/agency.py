from __future__ import unicode_literals
import reversion

from django.db import models

from .address import Address

@reversion.register()
class Agency(Address):
	"""Insurance Agency which employs Agents."""
	name = models.CharField(max_length=50, blank=False, unique=True)
	office_phone = models.CharField(max_length=25, blank=True)
	note = models.TextField(blank=True)

	class Meta:
		ordering = ('name',)

	def __unicode__(self):
		return u'{}'.format(self.name)
