from django.shortcuts import render
from .forms import LoginForm
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login

def user_login(request):
  if request.method == "POST":
    form = LoginForm(request.POST)

    if form.is_valid():
      cleaned_data = form.cleaned_data
      _username = cleaned_data["username"]
      _password = cleaned_data["password"]
      user = authenticate(request,username =_username,password=_password)

      if user is not None:
        if user.is_active:
          login(request,user)
          return HttpResponse("Authenticated successfully")
        else:
          return HttpResponse("Disabled account")
      else:
        return HttpResponse("Invalid login")


  else:
    form = LoginForm()
  return render(request,'pages/login.html',{"form":form})
