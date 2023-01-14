from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from cart.models import OrderItem, Order
from .forms import PasswordResetForm
from django.contrib.auth.models import User

# User registration view
# User has to add username, email and password
# If email is already in database user will get a message
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
            else:
                messages.error(request, 'Wystąpił błąd w trakcie zakładania konta. Spróbuj ponownie')
        else:
            form = CreateUserForm()

    return render(request,
                  'accounts/register.html',
                  {'form': form})


# User login view
# User can log in using his username and password
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


# This view doesn't have template it works as a function
def logoutUser(request):
    logout(request)
    return redirect('/accounts/login/')

# User can change his password by writing his email address and old password
# If email or old password doesn't match it will return a message
def changePassword(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            old_password = form.cleaned_data['old_password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(old_password):
                    user.set_password(form.cleaned_data['new_password'])
                    user.save()
                    login(request, user)
                    return redirect('/accounts/login')
                else:
                    messages.error(request, 'Błędna nazwa użytkownika lub hasło. Spróbuj ponownie')
            except User.DoesNotExist:
                pass
        else:
            messages.error(request, 'Błędna nazwa użytkownika lub hasło. Spróbuj ponownie')
    else:
        form = PasswordResetForm()

    return render(request,
                  'accounts/password_reset.html',
                  {'form': form})


# This view display profile of a user
# Logged user can browse his orders and other information
def profileUser(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(email=request.user.email)
    else:
        orders = []
    return render(request,
                  'accounts/profile_user.html',
                  {'orders': orders})
