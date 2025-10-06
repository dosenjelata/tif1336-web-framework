---
layout: post
title: "Django untuk pemula - Part 9. Menambahkan Author, Membuat Halaman About dan Halaman Contact"
date: 2025-09-25 07:02:00 +0700
categories: [Django, Blog App, Python]
tags: [Django, Blog App, Python]
---
{% raw %}

Pada bagian sebelumnya, kita telah berhasil membuat website blog sederhana menggunakan Django. Website ini sangat sederhana, tetapi berfungsi dengan baik dan memiliki tampilan yang rapi berkat penggunaan Bootstrap. Beberapa best practices juga telah kita terapkan, seperti penggunaan base template untuk menghindari duplikasi kode.


Sebagai bagian dari **Continuous Improvement**, pada tutorial ini, kita akan memperbaiki beberapa aspek dari aplikasi blog kita untuk meningkatkan fungsionalitas dan tampilan.

Daftar perbaikan yang akan kita lakukan:
1. Menambahkan halaman About.
2. Menambahkan field `author` pada model `Post`.
3. Menambahkan halaman Contact.
   1. Membuat model `ContactMessage` untuk menyimpan pesan dari halaman Contact.
   2. Membuat form untuk halaman Contact.
   3. Menambahkan validasi pada form Contact.
   4. Membuat class-based view untuk menangani form Contact.
   5. Menambahkan admin interface untuk model `ContactMessage`.

## Langkah 1: Menambahkan Halaman About
Kita akan menambahkan halaman About yang berisi informasi tentang blog kita. Pertama, buat file `about.html` di dalam folder project `templates`, yaitu `templates/about.html`. Isi file tersebut dengan konten berikut:
```html
{% extends "base.html" %}
{% block title %}About - MyBlog{% endblock %}

{% block content %}
<div class="py-4">
  <h1 class="mb-3">About</h1>
  <p class="text-muted">
    MyBlog is a simple project built with Django and Bootstrap.
  </p>
</div>
{% endblock %}
```
Selanjutnya, tambahkan URL untuk halaman About di file `website_django/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls')),
    path('about/', views.about, name='about'),  # Menambahkan URL untuk halaman About
]
```
Jangan lupa untuk menambahkan fungsi `about` di file `website_django/views.py`:
```python
from django.shortcuts import render
def about(request):
    return render(request, 'about.html')
```
Paling terakhir, update href di navbar bagian About yang ada di file `templates/partials/_header.html` yang sebelumnya masih mengarah ke `#` menjadi seperti berikut:
```html
<a href="{% url 'about' %}" class="text-decoration-none">About</a>
```

## Langkah 2: Menambahkan Field Author pada Model Post
Buka file `models.py` di dalam aplikasi `blogs` dan tambahkan field `author` pada model `Post`.
```python
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
```
Setelah menambahkan field `author`, kita perlu membuat dan menjalankan migrasi untuk memperbarui database:
```bash
python manage.py makemigrations
python manage.py migrate
```
Apabila ketika menjalankan migrasi muncul pertanyaan karena field `author` tidak boleh kosong, kita bisa mengatasi ini dengan memberikan nilai default sementara. Misalnya, kita bisa menetapkan user admin sebagai author default. Sehingga, ketika diminta untuk memasukkan nilai default, masukkan ID user admin (biasanya 1):


Alternatif lainnya adalah dengan
1. Menuliskan default user ke dalam field `author`.
```python
author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Ganti 1 dengan ID user admin Anda jika berbeda
```
2. Mengijinkan field `author` untuk menerima nilai `null` dan `blank` sementara waktu:
```python
author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
```

## Langkah 3: Memperbarui Tampilan Post Detail
Buka file `templates/blogs/post_detail.html` dan perbarui tampilannya untuk menampilkan informasi author. Ubah isinya menjadi seperti berikut:
```html
{% extends "base.html" %}
{% block title %}{{ post.title }} - MyBlog{% endblock %}

{% block content %}
<article class="py-3">
  <h1 class="h2 mb-2">{{ post.title }}</h1>
  <p class="text-muted small mb-3">
    By <strong>{{ post.author.get_full_name|default:post.author.username }}</strong>
    — {{ post.published_date|date:"F j, Y, g:i a" }}
  </p>
  <hr>
  <div class="mt-3">
    {{ post.content|linebreaks }}
  </div>
</article>

<a href="{% url 'post_list' %}" class="btn btn-outline-secondary mt-4">← Back to Blog</a>
{% endblock %}
```

## Langkah 4: Menambahkan Halaman Contact
Buat model baru untuk menyimpan pesan dari halaman Contact. Buka file `models.py` di dalam aplikasi `blogs` dan tambahkan model `ContactMessage`:
```python
from django.db import models

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
```

Setelah menambahkan model `ContactMessage`, buat dan jalankan migrasi:
```bash
python manage.py makemigrations
python manage.py migrate
```

Setelah model dibuat, kita akan membuat form untuk halaman Contact. Buat file baru bernama `forms.py` di dalam aplikasi `blogs` dan tambahkan kode berikut:
```python
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@example.com"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Optional"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "How can we help?"}),
        }
```
Selanjutnya, buat view untuk menangani form Contact. Buka file `views.py` di dalam aplikasi `blogs` dan tambahkan kode berikut:
```python
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import ContactForm
from .models import ContactMessage


class ContactView(CreateView):
    template_name = "blogs/contact.html"
    form_class = ContactForm
    model = ContactMessage
    success_url = reverse_lazy("contact_thanks")

class ContactThanksView(TemplateView):
    template_name = "blogs/contact_thanks.html"
```

Selanjutnya, buat file `contact.html` di dalam folder `blogs/templates/blogs`, yaitu `templates/blogs/contact.html`, dan tambahkan kode berikut:
```html
{% extends "base.html" %}
{% block title %}Contact - MyBlog{% endblock %}

{% block content %}
<div class="py-4">
  <h1 class="mb-3">Contact</h1>
  <p class="text-muted">Send us a message. We’ll get back to you soon.</p>

  <form method="post" class="mt-3">
    {% csrf_token %}
    <div class="mb-3">
      <label class="form-label">Name</label>
      {{ form.name }}
      {% if form.name.errors %}<div class="text-danger small">{{ form.name.errors|striptags }}</div>{% endif %}
    </div>

    <div class="mb-3">
      <label class="form-label">Email</label>
      {{ form.email }}
      {% if form.email.errors %}<div class="text-danger small">{{ form.email.errors|striptags }}</div>{% endif %}
    </div>

    <div class="mb-3">
      <label class="form-label">Subject</label>
      {{ form.subject }}
      {% if form.subject.errors %}<div class="text-danger small">{{ form.subject.errors|striptags }}</div>{% endif %}
    </div>

    <div class="mb-3">
      <label class="form-label">Message</label>
      {{ form.message }}
      {% if form.message.errors %}<div class="text-danger small">{{ form.message.errors|striptags }}</div>{% endif %}
    </div>

    <button type="submit" class="btn btn-primary">Send</button>
  </form>
</div>
{% endblock %}
```

Terakhir, buat file `contact_thanks.html` di dalam folder `blogs/templates/blogs`, yaitu `templates/blogs/contact_thanks.html`, dan tambahkan kode berikut:
```html
{% extends "base.html" %}
{% block title %}Thanks - MyBlog{% endblock %}

{% block content %}
<div class="py-5 text-center">
  <h1 class="fw-bold">Thank you!</h1>
  <p class="text-muted">Your message has been received.</p>
  <a href="{% url 'home' %}" class="btn btn-outline-secondary mt-3">Back to Home</a>
</div>
{% endblock %}
```
Selanjutnya, tambahkan URL untuk halaman Contact di file `blogs/urls.py`:
```python
from django.urls import path
from .views import get_blog_posts, post_detail, ContactView, ContactThanksView
urlpatterns = [
    path('', get_blog_posts, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact/thanks/", ContactThanksView.as_view(), name="contact_thanks"),
]
```
Jangan lupa untuk mengupdate href di navbar bagian Contact yang ada di file `templates/partials/_header.html` yang sebelumnya masih mengarah ke # menjadi seperti berikut:
```html
<a href="{% url 'contact' %}" class="text-decoration-none">Contact</a>
```
## Langkah 5: Menambahkan Admin Interface untuk Model ContactMessage
Buka file `admin.py` di dalam aplikasi `blogs` dan tambahkan model `ContactMessage` ke admin interface:
```python
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    list_filter = ("created_at",)
```

Sekarang, jalankan server Django dan pergi ke halaman Contact untuk menguji form Contact. Isi form dan kirimkan. Anda akan diarahkan ke halaman terima kasih. Pesan yang dikirim akan disimpan di database. Setelah itu, buka halaman admin untuk melihat model `ContactMessage` di admin interface.
{% endraw %}
## Tampilkan Hasilnya
Sekarang, kita dapat melihat hasil perbaikan aplikasi blog kita dengan mengunjungi beberapa URL berikut:
### Halaman Home: `http://localhost:8000/` 
![Home Page]({{ '/assets/images/08-home.png' | relative_url }})
### Halaman About: `http://localhost:8000/about/`
![About Page]({{ '/assets/images/09-about.png' | relative_url }})
### Halaman Blog: `http://localhost:8000/blogs/`
![Blog Page]({{ '/assets/images/08-blogs.png' | relative_url }})
### Halaman Detail Post: `http://localhost:8000/blogs/<post_id>/` (ganti `<post_id>` dengan ID post yang ada)
![Post Detail Page]({{ '/assets/images/08-post-detail.png' | relative_url }})
### Halaman Contact: `http://localhost:8000/blogs/contact/`
![Contact Page]({{ '/assets/images/09-contact.png' | relative_url }})
### Halaman Terima Kasih Contact: `http://localhost:8000/blogs/contact/thanks/`
![Contact Thanks Page]({{ '/assets/images/09-thankyou.png' | relative_url }})
### Halaman Admin: `http://localhost:8000/admin/`
![Admin Page]({{ '/assets/images/09-admin.png' | relative_url }})
![Admin Page Contact Message]({{ '/assets/images/09-admin-messages.png' | relative_url }})

Dengan langkah-langkah di atas, kita telah berhasil memperbaiki aplikasi blog kita dengan menambahkan halaman About, menambahkan field author pada model Post, serta menambahkan halaman Contact lengkap dengan form dan penyimpanan pesan ke database. Selain itu, kita juga menambahkan admin interface untuk model ContactMessage agar kita dapat mengelola pesan yang masuk melalui halaman admin Django.

