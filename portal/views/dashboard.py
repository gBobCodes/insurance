from django.contrib.auth.decorators import login_required
from django.shortcuts import render

"""
CBV
class DashboardList(AccessMixin):
"""

@login_required
def index(request):
	return render(request, "portal/dashboard.html")
	