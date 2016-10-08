from braces.views import LoginRequiredMixin, RecentLoginRequiredMixin

from rest_framework import generics, permissions

from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import (
	CreateView,
	FormView,
	ListView,
	UpdateView,
)

from portal.forms.agent import AgentListForm, AgentModelForm
from portal.models.agent import Agent
from portal.serializers.agent import AgentSerializer

from .mixins import SessionMessageMixin


class AgentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
	"""Get, Update or Delete a single Agent instance."""
	# permissions.DjangoModelPermissions
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Agent.objects.all()
	serializer_class = AgentSerializer


class AgentListAPI(generics.ListCreateAPIView):
	"""Get a list of Agents, or create a new one."""
	# permissions.DjangoModelPermissions
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Agent.objects.all()
	serializer_class = AgentSerializer


class AgentModelView(LoginRequiredMixin, SessionMessageMixin, FormView):
	"""
	Abstract agent model view to 
	create a new Agent, or update an existing one.
	"""
	model = Agent
	form_class = AgentModelForm
	template_name = "portal/agent/modal_edit.html"
	success_url = reverse_lazy('agent-list')


class AgentCreate(AgentModelView, CreateView):
	"""Create a new Agent."""
	session_message = "Agent Created"


class AgentUpdate(AgentModelView, UpdateView):
	"""Update an existing Agent."""
	session_message = "Agent Updated"
	

class AgentList(RecentLoginRequiredMixin, SessionMessageMixin, FormView):
	"""Get a list of agents."""
	max_last_login_delta = settings.SESSION_TIMEOUT_SECONDS
	model = Agent
	form_class = AgentListForm
	template_name = "portal/agent/list.html"

	def get_context_data(self, *args, **kwargs):
		'''
		Use the form to filter and search the Agents.
		Return the context for the view.
		'''
		context = super(AgentList, self).get_context_data(**kwargs)
		if self.request.GET:
			form = self.form_class(self.request.GET)
		else:
			form = self.form_class({})
			form.set_form_data_from_cache()
		context['agent_list'] = form.filter_agents()
		context['form'] = form
		return context

