from django import forms

from portal.models.state import State


class StateFilterForm(forms.Form):
	"""Form to filter a list of objects by State."""
	state = forms.ModelChoiceField(
		required=False,
		queryset=State.objects.active(),
		empty_label='All States',
		widget=forms.Select(
			attrs={
				'onchange': 'this.form.submit()',
			}
		)
	)
	

class StateSelectForm(forms.Form):
	"""Form to select a State from a list."""
	state = forms.ModelChoiceField(
		required=True,
		queryset=State.objects.active(),
		empty_label='Select a State',
		widget=forms.Select(
			attrs={
				'onchange': 'this.form.submit()',
			}
		)
	)
	

