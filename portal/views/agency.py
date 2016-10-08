from braces.views import LoginRequiredMixin, RecentLoginRequiredMixin

from rest_framework import generics, permissions, viewsets

from django.conf import settings
from django.urls import reverse
from django.views.generic import (
	CreateView,
	FormView,
	ListView,
	UpdateView,
)

from portal.apps import PortalConfig

from portal.forms.agency import AgencyListForm, AgencyModelForm
from portal.models.agency import Agency
from portal.serializers.agency import AgencySerializer

from .mixins import SessionMessageMixin


class AgencyDetailAPI(generics.RetrieveUpdateDestroyAPIView):
	"""Get, Update or Delete a single Agency instance."""
	# permissions.DjangoModelPermissions
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Agency.objects.all()
	serializer_class = AgencySerializer


class AgencyListAPI(generics.ListCreateAPIView):
	"""Get a list of agencies, or create a new one."""
	# permissions.DjangoModelPermissions
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Agency.objects.all()
	serializer_class = AgencySerializer


class AgencyModelView(LoginRequiredMixin, SessionMessageMixin, FormView):
	"""
	Abstract agency model view to 
	create a new Agency, or update an existing one.
	"""
	model = Agency
	form_class = AgencyModelForm
	template_name = "portal/agency/modal_edit.html"

	def get_success_url(self):
		return reverse('agency-list')


class AgencyCreate(AgencyModelView, CreateView):
	"""Create a new Agency."""
	session_message = "Agency Created"


class AgencyUpdate(AgencyModelView, UpdateView):
	"""Update an Agency."""
	session_message = "Agency Updated"
	

class AgencyList(RecentLoginRequiredMixin, SessionMessageMixin, FormView):
	"""Get a list of agencies."""
	max_last_login_delta = settings.SESSION_TIMEOUT_SECONDS
	model = Agency
	form_class = AgencyListForm
	template_name = "portal/agency/list.html"

	def get_context_data(self, *args, **kwargs):
		"""
		Use the form to filter and search the Agencies.
		Return the context for the view.
		"""
		context = super(AgencyList, self).get_context_data(**kwargs)
		if self.request.GET:
			form = self.form_class(self.request.GET)
		else:
			form = self.form_class({})
			form.set_form_data_from_cache()
		context['agency_list'] = form.filter_agencies()
		context['form'] = form
		return context



