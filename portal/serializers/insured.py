from rest_framework import serializers

from portal.models.insured import Insured


class InsuredSerializer(serializers.ModelSerializer):
	class Meta:
		model = Insured
		fields = (
			'url',
			'id',
			'name',
			'office_phone',
			'mobile_phone',
			'email',
			'note',
			'dob',
			'title',
			'title_other',
			'primary_practice',
			'secondary_practice',
		)