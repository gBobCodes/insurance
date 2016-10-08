from rest_framework import serializers

from portal.models.state import State


class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model = State
		fields = (
			'id',
			'name',
			'abbr',
		)