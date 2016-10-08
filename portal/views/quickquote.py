from random import randint
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import (
	DetailView,
	ListView,
)
from django.views.generic.edit import (
	CreateView,
	FormView,
	UpdateView,
)


from portal.forms.quickquote import QuickQuotePublicForm
from portal.forms.state import StateSelectForm
from portal.models.quickquote import QuickQuote
from portal.models.state import State

from .mixins import AjaxableResponseMixin, SessionMessageMixin


class QuickQuoteStateSelect(SessionMessageMixin, FormView):
	'''View to make the user select a State before creating a QuickQuote.'''
	form_class = StateSelectForm
	template_name = 'portal/quickquote/select_state.html'
	session_message = ""
	
	def get_success_url(self):
		'''Get the State the user selected. Pass it on to the next view.'''
		state_id = self.request.POST['state']
		try:
			pk = int(state_id)
			return reverse('quick-create',  kwargs={'pk':pk})
		except ValueError:
			# invalid input, try this view again
			return reverse('quick-select-state')


class QuickQuoteCreate(
	AjaxableResponseMixin,
	SessionMessageMixin,
	FormView,
):
	'''View to create a QuickQuote.'''
	form_class = QuickQuotePublicForm
	template_name = "portal/quickquote/create.html"
	session_message = "Quick Quote Created"
	
	def get(self, request, *args, **kwargs):
		'''Initialize the form with the State the user selected.'''
		state_id = kwargs['pk']
		state = get_object_or_404(State, pk=state_id)
		initial = {'state': state}
		form = self.form_class(initial=initial)
		form.fields['agent_name'].widget.attrs.update({'autofocus': ''})
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		state_id = kwargs['pk']
		state = get_object_or_404(State, pk=state_id)
		initial = {'state': state}
		form = self.form_class(request.POST, initial=initial)
		if form.is_valid():
			form.calculate_premiums()
			if form.cleaned_data.get('clicked_button') == 'calculate':
				return render(request, self.template_name, {'form': form})

			form.create_quick_quote()
			self.form_valid(form=form)
			return HttpResponseRedirect(reverse('quick-select-state'))

		return render(request, self.template_name, {'form': form})


	def form_valid(self, form):
		'''Set the quickquote creator to the current user.'''
		'''
		try:
			form.instance.creator = self.request.user
		except AttributeError:
			# request does not have a user, it came from public
			pass
		'''
		return super(QuickQuoteCreate, self).form_valid(form)

	def get_success_url(self):
		try:
			self.request.user
			#return reverse('quick-list')
			return reverse('quick-select-state')
		except AttributeError:
			return reverse('quick-select-state')


class QuickQuoteUpdate(
	SessionMessageMixin,
	AjaxableResponseMixin,
	UpdateView,
):
	session_message = "Quick Quote Updated"
	


