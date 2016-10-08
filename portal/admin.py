# These models are maintained in the Admin panel.
from django.contrib import admin

from portal.models.county import County
from portal.models.deductible import Deductible, DedLimitMultiplier
from portal.models.limit import Limit
from portal.models.state import State
from portal.models.title import Title


admin.site.register(County)
admin.site.register(Deductible)
admin.site.register(DedLimitMultiplier)
admin.site.register(Limit)
admin.site.register(State)
admin.site.register(Title)
