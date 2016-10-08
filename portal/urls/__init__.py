from django.conf import settings
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from rest_framework import routers

from portal.views import (
	dashboard,
	quickquote,
	state,
)

from portal.views.agent import AgentListAPI

router = routers.DefaultRouter()
#router.register(r'agents', AgentListAPI)

urlpatterns = [
	url(r'^$', RedirectView.as_view(url=reverse_lazy('dashboard'))),
	url(r'^api/', include(router.urls)),
	url(r'^api/states/', state.StateList.as_view(), name='api-state-list'),
	url(r'^api/agents/', AgentListAPI.as_view()),
	url(r'^api-auth/', include('rest_framework.urls')),
	url(r'^agency/', include('portal.urls.agency')),
	url(r'^agent/', include('portal.urls.agent')),
	url(r'^insured/', include('portal.urls.insured')),
	url(r'^quick/', include('portal.urls.quickquote')),
#	urlpatterns = format_suffix_patterns(urlpatterns)
#	url(r'^dashboard/', include('portal.urls.dashboard')),
	url(r'^dashboard/$', dashboard.index, name='dashboard'),
	url(r'^user/', include('portal.urls.user')),
]

if 0 and settings.DEBUG:
	urlpatterns.append(url(r'^tests/', include('portal.urls.tests')))

