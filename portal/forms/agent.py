from django import forms
from django.db.models import Model

from portal.models.agent import Agent
from .cache import CacheForm
from .agency import AgencyFilterForm
from .search import SearchForm
from .state import StateFilterForm


class AgentFilterForm(forms.Form):
	"""Form to filter a list of objects by Agent."""
	agency = forms.ModelChoiceField(
		required=False,
		queryset=Agent.objects.all(),
		empty_label='All Agents',
		widget=forms.Select(
			attrs={
				'onchange': 'this.form.submit()',
			}
		)
	)
	

class AgentListForm(
	CacheForm,
	SearchForm,
	StateFilterForm,
	AgencyFilterForm,
):
	"""Form to search and filter the list of Agents."""
	cache_name = 'agent_list'
	default_cache = {'search': '', 'state': '', 'agency': ''}

	def filter_agents(self):
		"""
		Return queryset of Agents filtered by the form fields.
		If there are less than 100 agents, display them all.
		Otherwise, make the user search or filter them.
		"""
		if Agent.objects.count() < 100:
			agents = Agent.objects.all()
		else:
			agents = Agent.objects.none()

		if self.is_valid():
			search = self.cleaned_data.get('search')
			state = self.cleaned_data.get('state')
			agency = self.cleaned_data.get('agency')
			self._set_form_cache(
				values={
					'search': search,
					'state': state,
					'agency': agency,
				}
			)

			if search:
				agents = agents.filter(name__icontains=search)
			if state:
				agents = agents.filter(agency__state=state)
			if agency:
				agents = agents.filter(agency=agency)
		return agents


class AgentModelForm(forms.ModelForm):
	"""Form to create or update an Agent."""
	class Meta:
		model = Agent
		fields = [
			'name',
			'email', 
			'mobile_phone',
			'office_phone',
			'agency',
			'note', 
		]

	def __init__(self, *args, **kwargs):
		"""Customer wants note text box to be shorter."""
		super(AgentModelForm, self).__init__(*args, **kwargs)
		self.fields['note'].widget=forms.Textarea(
			attrs={
				'class': 'care-note',
			}
		)
		self.fields['name'].widget.attrs.update({'autofocus': ''})


