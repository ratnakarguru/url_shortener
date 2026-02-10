from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortUrl
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def home(request):
    short_url = None

    if request.method == "POST":
        full_url = request.POST.get("full_url")
        obj = ShortUrl.objects.create(full_url=full_url)
        short_url = request.build_absolute_uri(f'/{obj.short_url}')

    return render(request, "shortener/home.html", {"short_url": short_url})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib import messages

def login_view(request):
    # 1. Handle the POST request (When user clicks "Sign In")
    if request.method == 'POST':
        # Get data from the HTML input fields
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Success: Log the user in and create a session
            auth_login(request, user)
            return redirect('home') # Change 'home' to your actual homepage URL name
        else:
            # Failure: Send an error message back to the page
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

    # 3. Handle the GET request (Show the empty login page)
    return render(request, 'shortener/login.html')


def signup(request):
    if request.method == "POST":
        # 1. Get the data from the form
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 2. Validation: Check if email already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "That email is already registered.")
            return render(request, 'shortener/signup.html')

        # 3. Validation: Basic password check
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return render(request, 'shortener/signup.html')

        # 4. Create the User
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = full_name
            user.save()
            # 5. Auto-login the user immediately
            login(request, user)
            # 6. Redirect to home
            messages.success(request, "Account created successfully!")
            return redirect('home')

        except Exception as e:
            messages.error(request, "Something went wrong. Please try again.")
            return render(request, 'shortener/signup.html')

    # GET Request: Just show the form
    return render(request, 'shortener/signup.html')



def redirect_url(request, short_code):
    obj = get_object_or_404(ShortUrl, short_url=short_code)

    # Increment click count
    obj.click_count += 1
    obj.save()

    return redirect(obj.full_url)
