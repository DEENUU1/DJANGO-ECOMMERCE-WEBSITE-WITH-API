from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# User registration view
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/product_list/')
    else:
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
    if request.user.is_authenticated:
        return redirect('/product_list/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,
                                username=username,
                                password=password)

            if user is not None:
                login(request, user)
                return redirect('/product_list/')

            else:
                messages.info(request, 'Nazwa użytkownika lub hasło są nieprawidłowe')
                return render(request,
                              'accounts/login.html')

    return render(request,
                  'accounts/login.html', )


def logoutUser(request):
    logout(request)
    return redirect('/accounts/login/')
