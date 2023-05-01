from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from users.forms import FormRegister, EditUserData

def login(request):
    
    if(request.method=="POST"):
        form=AuthenticationForm(request, data=request.POST)
        
        if(form.is_valid()):
            user_name=form.cleaned_data.get('username')
            psw= form.cleaned_data.get('password')
            user=authenticate(username=user_name, password=psw)
            django_login(request, user)
            return redirect('article:home')
        else:
            return render(request, 'login.html',{'form':form})
        
    form=AuthenticationForm()
    
    return render(request, 'login.html',{'form':form})

def check_in(request):
    
    
    if(request.method=='POST'):
        form=FormRegister(request.POST)
        
        if(form.is_valid()):
            
            form.save()
            return redirect('users:login')
            
        else:
            return render(request, 'checkin.html',{'form':form}) 
    
    
    form=FormRegister()
    return render(request, 'checkin.html',{'form':form})

@login_required
def edit_profile(request):
     
    if(request.method=='POST'):
        form=EditUserData(request.POST, instance=request.user)
        
        if(form.is_valid()):
            form.save()
            return redirect('article:home')
            
        else:
            return render(request, 'edit_data.html',{'form':form}) 
    
    
    form=EditUserData(instance=request.user)
    return render(request, 'edit_data.html',{'form':form})

class EditPassword(PasswordChangeView):
    template_name='edit_password.html'
    success_url= reverse_lazy('article:home')
 


