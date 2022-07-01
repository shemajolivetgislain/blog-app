from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import has_privileges

@has_privileges
@login_required
def index(request):
    user=request.user
    return render(request,'index.html',{'user':user})