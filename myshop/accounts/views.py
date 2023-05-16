from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from order.models import Order
from .forms import PasswordResetForm, DeleteUserForm
from django.contrib.auth.models import User
from .email import send_email
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


# User registration view
# User has to add username, email and password
# If email is already in database user will get a message


class SignUpView(View):
    form_class = CreateUserForm
    template_name = "accounts/user_register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/product_list")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if User.objects.filter(email=form.data["email"]).exists():
            messages.error(request, "Ten email jest już zarejestrowany")

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            send_email(
                "To jest temat wiadomości",
                "emails/email_register.html",
                username,
                email,
            )
            messages.success(request, "Twoje konto zostało utworzone")
            return redirect("/accounts/login")
        else:
            messages.error(request, "Nie udało się założyć konta")

        return render(request, self.template_name, {"form": form})


# User login view
# User can log in using his username and password


class SignInView(LoginView):
    template_name = "accounts/user_login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("shop:product_list")
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("shop:product_list")
        else:
            messages.info(request, "Logowanie nieudane. Spróbuj ponownie")
            return render(request, self.template_name)


# This view doesn't have template it works as a function


class LogoutUserView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect("shop:product_list")


# User can change his password by writing his email address and old password
# If email or old password doesn't match it will return a message


class PasswordResetView(View):
    template_name = "accounts/user_passwordReset.html"
    form_class = PasswordResetForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            old_password = form.cleaned_data["old_password"]
            username = form.cleaned_data.get("username")

            try:
                user = User.objects.get(email=email)

                if user.check_password(old_password):
                    user.set_password(form.cleaned_data["new_password"])
                    user.save()

                    send_email(
                        "To jest temat wiadomości",
                        "emails/email_changePassword.html",
                        username,
                        email,
                    )

                    login(request, user)
                    return redirect("/accounts/login")
                else:
                    messages.error(request, "Nie udało się zmienić hasła")
            except User.DoesNotExist:
                pass

        return render(request, self.template_name, {"form": form})


# This view display profile of a user
# Logged user can browse his orders and other information


class ProfilView(LoginRequiredMixin, View):
    template_name = "accounts/user_profile.html"

    def get(self, request):
        if request.user.is_authenticated:
            orders = Order.objects.filter(email=request.user.email)
            for order in orders:
                order.total_cost = order.get_total_cost(request)
        else:
            orders = []

        return render(request, self.template_name, {"orders": orders})


# This view allows user to delete account
# User has to be log in to delete account in his profile


class DeleteUserView(LoginRequiredMixin, View):
    template_name = "accounts/user_delete.html"
    form_class = DeleteUserForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    user.delete()
                    logout(request)
                    messages.success(request, "Usunięto konto")
                    return redirect("/accounts/login")

                else:
                    messages.error(request, "Usuwanie konta nie powiodło się")
            except User.DoesNotExist:
                messages.info(request, "To konto nie istnieje")
        else:
            messages.error(request, "Usuwanie konta nie powiodło się")

        return render(request, self.template_name, {"form": form})
