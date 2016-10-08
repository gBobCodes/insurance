from rest_framework import generics, permissions

from portal.models.state import State
from portal.serializers.state import StateSerializer


class StateDetail(generics.RetrieveUpdateDestroyAPIView):
	"""Get, Update or Delete a single State instance."""
	# permissions.DjangoModelPermissions
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = State.objects.all()
	serializer_class = StateSerializer


class StateList(generics.ListCreateAPIView):
	"""Get a list of states, or create a new one."""
	# permissions.DjangoModelPermissions
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = State.objects.all()
	serializer_class = StateSerializer
