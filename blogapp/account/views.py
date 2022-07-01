from django.shortcuts import redirect, render
from account.forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def user_registration(request):
    form=RegistrationForm()
    context={
        'form':form
    }
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context={
                'form':form
            } 
    return render(request,'registration.html',context)

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('user') #None if value is null
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request,'login.html')