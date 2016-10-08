from rest_framework import serializers

from portal.models.agency import Agency


class AgencySerializer(serializers.ModelSerializer):
	class Meta:
		model = Agency
		fields = (
			'url',
			'id',
			'name',
			'office_phone',
			'note',
			'street',
			'building',
			'city',
			'county',
			'state',
			'zip_code',
		)