from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# User registration view
def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

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
