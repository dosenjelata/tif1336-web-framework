---
layout: post
title: "Django untuk pemula - Part 8. Membuat Base Template dan Menambahkan Bootstrap CSS"
date: 2025-09-25 07:02:00 +0700
categories: [Django, Blog App, Python]
tags: [Django, Blog App, Python]
---

> **Kode sumber:** mulai dari folder [`part-07`](https://github.com/dosenjelata/tif1336-web-framework/tree/main/source/part-07/website_django), hasil akhir ada di folder [`part-08`](https://github.com/dosenjelata/tif1336-web-framework/tree/main/source/part-08/website_django).
{% raw %}

Pada bagian sebelumnya, kita telah mempelajari cara menampilkan detail dari setiap postingan blog. Pada bagian ini, kita akan mempelajari cara membuat base template yang dapat digunakan kembali untuk header dan footer di seluruh halaman web kita. Dengan menggunakan base template, kita dapat menghindari duplikasi kode dan memudahkan pemeliharaan tampilan situs web.
## Langkah 1: Membuat Base Template
Buat folder `templates` di folder utama proyek, yaitu folder yang sama dengan lokasi file `manage.py` (bukan di dalam folder `blogs`). Jalankan perintah berikut dari folder tersebut:

```bash
mkdir -p templates
```

Di dalam folder `templates`, buat file baru bernama `base.html`. File ini akan berfungsi sebagai template dasar untuk semua halaman web kita.

Sekarang proyek kita memiliki **dua** folder `templates` dengan fungsi yang berbeda:
- `blogs/templates/blogs/` berisi template khusus milik app `blogs` (daftar dan detail postingan) yang sudah kita buat di Part 6 dan 7.
- `templates/` di folder utama berisi template yang dipakai bersama oleh seluruh proyek, seperti `base.html`, header, footer, dan halaman home.

Jika Anda telah selesai mengikuti tutorial ini, struktur direktori Anda akan terlihat seperti berikut:
```
website_django/
├── blogs/
│   ├── migrations/
│   ├── templates/
│   │   └── blogs/
│   │       ├── post_list.html
│   │       └── post_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── templates/
│   ├── base.html
│   ├── home.html
│   └── partials/
│       ├── _header.html
│       └── _footer.html
├── website_django/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py      ← file baru
│   └── ...
├── manage.py
└── ...
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
Beberapa hal penting dari kode di atas:
- `{% block nama %}...{% endblock %}` mendefinisikan **blok**, yaitu bagian yang isinya dapat diganti oleh template lain. Template `base.html` memiliki blok `title`, `content`, dan `scripts`.
- `{% include "partials/_header.html" %}` menyisipkan isi file lain ke dalam template ini. Header dan footer kita pisahkan ke file tersendiri agar lebih rapi.
- Tag `<link>` dan `<script>` memuat Bootstrap langsung dari CDN (internet), sehingga kita tidak perlu mengunduh file Bootstrap. Pastikan komputer Anda terhubung ke internet agar tampilannya muncul.

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
Sekarang, kita perlu memodifikasi template `post_list.html` dan `post_detail.html` untuk menggunakan base template yang telah kita buat. Buka `blogs/templates/blogs/post_list.html` dan ubah isinya menjadi seperti berikut:
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
Perhatikan bahwa file ini tidak lagi berisi `<html>`, `<head>`, atau `<body>`. Baris `{% extends "base.html" %}` membuat template ini "mewarisi" seluruh struktur dari `base.html`. Template ini cukup mengisi blok `title` dan `content`, sedangkan header, footer, dan Bootstrap otomatis ikut dari `base.html`.

Buka `blogs/templates/blogs/post_detail.html` dan ubah isinya menjadi seperti berikut:
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
Di sini kita juga menggunakan **filter** template, yaitu penulisan dengan tanda `|`. Filter `date:"F j, Y, g:i a"` mengubah format tanggal menjadi lebih mudah dibaca (misalnya "September 25, 2025, 7:02 a.m."), dan filter `linebreaks` mengubah baris baru pada konten menjadi paragraf HTML.

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
Baris `from . import views` mengimpor file `views.py` dari folder `website_django/` yang sama dengan `urls.py`. File ini belum ada, jadi buat file baru `website_django/views.py` (di folder yang sama dengan `settings.py`, bukan `blogs/views.py`) dan isi dengan fungsi `home` berikut:
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```
## Langkah 6: Menambahkan setting untuk Templates
Secara default, Django hanya mencari template di folder `templates` milik setiap app (seperti `blogs/templates/`). Agar Django juga mencari di folder `templates/` utama yang kita buat di Langkah 1, kita perlu mendaftarkannya. Buka file `website_django/settings.py`, cari bagian `TEMPLATES`, lalu ubah `'DIRS': []` menjadi `'DIRS': [BASE_DIR / "templates"]`. `BASE_DIR` adalah folder utama proyek (lokasi `manage.py`).

Tanpa langkah ini, Django akan menampilkan error `TemplateDoesNotExist` untuk `base.html` dan `home.html`.

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
uv run python manage.py runserver
```
Buka browser Anda dan akses `http://127.0.0.1:8000/` untuk melihat halaman utama blog Anda. Pastikan Anda telah mengisi beberapa postingan di admin panel untuk melihat halaman blog (lihat bagian sebelumnya tentang halaman admin).
{% endraw %}

Berikut tampilan dari halaman utama dan halaman blog Anda:
### Halaman Utama (Home)
![Home Page]({{ '/assets/images/08-home.png' | relative_url }})*Figure 1: Tampilan Halaman Home di http://127.0.0.1:8000/*
{: style="display:block;text-align:center;font-size:0.9em;color:#555;" }

### Halaman Blog
![Blog Page]({{ '/assets/images/08-blogs.png' | relative_url }})*Figure 2: Tampilan Halaman Blog di http://127.0.0.1:8000/blogs/*
{: style="display:block;text-align:center;font-size:0.9em;color:#555;" }

### Halaman Detail Postingan
![Post Detail Page]({{ '/assets/images/08-post-detail.png' | relative_url }})*Figure 3: Tampilan Halaman Detail Postingan di http://127.0.0.1:8000/blogs/1/*
{: style="display:block;text-align:center;font-size:0.9em;color:#555;" }

## Kesimpulan
{% raw %}
Pada bagian ini, kita telah membuat base template (`base.html`) yang berisi struktur HTML, header, footer, dan Bootstrap. Halaman-halaman lain cukup menggunakan `{% extends "base.html" %}` dan mengisi blok `title` dan `content`, sehingga kita tidak perlu menulis ulang kode yang sama di setiap halaman. Jika suatu saat kita ingin mengubah header atau footer, cukup ubah satu file dan semua halaman akan ikut berubah.

Kita juga telah membuat halaman Home dengan view di level proyek (`website_django/views.py`) dan mendaftarkan folder `templates/` utama di `settings.py`. Pada tutorial berikutnya, kita akan melengkapi website dengan halaman About, informasi penulis (author) pada postingan, dan halaman Contact.
{% endraw %}

## Referensi Lanjutan
1. Template inheritance (pewarisan template) di Django: https://docs.djangoproject.com/en/6.1/ref/templates/language/#template-inheritance
2. Daftar tag dan filter bawaan Django (`extends`, `block`, `include`, `date`, `linebreaks`, dan lainnya): https://docs.djangoproject.com/en/6.1/ref/templates/builtins/
3. Dokumentasi Bootstrap 5.3: https://getbootstrap.com/docs/5.3/getting-started/introduction/

