from django.shortcuts import render,HttpResponseRedirect
from .form import Sign
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
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
               messages.add_message(request,messages.SUCCESS,'LogIn Successfully')
               return HttpResponseRedirect('/welcome/')
            messages.error(request, "wrong username or password!")
            return HttpResponseRedirect('/login/')
         messages.error(request, "wrong username or password!")
         return HttpResponseRedirect('/welcome/')
               
      else:
            fm = AuthenticationForm()
            return render(request,'enroll/login.html', {'form': fm})   
    
   else:
       return HttpResponseRedirect('/welcome/')
       

def welcome(request):
   if request.user.is_authenticated:
       return render(request,'enroll/welcome.html' , {'name':request.user})
   else:
        return HttpResponseRedirect('/login/')


def userlogout(request):
   logout(request)
   return HttpResponseRedirect('/login/')