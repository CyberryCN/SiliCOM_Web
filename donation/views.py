from django.shortcuts import render
from .models import Donor

# Create your views here.
def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'donation/donor_list.html', {'donors': donors})