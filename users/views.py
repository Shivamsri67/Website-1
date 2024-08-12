from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import Profileform
from django.contrib.auth.models import User
from .models import Profile
def register(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data.get('Username')
        
        messages.success(request,f'Welcome! {name} , Your account is created.')
        form.save()
        
        return redirect('login')
    return render(request,'users/register.html',{'form':form})
@login_required
def profilepage(request):
    return render(request,'users/profile.html')

# def passreset(request):
#     form=PasswordResetForm(request.POST)
#     if form.is_valid():
#         data=form.cleaned_data.get('email')
#         obj=User.objects.get(email=data)
#         if obj.email:
#            return redirect('setpass', email=obj.email)
        
#     return render(request,'users/passwordreset.html',{'form':form}) 
@login_required   
def passchange(request):
    form=PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("<h3>Your password is changed successfully</h3>")
    return render(request,'users/passchange.html',{'form':form})


# def setpass(request, email):
#     if email:
#         obj=User.objects.get(email=email)
#         a=SetPasswordForm(obj, request.POST)
#         if a.is_valid():
#             a.save()
#             return HttpResponse("helooooooooooooooooo")
        
#         return render(request,'users/setpass.html',{'a':a})   
    
# @login_required  
# def profilecreate(request):      
   
#     form=Profileform(request.POST, request.FILES)
#     if form.is_valid():
#         image=form.cleaned_data.get('image')
#         location=form.cleaned_data.get('location')
#         user=request.user
#         Profile.objects.create(user=user,location=location,image=image)

#         return redirect('food:index')
    
#     return render(request,'users/profilecreate.html',{'form':form})

@login_required
def profileupdate(request):
    profile=request.user.profile
    form=Profileform(request.POST or None,request.FILES,instance=profile)
    if form.is_valid():
        form.save()
        
       

        return redirect('food:index')
    
    return render(request,'users/profilecreate.html',{'form':form,'profile':profile})

