from django.test import TestCase

from portal.models.formcache import FormCache

class FormCacheTests(TestCase):
	'''Tests for the FormCache model.'''
	def setUp(self):
		self.cache_name = 'TestCache'
		self.test_values = {
			'first_name': 'Bob',
			'last_name': 'Collins',
		}	

		FormCache.set_form_cache(
			cache_name=self.cache_name,
			values=self.test_values,
		)

	def test_set_form_cache(self):
		'''Verify that form field values can be saved.'''
		self.assertEqual(self.test_values, FormCache.TestCache)

	def test_get_form_cache(self):
		'''Verify that the form values can be read.'''
		read_values = FormCache.get_form_cache(self.cache_name)
		self.assertEqual(self.test_values, read_values)




