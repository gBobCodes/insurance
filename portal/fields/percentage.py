from django.core.validators import MaxValueValidator
from django.db.models  import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _

class PercentageField(PositiveSmallIntegerField):
	description = _("Integer field with range from 0 to 100.")

	def __init__(self, *args, **kwargs):
		kwargs['validators'] = MaxValueValidator(100)
		super(PercentageField, self).__init__(*args, **kwargs)

