from django import forms
from django.db.models import Model

from portal.models.insured import Insured
from .cache import CacheForm
from .search import SearchForm


class InsuredListForm(
	CacheForm,
	SearchForm,
):
	"""Form to search and filter the list of Insureds."""
	cache_name = 'insured_list'
	default_cache = {'search': ''}

	def filter_insureds(self):
		"""
		Return queryset of Insureds filtered by the form fields.
		If there are less than 100 Insureds, display them all.
		Otherwise, make the user search or filter them.
		"""
		if Insured.objects.count() < 100:
			insureds = Insured.objects.all()
		else:
			insureds = Insured.objects.none()

		if self.is_valid():
			search = self.cleaned_data.get('search')
			self._set_form_cache(values={'search': search})

			if search:
				insureds = insureds.filter(name__icontains=search)
		return insureds


class InsuredModelForm(forms.ModelForm):
	"""Form to create or update an Insured."""
	class Meta:
		model = Insured
		fields = [
			'name', 
			'title',
			'title_other',
			'email',
			'mobile_phone',
			'office_phone',
			'dob',
			'note', 
		]

	def __init__(self, *args, **kwargs):
		"""Customer wants note text box to be shorter."""
		super(InsuredModelForm, self).__init__(*args, **kwargs)
		self.fields['note'].widget=forms.Textarea(
			attrs={
				'class': 'care-note',
			}
		)
		self.fields['name'].widget.attrs.update({'autofocus': ''})

