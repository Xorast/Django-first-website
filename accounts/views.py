from django.shortcuts    import render, redirect
from django.http         import HttpResponse
from django.contrib.auth import authenticate
from django.contrib      import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        # see django authentication system
        user = authenticate(username=username,password=password)
        
        # see django authentication system
        if user is not None : 
            auth.login(request, user) 
            return  redirect('/')
        
        else: 
            return HttpResponse('That user / password combination is wrong.')    
        
    else:
        return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

# def logout(request):
#     return HttpResponse('You are logged out.')

# def logout(request):
#     return redirect('/accounts/register')

def logout(request):
    auth.logout(request)
    return redirect('/')