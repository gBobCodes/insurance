from django.db.models.query import QuerySet

class StateQuerySet(QuerySet):

	def active(self):
		'''Return a queryset of States with active set to True.'''
		return self.filter(active=True)

	def inactive(self):
		'''Return a queryset of States with active set to False.'''
		return self.filter(active=False)

