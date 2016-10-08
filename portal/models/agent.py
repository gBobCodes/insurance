from __future__ import unicode_literals
import reversion

from django.db import models

from .agency import Agency
from .person import Person

@reversion.register()
class Agent(Person):
	"""Insurance sales agent who works for an Agency."""
	agency = models.ForeignKey('Agency')

	class Meta:
		ordering = ('name',)

		
	def __unicode__(self):
		return u'{}'.format(self.name)