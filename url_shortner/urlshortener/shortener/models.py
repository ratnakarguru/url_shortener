from django.db import models
from django.contrib.auth.models import User
from .utils import generate_short_code

class ShortUrl(models.Model):
    full_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, blank=True)
    click_count = models.PositiveIntegerField(default=0) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # 3. Add the Timestamp (Required for sorting by 'newest first')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = generate_short_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_url


