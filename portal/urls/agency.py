from django.conf.urls import url

from portal.views import agency

urlpatterns = [
	url(r'^list/$', agency.AgencyList.as_view(), name='agency-list'),
	url(r'^add/$', agency.AgencyCreate.as_view(), name='agency-create'),
	url(r'^(?P<pk>[0-9]+)/$', agency.AgencyUpdate.as_view(), name='agency-update'),
]
