from django.test import TestCase

from portal.forms.insured import InsuredListForm
from portal.models.insured import Insured
from portal.tests.factories import InsuredFactory


class InsuredListFormTests(TestCase):

	def setUp(self):
		InsuredFactory.create_batch(10)

	def test_filter_agents_search(self):
		'''Verify that filtered insureds match the search text.'''
		search_text = 'Jack'
		test_insured = InsuredFactory(name='Dr. {} Rodman'.format(search_text))
		form = InsuredListForm(data={'search': search_text})
		found_insureds = form.filter_insureds()
		self.assertIn(test_insured, found_insureds)
