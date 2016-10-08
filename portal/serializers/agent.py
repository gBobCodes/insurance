from rest_framework import serializers

from portal.models.agent import Agent


class AgentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Agent
		fields = (
			'id',
			'name',
			'office_phone',
			'mobile_phone',
			'email',
			'note',
			'dob',
			'agency',
		)