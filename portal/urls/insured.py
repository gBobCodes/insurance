from django.conf.urls import url

from portal.views import insured

urlpatterns = [
	url(r'^list/$', insured.InsuredList.as_view(), name='insured-list'),
	url(r'^add/$', insured.InsuredCreate.as_view(), name='insured-create'),
	url(r'^(?P<pk>[0-9]+)/$', insured.InsuredUpdate.as_view(), name='insured-update'),
]
