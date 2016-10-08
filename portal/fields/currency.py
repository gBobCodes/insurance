from django.db.models  import DecimalField
from django.utils.translation import ugettext_lazy as _

class CurrencyField(DecimalField):
	description = _("Decimal field to hold dollar values.")

	def __init__(self, *args, **kwargs):
		kwargs['max_digits'] = 8
		kwargs['decimal_places'] = 2
		kwargs['default'] = 0
		super(CurrencyField, self).__init__(*args, **kwargs)

