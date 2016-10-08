from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class AppUserChangeForm(forms.ModelForm):
	"""Form for current user to update his/her user profile."""
	class Meta:
		model = User
		fields = [
			'first_name', 
			'last_name', 
			'email', 
		]
	
	def __init__(self, *args, **kwargs):
		"""Customer wants each user to have a first name."""
		super(AppUserChangeForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = True
		self.fields['first_name'].widget.attrs.update({'autofocus': ''})

