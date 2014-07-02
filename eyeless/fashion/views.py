from django.shortcuts import render
from fashion.models import EyelessUser
from django.template.loader import get_template

# Create your views here.

def eyeless_user(request):
	all_users=EyelessUser.objects.all()
	return render(request, 'User.html', {'all_users': all_users})
