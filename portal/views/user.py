from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, UpdateView

from portal.forms.user import AppUserChangeForm
from portal.serializers.user import UserSerializer

from .mixins import AjaxableResponseMixin


class PasswordChange(LoginRequiredMixin, AjaxableResponseMixin, FormView):
	'''Current user can change his/her password.'''
	form_class = PasswordChangeForm
	template_name = 'portal/user/modal_password_change.html'
	success_url = reverse_lazy('dashboard')

	def get_form_kwargs(self):
		kwargs = super(PasswordChange, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def form_valid(self, form):
		# Updating the password logs out all other sessions for the user
		# except the current one.
		form.save()
		update_session_auth_hash(self.request, form.user)
		return super(PasswordChange, self).form_valid(form)


class ProfileUpdate(LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
	'''Current user can update his/her user profile.'''
	model = User
	form_class = AppUserChangeForm
	serializer_class = UserSerializer
	template_name = 'portal/user/modal_update_form.html'
	success_url = reverse_lazy('dashboard')

	def get_object(self, queryset=None):
		'''Primary key is not provided. Allow editing of the user record.'''
		return self.request.user
