from __future__ import unicode_literals
import reversion

from django.db import models

from portal.fields.percentage import PercentageField
from portal.querysets.state import StateQuerySet
from .county import County
from .limit import Limit

@reversion.register()
class State(models.Model):
	'''A State in the U.S.A.'''

	objects = StateQuerySet.as_manager()

	active = models.BooleanField(default=False)
	name = models.CharField(max_length=30, blank=False, unique=True)
	abbr = models.CharField(max_length=2, blank=False, unique=True)
	limits = models.ManyToManyField('Limit')
	counties = models.ManyToManyField('County', editable=False)

	class Meta:
		ordering = ('name',)

	def __unicode__(self):
		return u'{}'.format(self.name)


class StateCoverage(models.Model):
	'''
	Doctors can practice in multiple states.
	Save the percentage of work in each.
	'''
	state = models.ForeignKey('State')
	practice_percentage = PercentageField(default=0)

