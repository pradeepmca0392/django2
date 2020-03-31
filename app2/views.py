from django.shortcuts import render, redirect

from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html",{"form":form})

def home(request):
    return render(request, "registration/home.html")
