from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:   
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Sorry, you are not authorized to View this Page!')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
            
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'customers':
            return redirect('user')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
            
        # else:
        #      return HttpResponse('Hey, You are not in any!')
    return wrapper_function