from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login 
from .models import ShortUrl
from django.contrib.auth.decorators import login_required

# --- HOME VIEW ---
def home(request):
    short_url = None

    if request.method == "POST":
        full_url = request.POST.get("full_url")
        # Create the short URL object
        if full_url:
            obj = ShortUrl.objects.create(full_url=full_url)
            short_url = request.build_absolute_uri(f'/{obj.short_url}')

    return render(request, "shortener/home.html", {"short_url": short_url})


# --- LOGIN VIEW ---
def login_view(request):
    # 1. Handle the POST request (When user clicks "Sign In")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate using email as the username
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'shortener/login.html')
    return render(request, 'shortener/login.html')


# --- SIGNUP VIEW ---
def signup(request):
    if request.method == "POST":
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')


        if User.objects.filter(username=email).exists():
            messages.error(request, "That email is already registered.")
            return render(request, 'shortener/signup.html')

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return render(request, 'shortener/signup.html')


        try:

            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = full_name
            user.save()
            
            auth_login(request, user)
            
            messages.success(request, "Account created successfully!")
            return redirect('dashboard')

        except Exception as e:
            messages.error(request, "Something went wrong. Please try again.")
            return render(request, 'shortener/signup.html')

    return render(request, 'shortener/signup.html')

@login_required(login_url='login')
def dashboard(request):
    if request.method == "POST":
        full_url = request.POST.get("full_url")
        if full_url:
            obj = ShortUrl(full_url=full_url)
            obj.user = request.user
            obj.save()
            return redirect('dashboard')

    # 2. Handle Displaying Links (GET request)
    user_links = ShortUrl.objects.filter(user=request.user).order_by('-created_at')
    total_clicks = sum(link.click_count for link in user_links)

    context = {
        'urls': user_links,
        'total_clicks': total_clicks,
        'total_links': user_links.count()
    }
    
    return render(request, 'shortener/dashboard.html', context)

# --- REDIRECT VIEW ---
def redirect_url(request, short_code):
    obj = get_object_or_404(ShortUrl, short_url=short_code)
    obj.click_count += 1
    obj.save()
    return redirect(obj.full_url)