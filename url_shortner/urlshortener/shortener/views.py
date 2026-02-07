from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortUrl

def home(request):
    short_url = None

    if request.method == "POST":
        full_url = request.POST.get("full_url")

        # create entry in DB
        obj = ShortUrl.objects.create(full_url=full_url)

        short_url = request.build_absolute_uri(f'/{obj.short_url}')

    return render(request, "shortener/home.html", {"short_url": short_url})


def redirect_url(request, short_code):
    obj = get_object_or_404(ShortUrl, short_url=short_code)
    return redirect(obj.full_url)
