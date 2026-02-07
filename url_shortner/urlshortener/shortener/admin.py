from django.contrib import admin
from .models import ShortUrl

class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('full_url', 'short_url', 'click_count')

admin.site.register(ShortUrl, ShortUrlAdmin)
