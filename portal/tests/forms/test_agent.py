from django.test import TestCase

from portal.forms.agent import AgentListForm
from portal.models.agent import Agent
from portal.tests.factories import AgentFactory


class AgentListFormTests(TestCase):

	def setUp(self):
		AgentFactory.create_batch(10)

	def test_filter_agents_search(self):
		'''Verify that filtered agents match the search text.'''
		search_text = 'Bob'
		test_agent = AgentFactory(name='{} Agent'.format(search_text))
		form = AgentListForm(data={'search': search_text})
		found_agents = form.filter_agents()
		self.assertIn(test_agent, found_agents)

	def test_filter_agents_state(self):
		'''Verify that filtered agents match the filter state.'''
		agent = Agent.objects.all()[0]
		test_agents = Agent.objects.filter(agency__state=agent.agency.state)
		form = AgentListForm(data={'state': agent.agency.state.id})
		found_agents = form.filter_agents()
		self.assertQuerysetEqual(
			test_agents,
			[repr(fa) for fa in found_agents]
		)

	def test_filter_agents_agency(self):
		'''Verify that filtered agents match the filter agency.'''
		agent = Agent.objects.all()[0]
		test_agents = Agent.objects.filter(agency=agent.agency)
		form = AgentListForm(data={'agency': agent.agency.id})
		found_agents = form.filter_agents()
		self.assertQuerysetEqual(
			test_agents,
			[repr(fa) for fa in found_agents]
		)