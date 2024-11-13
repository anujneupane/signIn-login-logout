from django.shortcuts import render,HttpResponseRedirect
from .form import Sign,Changeuser
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages

# Create your views here.
def Sign_up(request):
    if request.method == 'POST':
     fm = Sign(request.POST)
     if fm.is_valid():
        fm.save()
        messages.add_message(request,messages.SUCCESS,'Account Created Successfully')
    else:
      fm = Sign()
    return render(request, 'enroll/signup.html', {'form':fm})

def Login(request):
   if not request.user.is_authenticated:
      if request.method == 'POST':
         fm = AuthenticationForm(request=request, data = request.POST)
         if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(
                           username =uname, 
                           password = upass
                           )
            if user is not None:
               login(request,user)
               messages.success(request,'LogIn Successfully')
               return HttpResponseRedirect('/welcome/')
               
      else:
        fm = AuthenticationForm()
      return render(request,'enroll/login.html', {'form': fm})   
   else:
       return HttpResponseRedirect('/welcome/')
       

def welcome(request):
   if request.user.is_authenticated:
       if request.method == "POST":
          fm = Changeuser(request.POST, instance = request.user)
          if fm.is_valid():
             messages.success(request,"User Profile Modified Successfully")
             fm.save()
       else:
          fm = Changeuser(instance = request.user)
       return render(request,'enroll/welcome.html' , {'name':request.user,'form':fm})
   else:
        return HttpResponseRedirect('/login/')


def userlogout(request):
   logout(request)
   return HttpResponseRedirect('/login/')

def passchange(request):
  if request.user.is_authenticated:
   if request.method == "POST":
      fm = PasswordChangeForm(user=request.user,data=request.POST)
      if fm.is_valid():
         fm.save()
         update_session_auth_hash(request,fm.user)
         return HttpResponseRedirect('/welcome/',messages.success(request,'Password Changed Successfully') )
   else:
      fm = PasswordChangeForm(user=request.user)
   return render(request,'enroll/change.html', {'form': fm})
  else:
     return HttpResponseRedirect('/login/')
  

 

