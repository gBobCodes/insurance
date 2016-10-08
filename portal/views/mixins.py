from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic.base import ContextMixin, View, TemplateResponseMixin
from django.views.generic.edit import FormMixin, ProcessFormView


class AjaxableResponseMixin(object):
	'''
	Mixin to add AJAX support to a form.
	If used with an object-based FormView (e.g. CreateView)
	that view should define a serializer_class
	so the object's data can be returned in the reponse.
	'''
	def form_invalid(self, form):
		response = super(AjaxableResponseMixin, self).form_invalid(form)
		if self.request.is_ajax():
			return JsonResponse(form.errors, status=400)
		else:
			return response

	def form_valid(self, form):
		'''
		Return a JsonResponse when using AJAX.
		Otherwise return a normal http response.
		Call the parent's form_valid() method because
		it might do some processing (in the case of CreateView, it will
		call form.save() for example).
		'''
		response = super(AjaxableResponseMixin, self).form_valid(form)
		if self.request.is_ajax():
			try:
				data = {
					'model': self.object.__class__.__name__,
				}
				try:
					data['instance'] = self.serializer_class(self.object).data
				except AttributeError:
					# This view does not have a serializer class.
					data['instance'] = self.object.id
			except AttributeError:
				# This view does not have an object, so use the view itself.
				data = {
					'model': self.__class__.__name__,
				}
			return JsonResponse(data)
		else:
			return response


class SessionMessageMixin(ContextMixin):
	'''
	Write and read a string in request.session dictionary.
	Define this class variable in the Views using this mixin:
	session_message = "some text to display to the user"
	'''
	def get_context_data(self, **kwargs):
		'''
		Read the message from the request.session dictionary.
		Add the message to the template context.
		'''
		context = super(SessionMessageMixin, self).get_context_data(**kwargs)
		session_message = self.request.session.get('session_message')
		if session_message:
			context['session_message'] = session_message
			# The message is only displayed once, so get rid of it.
			del self.request.session['session_message']
		return context

	def form_valid(self, form):
		'''Write the message in the request.session dictionary.'''
		response = super(SessionMessageMixin, self).form_valid(form)
		self.request.session['session_message'] = self.session_message
		return response


class MultipleFormsMixin(FormMixin):
	"""
	A mixin that provides a way to show and handle several forms in a
	request.
	"""
	form_classes = {} # set the form classes as a mapping

	def get_form_classes(self):
		return self.form_classes

	def get_forms(self, form_classes):
		return dict([(key, klass(**self.get_form_kwargs())) \
			for key, klass in form_classes.items()])

	def forms_valid(self, forms):
		return super(MultipleFormsMixin, self).form_valid(forms)

	def forms_invalid(self, forms):
		return self.render_to_response(self.get_context_data(forms=forms))


class ProcessMultipleFormsView(ProcessFormView):
	"""
	A mixin that processes multiple forms on POST. Every form must be
	valid.
	"""
	def get(self, request, *args, **kwargs):
		form_classes = self.get_form_classes()
		forms = self.get_forms(form_classes)
		return self.render_to_response(self.get_context_data(forms=forms))

	def post(self, request, *args, **kwargs):
		form_classes = self.get_form_classes()
		forms = self.get_forms(form_classes)
		if all([form.is_valid() for form in forms.values()]):
			return self.forms_valid(forms)
		else:
			return self.forms_invalid(forms)


class BaseMultipleFormsView(MultipleFormsMixin, ProcessMultipleFormsView):
	"""
	A base view for displaying several forms.
	"""

class MultipleFormsView(TemplateResponseMixin, BaseMultipleFormsView):
	"""
	A view for displaing several forms, and rendering a template response.
	"""