from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect


from .forms import SignUpForm  # comes from globalkitchn/accounts/forms.py


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    # take back to sign up screen
    return render(request, 'signup.html', {'form': form})
