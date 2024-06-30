from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

# This app will be responsible for handling user login and logout.
# Implement a normal login form with username and password fields.
# use Django's built-in authentication system to handle user authentication.

def index(request):
    return render(request, 'login/index.html')

def register(request):
    if request.method == 'POST':
        # Get the form data
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']

        # Check if passwords match
        if password1 == password2:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, 'login/register.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'login/register.html')
            else:
                # Create a new user object
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Registration successful')
                return render(request, 'login/login.html')
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'login/register.html')
    else:
        return render(request, 'login/register.html')
