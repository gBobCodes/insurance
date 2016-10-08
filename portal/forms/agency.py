from django import forms
from django.db.models import Model

from portal.models.agency import Agency
from .cache import CacheForm
from .search import SearchForm
from .state import StateFilterForm


class AgencyFilterForm(forms.Form):
	"""Form to filter a list of objects by Agency."""
	agency = forms.ModelChoiceField(
		required=False,
		queryset=Agency.objects.all(),
		empty_label='All Agencies',
		widget=forms.Select(
			attrs={
				'onchange': 'this.form.submit()',
			}
		)
	)


class AgencyListForm(
	CacheForm,
	SearchForm,
	StateFilterForm,
):
	"""Form to search and filter the list of Agencies."""
	cache_name = 'agency_list'
	default_cache = {'search': '', 'state': ''}

	def filter_agencies(self):
		"""
		Return queryset of Agencies filtered by the form fields.
		If there are less than 100 agencies, display them all.
		Otherwise, make the user search or filter them.
		"""
		if Agency.objects.count() < 100:
			agencies = Agency.objects.all()
		else:
			agencies = Agency.objects.none()

		if self.is_valid():
			search = self.cleaned_data.get('search')
			state = self.cleaned_data.get('state')
			self._set_form_cache(
				values={
					'search': search,
					'state': state,
				}
			)

			# Apply the search and filters applied by the user.
			if search:
				agencies = agencies.filter(name__icontains=search)
			if state:
				agencies = agencies.filter(state=state)
		else:
			print vars(self)

		return agencies


class AgencyModelForm(forms.ModelForm):
	"""Form to create or update an Agency."""
	class Meta:
		model = Agency
		fields = [
			'name', 
			'office_phone',
			'street',
			'building',
			'city',
			'state',
			'zip_code', 
			'note', 
		]

	def __init__(self, *args, **kwargs):
		"""Customer wants note text box to be shorter."""
		super(AgencyModelForm, self).__init__(*args, **kwargs)
		self.fields['note'].widget=forms.Textarea(
			attrs={
				'class': 'care-note',
			}
		)
		self.fields['name'].widget.attrs.update({'autofocus': ''})

