from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# User registration view
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'{user} Twoje konto zostało utworzone')

            return redirect('/accounts/login/')

    return render(request,
                  'accounts/register.html',
                  {'form': form,
                   })


# User login view
def loginPage(request):
    context = {}
    return render(request,
                  'accounts/login.html',
                  context)

