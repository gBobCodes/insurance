from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
	"""Abstract class holding the attributes of a human person."""
	name = models.CharField(max_length=50, blank=False)
	office_phone = models.CharField(max_length=25, blank=True)
	mobile_phone = models.CharField(max_length=25, blank=True)
	email = models.EmailField(blank=True)
	dob = models.DateField(blank=True, null=True)
	note = models.TextField(blank=True)

	class Meta:
		abstract = True
