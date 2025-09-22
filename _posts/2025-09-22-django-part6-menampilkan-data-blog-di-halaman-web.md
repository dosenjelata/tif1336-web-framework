---
layout: post
title: "Django untuk pemula - Part 6. Menampilkan Data Blog di Halaman Web"
date: 2025-09-22 07:01:00 +0700
categories: [Django, Blog App, Python]
tags: [Django, Blog App, Python]
---

Pada bagian sebelumnya, kita telah mempelajari tentang routing URL dan views di Django. Pada bagian ini, kita akan mempelajari cara menampilkan data blog yang telah kita buat di bagian sebelumnya ke dalam halaman web menggunakan **template HTML**. Kita akan membuat fungsi view untuk mengambil data blog dari database, membuat template HTML untuk menampilkan data tersebut, dan menghubungkan semuanya melalui routing URL.

## Apa itu Template di Django?
Template di Django adalah file HTML yang berisi struktur dan tampilan halaman web. Template memungkinkan kita untuk memisahkan logika bisnis dari tampilan, sehingga memudahkan pengelolaan dan pengembangan aplikasi web. Dengan menggunakan template, kita dapat menampilkan data dinamis yang diambil dari database ke dalam halaman web.

## Dari mana data blog diambil?
Data blog diambil dari model `Post` yang telah kita buat di aplikasi blogs pada bagian sebelumnya. Model `Post` merepresentasikan struktur data blog yang disimpan di database, termasuk judul, konten, dan tanggal pembuatan blog.

Cara mengambil data blog dari model `Post` adalah dengan menggunakan ORM (*Object-Relational Mapping*) yang disediakan oleh Django. ORM adalah sebuah teknik yang memungkinkan kita untuk berinteraksi dengan database menggunakan objek dan metode dalam bahasa pemrograman Python, tanpa perlu menulis query SQL secara langsung. Dengan ORM, kita dapat dengan mudah mengambil, menambahkan, mengubah, dan menghapus data di database menggunakan kode Python yang lebih sederhana dan mudah dipahami.

Contoh penggunaan ORM untuk mengambil data blog dari model `Post` adalah sebagai berikut:
```python
from blogs.models import Post
blog_posts = Post.objects.all()
```
Pada contoh di atas, kita mengimpor model `Post` dari file `models.py`, kemudian menggunakan metode `objects.all()` untuk mengambil semua data blog yang ada di tabel `Post`.

## Menyiapkan Template HTML untuk Menampilkan Data Blog
Kita akan menyiapkan template HTML untuk menampilkan data blog tersebut. Kita akan membuat file `post_list.html` di dalam folder `templates/blogs/` yang ada di dalam aplikasi `blogs`. Setelah penambahan template, struktur direktori proyek kita akan terlihat seperti ini:
```
website_django/
│├── blogs/
│   ├── migrations/
│   ├── templates/blogs/
│   │   └── post_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│├── website_django/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```
Buka file `post_list.html` dan tambahkan kode HTML berikut:
```html
<!DOCTYPE html>
<html lang="en"></html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Blog List</title>
</head>
<body>
    <h1>Blog List</h1>
    <ul>{% raw %}
        {% for post in blog_posts %}
            <li>
                <h2>{{ post.title }}</h2>
            </li>
        {% empty %}
            <li>No blog posts available.</li>
        {% endfor %}
        {% endraw %}
    </ul>
</body>
</html>
```
Pada kode di atas, kita menggunakan sintaks template Django untuk melakukan iterasi pada variabel `blog_posts` yang akan kita kirim dari fungsi view. Setiap item dalam `blog_posts` akan ditampilkan dalam elemen `<li>`, dan menampilkan judul postingan. Judul tersebut diambil menggunakan sintaks `{{ post.title }}` dan akan ditampilkan dalam elemen `<h2>`. Jika tidak ada data blog yang tersedia, maka akan ditampilkan pesan "No blog posts available."

Sintaks Template Django memungkinkan kita untuk menambahkan logika pemrograman ke dalam HTML. Untuk informasi lebih lanjut tentang sintaks template Django, Anda dapat merujuk ke dokumentasi resmi di sini: https://docs.djangoproject.com/en/5.2/ref/templates/language/
## Membuat Fungsi View untuk Menampilkan Data Blog
Selanjutnya, kita akan membuat fungsi view di dalam file `views.py` untuk mengambil data blog dari model `Post` dan mengirimkannya ke template `post_list.html`. Berikut adalah contoh kode untuk fungsi view tersebut:
```python
from django.shortcuts import render
from .models import Post

def get_blog_posts(request):
    blog_posts = Post.objects.all()
    return render(request, 'blogs/post_list.html', {'blog_posts': blog_posts})
```
Pada kode di atas, kita mengimpor fungsi `render` dari `django.shortcuts` dan model `Post` dari file `models.py`. Fungsi `get_blog_posts` mengambil semua data blog dari model `Post` menggunakan metode `objects.all()`, kemudian mengirimkan data tersebut ke template `post_list.html` melalui konteks `{'blog_posts': blog_posts}`.
## Menambahkan Routing URL untuk Fungsi View
Setelah kita membuat fungsi view untuk menampilkan data blog, langkah selanjutnya adalah menambahkan routing URL untuk menghubungkan fungsi view tersebut dengan URL tertentu. Kita akan menambahkan routing URL di dalam file `urls.py` di aplikasi `blogs`. Kita edit file `blogs/urls.py` menjadi kode berikut:
```python
from django.urls import path
# from .views import home
from .views import get_blog_posts

urlpatterns = [
    # path('', home, name='home'),
    path('', get_blog_posts, name='home'),
]
```
Dari file `views.py`, kita mengimpor fungsi `get_blog_posts` yang telah kita buat sebelumnya menggantikan fungsi `home`. Kita juga mendisable (mengomentari) routing URL untuk fungsi `home` dan menambahkan routing URL untuk fungsi `get_blog_posts`. Dengan ini, ketika kita mengakses URL dasar dari aplikasi `blogs`, maka sekarang fungsi `get_blog_posts` akan dipanggil dan menampilkan halaman daftar blog yang telah kita buat.

## Menjalankan Server dan Mengakses Halaman Blog
Setelah kita menyelesaikan semua langkah di atas, kita dapat menjalankan server Django dan mengakses halaman blog yang telah kita buat. Berikut adalah langkah-langkah untuk menjalankan server dan mengakses halaman blog:
1. Buka terminal atau command prompt.
2. Arahkan ke direktori proyek Django Anda.
3. Jalankan perintah berikut untuk memulai server Django:
   ```bash
   python manage.py runserver
   ```
4. Buka browser web dan akses URL berikut:
   ```http://localhost:8000/blogs/```
5. Anda akan melihat halaman blog yang menampilkan daftar posting yang telah Anda buat sebelumnya.

![Halaman Blog Menampilkan Daftar Postingan]({{ '/assets/images/django-part6-post-list.png'| relative_url }})*Figure 1: Tampilan Halaman Blog berisi daftar postingan yang telah ditulis di halaman admin  *
## Kesimpulan
Pada bagian ini, kita telah mempelajari cara menampilkan data blog di halaman web menggunakan template HTML di Django. Kita telah membuat fungsi view untuk mengambil data blog dari model `Post`, menyiapkan template HTML untuk menampilkan data tersebut, dan menghubungkan semuanya melalui routing URL. Dengan memahami konsep ini, Anda dapat mulai membangun aplikasi web yang dinamis dan interaktif menggunakan Django.

## Refensi Lanjutan
1. [Django Documentation - Views](https://docs.djangoproject.com/en/4.0/topics/http/views/)
2. [Django Documentation - Templates](https://docs.djangoproject.com/en/4.0/topics/templates/)
3. [Django Documentation - URL dispatcher](https://docs.djangoproject.com/en/4.0/topics/http/urls/)
