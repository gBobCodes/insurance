from __future__ import unicode_literals

from django.db import models

from portal.fields.currency import CurrencyField

from .limit import Limit


class Deductible(models.Model):
	'''Policy deductible options.'''
	value = models.PositiveIntegerField(unique=True)

	class Meta:
		ordering = ('value',)

	def __unicode__(self):
		return u'{:,d}'.format(self.value)


class DeductibleLimit(models.Model):
	'''The relationship between Deductible and Limit.'''
	class Meta:
		abstract = True

	deductible = models.ForeignKey('Deductible')
	limit = models.ForeignKey('Limit')


class DedLimitMultiplier(DeductibleLimit):
	'''The relationship between Deductible and Limit.
	
	Has a field 'multiplier' that changes the premium
	based on the selected deductible and limit.
	The minimum multiplier value is 1.0
	Maximum value is 9.99999
	'''
	multiplier = models.DecimalField(
		max_digits=6,
		decimal_places=5,
		default=1.0
	)

class DedLimitPremium(DeductibleLimit):
	'''The relationship between Deductible and Limit.
	
	Has a field 'premium' that is a calculated premium
	based on the selected deductible and limit.
	'''
	premium = CurrencyField(blank=True)

