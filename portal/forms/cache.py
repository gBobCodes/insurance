from django import forms
from django.db.models import Model

from portal.models.formcache import FormCache


class CacheForm(forms.Form):
	"""
	Form that know how to save its values in cache.
	cache_name and default_cache need to be set by the subclass.
	"""
	cache_name = 'needs to be set by subclass'
	default_cache = {}

	def _get_form_cache(self):
		"""Return the previously saved form values from the cache. """
		cache = FormCache.get_form_cache(cache_name=self.cache_name)
		if cache is None:
			cache = self.default_cache
			FormCache.set_form_cache(
				cache_name=self.cache_name,
				values=cache,
			)
		return cache

	def _set_form_cache(self, values):
		"""
		Save the user entered values in the FormCache class.
		Input: values is a dictionary.
		"""
		cache = {}
		for key in values.keys():
			value = values[key]
			# If the value is an instance of a database Model, save the instance.id
 			if isinstance(value, Model):
 				cache[key] = value.id
 			else:
 				cache[key] = value
		FormCache.set_form_cache(cache_name=self.cache_name, values=cache)

	def set_form_data_from_cache(self):
		"""Set the form data values from the previously saved values in cache. """
		self.data = self._get_form_cache()

