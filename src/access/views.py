from django.shortcuts import render, redirect
from access.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


def register(request): 
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    context = {'form' : form}
    return render(request, 'registration/register.html', context)
