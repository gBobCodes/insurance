from django.test import TestCase

from portal.models.state import State
from portal.tests.factories import StateFactory

class StateQuertSetTests(TestCase):

	def setUp(self):
		'''Specify the state abbr to assure unique states in the DB.'''
		self.active_state = StateFactory(active=True, abbr='AA')
		self.inactive_state = StateFactory(active=False, abbr='BB')

	def test_active(self):
		'''Verify that .active() only returns active States.'''
		found_states = State.objects.active()
		self.assertIn(self.active_state, found_states)
		self.assertNotIn(self.inactive_state, found_states)

	def test_active(self):
		'''Verify that .inactive() only returns inactive States.'''
		found_states = State.objects.inactive()
		self.assertIn(self.inactive_state, found_states)
 		self.assertNotIn(self.active_state, found_states)


