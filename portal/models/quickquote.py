from __future__ import unicode_literals
import reversion

from django.contrib.auth.models import User
from django.db import models

from portal.fields.percentage import PercentageField
from .address import Address
from .deductible import Deductible
from .limit import Limit
from .procedure import Procedure
from .specialty import Specialty
from .state import State, StateCoverage

@reversion.register()
class QuickQuote(models.Model):
	'''
	A model for Quick Quotes created by the public
	or by authenticated users.
	'''

	STATUS_NOT_REQUESTED = 0
	STATUS_AGENT_REQUEST = 10
	STATUS_UNDERWRITING = 20
	STATUS_INTERNAL_REVIEW = 30
	STATUS_SENT_TO_AGENT = 40
	STATUS_REJECTED = 50
	STATUS_ACCEPTED = 60
	STATUS_CHOICES = (
		(STATUS_NOT_REQUESTED, ''),
		(STATUS_AGENT_REQUEST, ''),
		(STATUS_UNDERWRITING, ''),
		(STATUS_INTERNAL_REVIEW, ''),
		(STATUS_SENT_TO_AGENT, ''),
		(STATUS_REJECTED, ''),
		(STATUS_ACCEPTED, ''),
	)

	SURGERY_NONE = 0
	SURGERY_MINOR = 50
	SURGERY_MAJOR = 100
	SURGERY_CHOICES = (
		(SURGERY_NONE, 'None'),
		(SURGERY_MINOR, 'Minor'),
		(SURGERY_MAJOR, 'Major'),
	)

	status = models.PositiveSmallIntegerField(
		choices=STATUS_CHOICES,
		default=STATUS_NOT_REQUESTED,
	)
	surgery = models.PositiveSmallIntegerField(
		choices=SURGERY_CHOICES,
		default=SURGERY_NONE,
	)
	created = models.DateTimeField(auto_now_add=True)
	edited = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User)
	editor = models.ForeignKey(User)
	friendly_name = models.CharField(max_length=50, blank=True)

	state = models.ForeignKey('State')
	primary_state = models.ForeignKey('StateCoverage')
	secondary_state = models.ForeignKey('StateCoverage', blank=True, null=True)

	primary_specialty = models.ForeignKey('Specialty')
	secondary_specialty = models.ForeignKey('Specialty', blank=True, null=True)

	laser_procedure = models.ForeignKey('Procedure')
	bariatric_procedure = models.ForeignKey('Procedure')
	telemedicine_procedure = models.ForeignKey('Procedure')
	correctional_facilities = models.ForeignKey('Procedure')
	nursing_homes = models.ForeignKey('Procedure')

	# An authenticated user will select these values.
	agency = models.ForeignKey('Agency', blank=True, null=True)
	agent = models.ForeignKey('Agent', blank=True, null=True)
	insured = models.ForeignKey('Insured', blank=True, null=True)

	# An external user will enter these values.
	agency_name = models.CharField(max_length=50, blank=False)
	agent_name = models.CharField(max_length=30, blank=False)
	agent_email = models.EmailField(blank=False)
	insured_name = models.CharField(max_length=30, blank=False)

	primary_practice = models.ManyToManyField(
		'Address',
		related_name='primary_address',
	)
	secondary_practice = models.ManyToManyField(
		'Address',
		related_name='secondary_address',
	)

	prior_acts_effective_date = models.DateField(blank=True, null=True)
	prior_acts_retroactive_date = models.DateField(blank=True, null=True)
	board_actions_last_10_years = models.PositiveSmallIntegerField(default=0)
	weekly_hours = models.PositiveSmallIntegerField(default=0)
	weekly_patients = models.PositiveSmallIntegerField(default=0)
	weekly_procedures = models.PositiveSmallIntegerField(default=0)
	weekly_deliveries = models.PositiveSmallIntegerField(default=0)
	weekly_reads = models.PositiveSmallIntegerField(default=0)
	entity_coverage = models.BooleanField(default=False)
	entity_note = models.TextField(blank=True)
	professional_coverage = models.BooleanField(default=False)
	professional_note = models.TextField(blank=True)
	cosmetic_surgery = models.ForeignKey('Procedure')
	cosmetic_elective_percentage = PercentageField(default=0)
	cosmetic_recon_percentage = PercentageField(default=0)
	claims_last_10_years = models.PositiveSmallIntegerField(default=0)
	open_claims = models.PositiveSmallIntegerField(default=0)
	closed_claims = models.PositiveSmallIntegerField(default=0)
	current_carrier = models.CharField(max_length=50, blank=True)
	expiring_premium = models.CharField(max_length=10, blank=True)
	note = models.TextField(blank=True)


