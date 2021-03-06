from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """register new user"""
    if request.method != 'POST':
        #make empty form
        form = UserCreationForm()
    else:
        #
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #log in new user
            login(request, new_user)
            return redirect('blogs:index')
    # show empty form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
    

# Create your views here.
