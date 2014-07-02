from django.shortcuts import render, get_object_or_404
from fashion.models import EyelessUser
from django.template.loader import get_template

# Create your views here.

def eyeless_user(request):
	all_users=EyelessUser.objects.all()
	return render(request, 'User.html', {'all_users': all_users})

def userview(request, EyelessUser_id):
	userView = get_object_or_404(EyelessUser, pk=EyelessUser_id)
	return render(request, 'userView.html', {'userView':userView})
