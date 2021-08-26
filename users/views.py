from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .form import ContactForm
from .models import MyUser, MyUserManager
from django.contrib.auth.models import User


# Create your views here.
def loginpage(request):
    return render(request, 'users/login.html')


def dologin(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        # import pdb;pdb.set_trace()
        login(request, user)
        return HttpResponseRedirect('/recipes')
    else:
        return render(request, 'users/login.html',{'message':"Email and Password are not valid."})
        # return HttpResponseRedirect('/users/')
        # return HttpResponseRedirect('/users/' + "Username and Password are not valid.")


def register(request):
    return render(request, 'users/register.html')


def saveuser(request):
    MyUser.objects.create_user(first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'), email=request.POST.get('email'),
                password=request.POST.get('password'), mobile_no=request.POST.get('mobile_no'), date_of_birth=request.POST.get('date_of_birth'), age=request.POST.get('age'), country=request.POST.get('country'))
    # user.set_password(user.password) # convert plain password into hashed
    # user.save()
    return HttpResponseRedirect('/users')

def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/users/')

def contact_form(request):
    if request.method == "GET":
        return render(request, "users/contact_form.html",{"form":ContactForm()})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            cc_myself = form.cleaned_data["cc_myself"]
            return render(request, "users/contact_form.html",{"form":ContactForm()})
        else:
            return render(request, "users/contact_form.html", {"form": ContactForm(),"errors":form.errors})
