'''
I considered importing the model classes here,
then other files could use the simple command
	from portal.models import Agency, Agent, Insured

I decided against it to be consistent with forms, serializers
and views.

Also, there are few files that need to import multiple classes.
'''