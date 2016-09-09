from django.shortcuts import render
from .models import HomepageVisits
# Create your views here.

def home_view(request):
	visit = HomepageVisits.objects.get(id=1)
	visit.count = visit.count + 1
	visit.save()
	return render(request, 'website/index.html', {})