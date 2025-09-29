---
layout: post
title: "Django untuk pemula - Part 8. Membuat Base Template dan Menambahkan Bootstrap CSS"
date: 2025-09-25 07:02:00 +0700
categories: [Django, Blog App, Python]
tags: [Django, Blog App, Python]
---
{% raw %}

Pada bagian sebelumnya, kita telah mempelajari cara menampilkan detail dari setiap postingan blog. Pada bagian ini, kita akan mempelajari cara membuat base template yang dapat digunakan kembali untuk header dan footer di seluruh halaman web kita. Dengan menggunakan base template, kita dapat menghindari duplikasi kode dan memudahkan pemeliharaan tampilan situs web.
## Langkah 1: Membuat Base Template
Buat folder templates di dalam direktori project Django Anda jika belum ada. Di dalam folder templates, buat file baru bernama `base.html`. File ini akan berfungsi sebagai template dasar untuk semua halaman web kita.

```bash
mkdir -p templates
```

Jika anda telah selesai mengikuti tutorial ini, Struktur direktori Anda harus terlihat seperti berikut:
```
website_django/
└── blogs/
    ├── migrations/
    ├── templates/
    │   └── blogs/
    │       ├── post_list.html
    │       └── post_detail.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── ...
└── templates/
    └── base.html
    └── home.html
    └── partials/
        ├── _header.html
        └── _footer.html
└── manage.py
└── website_django/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
    └── views.py
```
Tambahkan kode HTML berikut di dalam `templates/base.html`:
```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}MyBlog{% endblock %}</title>

    {# Bootstrap CSS #}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    {% include "partials/_header.html" %}

    <main class="container my-4">
      {% block content %}{% endblock %}
    </main>

    {% include "partials/_footer.html" %}

    {# Bootstrap JS #}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    {% block scripts %}{% endblock %}
  </body>
</html>
```
## Langkah 2: Membuat Header dan Footer Partial Templates
Buat folder baru bernama `partials` di dalam folder `templates`. Di dalam folder `partials`, buat dua file baru bernama `_header.html` dan `_footer.html`.
```bash
mkdir -p templates/partials
```
Tambahkan kode berikut di dalam `templates/partials/_header.html`:
```html
<header class="bg-light border-bottom py-2">
  <div class="container d-flex justify-content-between align-items-center">
    <a href="{% url 'home' %}" class="text-decoration-none fw-bold">MyBlog</a>

    <nav class="d-flex gap-3">
      <a href="{% url 'home' %}" class="text-decoration-none">Home</a>
      <a href="{% url 'post_list' %}" class="text-decoration-none">Blog</a>
      <a href="#" class="text-decoration-none">About</a>
      <a href="#" class="text-decoration-none">Contact</a>
    </nav>
  </div>
</header>
```

Tambahkan kode berikut di dalam `templates/partials/_footer.html`:
```html
<footer class="bg-light border-top py-3 mt-5">
  <div class="container text-center">
    <p class="mb-0">&copy; {% now "Y" %} MyBlog - All Rights Reserved</p>
  </div>
</footer>
```
## Langkah 3: Memodifikasi Template Post List dan Post Detail
Sekarang, kita perlu memodifikasi template `post_list.html` dan `post_detail.html` untuk menggunakan base template yang telah kita buat. Buka `templates/blogs/post_list.html` dan ubah isinya menjadi seperti berikut:
```html
{% extends "base.html" %}
{% block title %}Blog - MyBlog{% endblock %}

{% block content %}
<h1 class="mb-4">Blog Posts</h1>

{% if blog_posts %}
  <ul class="list-group">
    {% for post in blog_posts %}
      <li class="list-group-item">
        <a href="{% url 'post_detail' post.id %}" class="text-decoration-none">
          {{ post.title }}
        </a>
      </li>
    {% endfor %}
  </ul>
{% else %}
  <p class="text-muted">No posts available yet.</p>
{% endif %}
{% endblock %}
```

Buka `templates/blogs/post_detail.html` dan ubah isinya menjadi seperti berikut:
```html
{% extends "base.html" %}
{% block title %}{{ post.title }} - MyBlog{% endblock %}

{% block content %}
<article>
  <h1 class="mb-3">{{ post.title }}</h1>
  <p class="text-muted small">
    Published on {{ post.published_date|date:"F j, Y, g:i a" }}
  </p>
  <hr>
  <div class="mt-3">
    {{ post.content|linebreaks }}
  </div>
</article>

<a href="{% url 'post_list' %}" class="btn btn-outline-secondary mt-4">← Back to Blog</a>
{% endblock %}
```
## Langkah 4: Menambahkan Halaman Home
Buat file baru bernama `home.html` di dalam folder `templates`, yaitu `templates/home.html`, dan tambahkan kode berikut:
```html
{% extends "base.html" %}
{% block title %}Home - MyBlog{% endblock %}

{% block content %}
<div class="text-center py-5">
  <h1 class="fw-bold">Welcome to MyBlog</h1>
  <p class="lead text-muted">
    A simple blog built with Django & Bootstrap.
  </p>
  <a href="{% url 'post_list' %}" class="btn btn-primary mt-3">Read the Blog</a>
</div>
{% endblock %}
```
## Langkah 5: Menambahkan URL untuk Halaman Home
Buka file `urls.py` di dalam direktori project Anda (`website_django/urls.py`) dan tambahkan path untuk halaman home:
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls')),
]
```
Buat fungsi `home` di dalam file `views.py` di direktori project Anda (`website_django/views.py`):
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```
## Langkah 6: Menambahkan setting untuk Templates
Pastikan setting untuk templates di `settings.py` sudah benar. Buka file `settings.py` di dalam direktori project django Anda (`website_django/settings.py`) dan pastikan menambahkan 'DIRS': [BASE_DIR / "templates"]. 

Bagian TEMPLATES akan terlihat seperti berikut:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## Langkah 7: Menjalankan Server dan Melihat Hasilnya
Sekarang, jalankan server Django Anda dengan perintah berikut:
```bash
python manage.py runserver
```
Buka browser Anda dan akses `http://127.0.0.1:8000/` untuk melihat halaman utama blog Anda. Pastikan anda telah mengisi beberapa postingan di admin panel untuk melihat halaman blog (lihat bagian sebelumnya tentang halaman admin).

Dengan mengikuti langkah-langkah di atas, Anda telah berhasil membuat base template dan menambahkan file CSS menggunakan Bootstrap untuk mempercantik tampilan situs web Anda.

{% endraw %}