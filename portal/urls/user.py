from django.conf.urls import url

from portal.views import user

urlpatterns = [
	url(
		r'^password_change/$',
		user.PasswordChange.as_view(),
		name='password_change'
	),
	url(
		r'^user_change/$',
		user.ProfileUpdate.as_view(),
		name='user_change'
	),
]


