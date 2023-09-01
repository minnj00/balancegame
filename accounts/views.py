from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('questions:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save() 
            auth_login(request, user)
            return redirect('accounts:login')


    else: 
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'account_form.html', context) 
 
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        
        if form.is_valid():
            auth_login(request, form.get_user())
          

    


            return redirect('questions:index')
  

    else:
        form = CustomAuthenticationForm()

    context ={
        'form': form,

    }
    return render(request, 'account_form.html', context)

def logout(request):
    auth_logout(request)
    return redirect ('accounts:login')
