from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form =  RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Username: {username}, your account is created")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request,"blog/register.html",{"form":form})


def index(request):
    return render(request,"blog/index.html")


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'blog/profile.html', {'user': user})