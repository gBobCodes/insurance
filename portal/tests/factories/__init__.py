import factory

from portal.models.agency import Agency
from portal.models.agent import Agent
from portal.models.insured import Insured
from portal.models.state import State
from portal.models.title import Title


class StateFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = State

	active = True
	#abbr = factory.Faker('state_abbr')
	abbr = factory.Sequence(lambda n: '%s' % n)
	#name = factory.Faker('state')
	name = factory.Sequence(lambda n: 'State%s' % n)

class AgencyFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Agency

	street = factory.Faker('street_address')
	building = factory.Faker('secondary_address')
	city = factory.Faker('city')
	state = factory.SubFactory(StateFactory)
	zip_code = factory.Faker('zipcode')
	name = factory.Faker('company')
	office_phone = factory.Faker('phone_number')
	note = factory.Faker('text')


class AgentFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Agent

	name =  factory.Faker('name')
	office_phone = factory.Faker('phone_number')
	mobile_phone = factory.Faker('phone_number')
	email = factory.Faker('email')
	dob = factory.Faker('date')
	note = factory.Faker('text')
	agency = factory.SubFactory(AgencyFactory)


class TitleFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Title

	name = factory.Sequence(lambda n: 'MD%s' % n)


class InsuredFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Insured

	name =  factory.Faker('name')
	title = factory.SubFactory(TitleFactory)

