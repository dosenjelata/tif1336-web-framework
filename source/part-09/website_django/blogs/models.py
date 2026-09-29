from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Menambahkan field author
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.subject or 'No subject'}"
