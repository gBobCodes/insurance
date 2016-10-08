from django import forms


class SearchForm(forms.Form):
	"""Form to search a list of objects, such as Agencies, Agents, etc."""

	search = forms.CharField(
		label='',
		required=False,
		widget=forms.TextInput(
			attrs={
				'class': 'pure-input-rounded',
				'placeholder': 'search',
			}
		)
	)
	

