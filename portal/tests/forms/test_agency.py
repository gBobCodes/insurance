from django.test import TestCase

from portal.forms.agency import AgencyListForm
from portal.models.agency import Agency
from portal.tests.factories import AgencyFactory


class AgencyListFormTests(TestCase):

	def setUp(self):
		AgencyFactory.create_batch(10)

	def test_filter_agencies_search(self):
		'''Verify that filtered agencies match the search text.'''
		search_text = 'nova'
		test_agency = AgencyFactory(name='Test {} Agency'.format(search_text))
		form = AgencyListForm(data={'search': search_text})
		found_agencies = form.filter_agencies()
		self.assertIn(test_agency, found_agencies)

	def test_filter_agencies_state(self):
		'''Verify that filtered agencies match the filter state.'''
		agency = Agency.objects.all()[0]
		test_agencies = Agency.objects.filter(state=agency.state)
		form = AgencyListForm(data={'state': agency.state.id})
		found_agencies = form.filter_agencies()
		self.assertQuerysetEqual(
			test_agencies,
			[repr(fa) for fa in found_agencies]
		)

