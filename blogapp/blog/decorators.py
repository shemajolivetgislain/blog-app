from django.contrib.auth import get_user_model
from django.shortcuts import redirect
User=get_user_model()

def has_privileges(view):
    def wrapper_func(request,*args, **kwargs):
        try:
            user=request.user
            if user.groups=="MANAGER":
                return redirect('manager')
            else:
                return redirect('JUNIORS')
        except Exception:
            pass
    return wrapper_func