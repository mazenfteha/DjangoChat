from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm 

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST': #check if the form submitted
        form = SignUpForm(request.POST)

        #check if it valid
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form':form})