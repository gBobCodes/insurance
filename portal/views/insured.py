from braces.views import LoginRequiredMixin, RecentLoginRequiredMixin

from rest_framework import generics, permissions

from django.conf import settings
from django.urls import reverse
from django.views.generic import (
	CreateView, 
	FormView,
	ListView,
	UpdateView,
)

from portal.forms.insured import InsuredListForm, InsuredModelForm
from portal.models.insured import Insured
from portal.serializers.insured import InsuredSerializer

from .mixins import SessionMessageMixin


class InsuredDetailAPI(generics.RetrieveUpdateDestroyAPIView):
	"""Get, Update or Delete a single Insured instance."""
	# permissions.DjangoModelPermissions
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Insured.objects.all()
	serializer_class = InsuredSerializer


class InsuredListAPI(generics.ListCreateAPIView):
	"""Get a list of Insureds, or create a new one."""
	# permissions.DjangoModelPermissions
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Insured.objects.all()
	serializer_class = InsuredSerializer


class InsuredModelView(LoginRequiredMixin, SessionMessageMixin, FormView):
	"""
	Abstract Insured model view to
	create an new Insured, or update an existing one.
	"""
	model = Insured
	form_class = InsuredModelForm
	template_name = "portal/insured/modal_edit.html"

	def get_success_url(self):
		return reverse('insured-list')


class InsuredCreate(InsuredModelView, CreateView):
	"""Create a new Insured."""
	session_message = "Insured Created"
	

class InsuredUpdate(InsuredModelView, UpdateView):
	"""Update an existing Insured."""
	session_message = "Insured Updated"
	

class InsuredList(RecentLoginRequiredMixin, SessionMessageMixin, FormView):
	"""Get a list of Insureds."""
	max_last_login_delta = settings.SESSION_TIMEOUT_SECONDS
	model = Insured
	form_class = InsuredListForm
	template_name = "portal/insured/list.html"

	def get_context_data(self, *args, **kwargs):
		"""
		Use the form to filter and search the Insureds.
		Return the context for the view.
		"""
		context = super(InsuredList, self).get_context_data(**kwargs)
		if self.request.GET:
			form = self.form_class(self.request.GET)
		else:
			form = self.form_class({})
			form.set_form_data_from_cache()
		context['insured_list'] = form.filter_insureds()
		context['form'] = form
		return context
