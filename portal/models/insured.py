from __future__ import unicode_literals
import reversion

from django.db import models

from .person import Person
from .title import Title

@reversion.register()
class Insured(Person):
	"""Doctor or medical professional needing malpractice insurance."""
	title = models.ForeignKey('Title')
	title_other = models.CharField(max_length=10, blank=True)

	class Meta:
		ordering = ('name',)

	def __unicode__(self):
		return u'{}'.format(self.name)