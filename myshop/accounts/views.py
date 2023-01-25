from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from order.models import OrderItem, Order
from .forms import PasswordResetForm, DeleteUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

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

            # This code check if email address already exist in database
            if User.objects.filter(email=form.data['email']).exists():
                messages.error(request, 'Podany email już istnieje!')

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')

                # Sending email function
                html_file = get_template('accounts/email_register.html')
                subject_email = 'Rejestracja konta'
                email_subject, shop_email, user_email = subject_email, settings.EMAIL_HOST_USER, email
                html_content = html_file.render({'username': username})
                message = EmailMultiAlternatives(email_subject, html_content, shop_email, [user_email])
                message.attach_alternative(html_content, 'text/html')
                message.send()


                messages.success(request, f'{username} Twoje konto zostało utworzone')
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

@login_required()
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
                    username = form.cleaned_data.get('username')
                    email = form.cleaned_data.get('email')
                    user.save()

                    # Email sending
                    html_file = get_template('accounts/email_changePassword.html')
                    subject_email = 'Zmiana hasła'
                    subject, shop_email, user_email = subject_email, settings.EMAIL_HOST_USER, email
                    html_content = html_file.render({'username': username})
                    message = EmailMultiAlternatives(subject, html_content, shop_email, [user_email])
                    message.attach_alternative(html_content, 'text/html')
                    message.send()


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

@login_required()
def profileUser(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(email=request.user.email)
        for order in orders:
            order.total_cost = order.get_total_cost(request)
    else:
        orders = []
    return render(request,
                  'accounts/profile_user.html',
                  {'orders': orders})


# This view allows user to delete account
# User has to be log in to delete account in his profile

@login_required()
def deleteUser(request):
    if request.user.is_authenticated:
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    user.delete()
                    logout(request)
                    messages.success(request, 'Twoje konto pomyślnie usunięte')
                    return redirect('/accounts/login')
                else:
                    messages.error(request, 'Nie udało się usunąć twojego konta. Spróbuj ponownie')
            except User.DoesNotExist:
                messages.info(request, 'To konto nie istnieje.')
        else:
            messages.error(request, 'Błędna nazwa użytkownika lub hasło. Spróbuj ponownie.')
    else:
        form = DeleteUserForm()

    return render(request,
                  'accounts/delete_user.html',
                  {'form': form})
