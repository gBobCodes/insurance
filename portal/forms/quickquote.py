from collections import OrderedDict

from django import forms
from django.db.models import Model

from portal.models.county import County
from portal.models.deductible import Deductible, DedLimitPremium
from portal.models.limit import Limit
from portal.models.quickquote import QuickQuote
from portal.models.state import State
from portal.models.title import Title



class QuickQuotePublicForm(forms.Form):
	'''Form for the public to create a QuickQuote.'''

	clicked_button = forms.CharField(
		required=False,
		initial='',
		widget = forms.HiddenInput(),
	)
	state = forms.ModelChoiceField(
		queryset=State.objects.active(),
		required=True,
		widget = forms.HiddenInput(),
	)
	deductible = forms.ModelChoiceField(
		queryset=Deductible.objects.all(),
		empty_label = None,
		required=False,
	)

	agency_name = forms.CharField(required=True)
	agent_name = forms.CharField(required=True)
	agent_email = forms.EmailField(required=True)
	insured_name = forms.CharField(required=True)
	primary_practice_street = forms.CharField(required=True)
	primary_practice_building = forms.CharField(required=False)
	primary_practice_city = forms.CharField(required=True)
	primary_practice_zip_code = forms.CharField(required=True)
	title = forms.ModelChoiceField(queryset=Title.objects.all(), required=True)
	title_other = forms.CharField(
		required=False,
		widget=forms.TextInput(
			attrs={
				'class': 'care-other-title',
				'placeholder': 'if other',
			}
		)
	)
	dob = forms.DateField(required=True)

	surgery = forms.ChoiceField(
		required=True,
		choices=QuickQuote.SURGERY_CHOICES,
		initial=QuickQuote.SURGERY_NONE,
	)

	primary_state_percentage = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=100,
		initial=100,
	)
	secondary_state_coverage = forms.ModelChoiceField(
		required=False,
		queryset=State.objects.active(),
	)
	secondary_state_percentage = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=100,
		initial=0,
	)

	primary_specialty_name = forms.CharField(required=True)
	primary_specialty_percentage = forms.IntegerField(
		required=True,
		min_value=1,
		max_value=100,
		initial=100,
	)

	secondary_specialty_name = forms.CharField(required=False)
	secondary_specialty_percentage = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=100,
		initial=0,
	)

	weekly_hours = forms.IntegerField(
		required=False,
		min_value=0,
		max_value=100,
		initial=0,
	)
	weekly_patients = forms.IntegerField(
		required=False,
		min_value=0,
		max_value=100,
		initial=0,
	)
	weekly_procedures = forms.IntegerField(
		required=False,
		min_value=0,
		max_value=100,
		initial=0,
	)
	weekly_deliveries = forms.IntegerField(
		required=False,
		min_value=0,
		max_value=100,
		initial=0,
	)
	weekly_reads = forms.IntegerField(
		required=False,
		min_value=0,
		max_value=100,
		initial=0,
	)

	bariatric_performs = forms.BooleanField(initial=False, required=False)

	correctional_performs = forms.BooleanField(initial=False, required=False)
	correctional_note = forms.CharField(
		required=False,
		widget=forms.Textarea(),
	)
	
	cosmetic_performs = forms.BooleanField(initial=False, required=False)
	cosmetic_work_percentage = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=100,
		initial=0,
	)
	cosmetic_elective_percentage = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=100,
		initial=0,
	)
	cosmetic_recon_percentage = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=100,
		initial=0,
	)

	laser_performs = forms.BooleanField(initial=False, required=False)
	laser_work_percentage = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=100,
		initial=0,
	)
	laser_note = forms.CharField(
		required=False,
		widget=forms.Textarea(),
	)

	nursing_performs = forms.BooleanField(initial=False, required=False)
	nursing_work_percentage = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=100,
		initial=0,
	)

	telemedicine_performs = forms.BooleanField(initial=False, required=False)
	
	entity_coverage = forms.BooleanField(initial=False, required=False)
	entity_note = forms.CharField(
		required=False,
		widget=forms.Textarea(),
	)

	professional_coverage = forms.BooleanField(initial=False, required=False)
	professional_note = forms.CharField(
		required=False,
		widget=forms.Textarea(),
	)

	claims_last_10_years = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=900,
		initial=0,
	)
	open_claims = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=900,
		initial=0,
	)
	closed_claims = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=900,
		initial=0,
	)
	board_actions_last_10_years = forms.IntegerField(
		required=True,
		min_value=0,
		max_value=900,
		initial=0,
	)
	current_carrier = forms.CharField(required=False)
	expiring_premium = forms.CharField(required=False)
	prior_acts_effective_date = forms.DateField(required=False)
	prior_acts_retroactive_date = forms.DateField(required=False)
	
	def __init__(self, *args, **kwargs):
		'''
		Customer wants note text box to be shorter.
		Initialize the State from the kwargs.
		Initialize the Counties from the State.
		'''
		super(QuickQuotePublicForm, self).__init__(*args, **kwargs)
		try:
			state = kwargs['initial']['state']
		except KeyError as e:
			print "keyerror", e

		self.fields['state'].initial = state
		self.fields['primary_practice_county'] = forms.ModelChoiceField(
			queryset=state.counties.all(),
			required=True,
		)
		self.fields['state_limit'] = forms.ModelChoiceField(
			queryset=state.limits.all(),
			required=False,
			empty_label=None,
		)

		''' Test data'''
		self.fields['agent_name'].initial = 'Sam'
		self.fields['agent_email'].initial = 'sam@jail.com'
		self.fields['agency_name'].initial = 'Iverson'
		self.fields['insured_name'].initial = 'Dr. Jackson'
		self.fields['primary_specialty_name'].initial = 'podiatry'
		self.fields['primary_practice_street'].initial = '123 Main'
		self.fields['primary_practice_building'].initial = 'Suite 100'
		self.fields['primary_practice_city'].initial = 'Orlando'
		self.fields['primary_practice_zip_code'].initial = '34556'
		self.fields['title'].initial = Title.objects.all()[1]
		self.fields['dob'].initial = '1980-12-12'
		

		for field_name in self.fields.keys():
			if any([
				'_note' in field_name,
				'note' == field_name,
			]):
				self.fields[field_name].widget=forms.Textarea(
					attrs={
						'class': 'care-note',
					}
				)

	def clean(self):
		'''Perform cross-field validation'''
		cleaned_data = super(QuickQuotePublicForm, self).clean()
		# If title is Other, user must enter the Other title.
		if all([
			cleaned_data.get('title').name == 'Other',
			cleaned_data.get('title_other') == '',
		]):
			self.add_error(
				'title_other',
				'Enter the title that is not in the list.'
			)
			self.fields['title_other'].widget.attrs.update({'autofocus': ''})

		# If secondary specialty is given, percentage must be GT zero.
		if all([
			cleaned_data.get('secondary_specialty_name'),
			cleaned_data.get('secondary_specialty_percentage', 0) == 0,
		]):
			self.add_error(
				'secondary_specialty_percentage',
				'Sub Speciality percentage must be more than zero.'
			)
			self.fields['secondary_specialty_percentage'].widget.attrs.update(
				{'autofocus': ''}
			)
		
		# Sum of specialty percentages must be 100.
		psp = cleaned_data.get('primary_specialty_percentage', 0)
		ssp = cleaned_data.get('secondary_specialty_percentage', 0)
		if psp + ssp != 100:
			self.add_error(
				'secondary_specialty_percentage',
				'Speciality percentages must total 100%.'
			)
			self.fields['secondary_specialty_percentage'].widget.attrs.update(
				{'autofocus': ''}
			)

		# If secondary state is given, percentage must be GT zero.
		if all([
			cleaned_data.get('secondary_state_coverage'),
			cleaned_data.get('secondary_state_percentage', 0) == 0,
		]):
			self.add_error(
				'secondary_state_percentage',
				'Secondary state practice percentage must be more than zero.'
			)
			self.fields['secondary_state_percentage'].widget.attrs.update(
				{'autofocus': ''}
			)
		
		# Sum of specialty percentages must be 100.
		psp = cleaned_data.get('primary_state_percentage', 0)
		ssp = cleaned_data.get('secondary_state_percentage', 0)
		if psp + ssp != 100:
			self.add_error(
				'secondary_state_percentage',
				'State practice percentages must total 100%.'
			)
			self.fields['secondary_state_percentage'].widget.attrs.update(
				{'autofocus': ''}
			)

		# If cosmetic procedures, the percentages cannot all be zero.
		if all ([
			cleaned_data.get('cosmetic_performs'),
			cleaned_data.get('cosmetic_work_percentage') == 0,
			cleaned_data.get('cosmetic_elective_percentage') == 0,
			cleaned_data.get('cosmetic_recon_percentage') == 0,
		]):
			self.add_error(
				'cosmetic_recon_percentage',
				'Enter the cosmetic procedure percentages.'
			)
			self.fields['cosmetic_recon_percentage'].widget.attrs.update(
				{'autofocus': ''}
			)

		# If laser procedures, percentage cannot be zero, description is required.
		if all ([
			cleaned_data.get('laser_performs'),
			cleaned_data.get('laser_work_percentage') == 0,
		]):
			self.add_error(
				'laser_work_percentage',
				'Enter the procedure percentage.'
			)
			self.fields['laser_work_percentage'].widget.attrs.update(
				{'autofocus': ''}
			)
		if all ([
			cleaned_data.get('laser_performs'),
			cleaned_data.get('laser_note','') == '',
		]):
			self.add_error('laser_note', 'Enter the procedure description.')
			self.fields['laser_note'].widget.attrs.update({'autofocus': ''})

		# If correctional facilities, state list is required.
		if all ([
			cleaned_data.get('correctional_performs'),
			cleaned_data.get('correctional_note','') == '',
		]):
			self.add_error(
				'correctional_note',
				'Enter the correctional facility states.'
			)
			self.fields['correctional_note'].widget.attrs.update(
				{'autofocus': ''}
			)

		# If nursing homes, percentage cannot be zero.
		if all ([
			cleaned_data.get('nursing_performs'),
			cleaned_data.get('nursing_work_percentage') == 0,
		]):
			self.add_error(
				'nursing_work_percentage',
				'Enter the nursing home percentage.'
			)
			self.fields['nursing_work_percentage'].widget.attrs.update(
				{'autofocus': ''}
			)

		# If entity coverage is request, user must enter the names.
		if all([
			cleaned_data.get('entity_coverage'),
			cleaned_data.get('entity_note', '') == '',
		]):
			self.add_error(
				'entity_coverage',
				'Enter the names of the entity or allieds.'
			)
			self.fields['entity_note'].widget.attrs.update({'autofocus': ''})

		# if professional coverage is requests, user must enter the names.
		if all([
			cleaned_data.get('professional_coverage'),
			cleaned_data.get('professional_note', '') == '',
		]):
			self.add_error(
				'professional_coverage',
				'Enter the names of the medical directors.'
			)
			self.fields['professional_note'].widget.attrs.update(
				{'autofocus': ''}
			)

		# Number of open claims + number of closed claims must equal claims last 10 years.
		total_claims = cleaned_data.get('claims_last_10_years')
		open_claims = cleaned_data.get('open_claims')
		closed_claims = cleaned_data.get('closed_claims')
		if open_claims + closed_claims != total_claims:
			self.add_error(
				'closed_claims',
				'The sum of open and closed claims must match the claim total.'
			)
			self.fields['closed_claims'].widget.attrs.update({'autofocus': ''})

		return cleaned_data

	def calculate_premiums(self):
		'''Calculate the quick quote premiums for each limit and deductible'''
		self.premiums = []
		for limit in self.fields['state_limit'].queryset:
			for deduct in self.fields['deductible'].queryset:
				dedlim = DedLimitPremium(
					limit=limit,
					deductible=deduct,
					premium=deduct.value+100
				)
				self.premiums.append(dedlim)
		self.fields['expiring_premium'].widget.attrs.update(
			{'autofocus': ''}
		)

	def create_quick_quote(self):
		'''Create and save a new quick quote, and all the Foreign Key objects.'''
		print "---> Called create_quick_quote()"
		#print self.cleaned_data
		print self.cleaned_data.get('clicked_button');
		return True

