from django.conf.urls import url

from portal.views import quickquote

urlpatterns = [
	url(
		r'^$',
		quickquote.QuickQuoteStateSelect.as_view(),
		name='quick-select-state'
	),
	url(
		r'^state/(?P<pk>[0-9]+)/$',
		quickquote.QuickQuoteCreate.as_view(),
		name='quick-create'
	),
	url(
		r'^(?P<pk>[0-9]+)/$',
		quickquote.QuickQuoteUpdate.as_view(),
		name='quick-update'
	),
]
