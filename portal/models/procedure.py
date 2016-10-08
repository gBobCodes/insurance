from __future__ import unicode_literals

from django.db import models

from portal.fields.percentage import PercentageField


class Procedure(models.Model):
	"""Doctors perform procedures on people."""
	performs = models.BooleanField(default=False)
	work_percentage = PercentageField(default=0)
	note = models.TextField(blank=True)

