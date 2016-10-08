from django.conf.urls import url

from portal.views import agent

urlpatterns = [
	url(r'^list/$', agent.AgentList.as_view(), name='agent-list'),
	url(r'^add/$', agent.AgentCreate.as_view(), name='agent-create'),
	url(r'^(?P<pk>[0-9]+)/$', agent.AgentUpdate.as_view(), name='agent-update'),
]
