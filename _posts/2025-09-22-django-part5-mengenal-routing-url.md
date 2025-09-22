---
layout: post
title: "Django untuk pemula - Part 5. Mengenal Routing URL dan Views di Django"
date: 2025-09-22 07:00:00 +0700
categories: [Django, URL Routing, Views, Python]
tags: [Django, URL Routing, Views, Python]
---

Pada bagian sebelumnya, kita telah mempelajari tentang model dan bagaimana mengelola data melalui halaman admin. Tahapan selanjutnya adalah menampilkan data tersebut di halaman web menggunakan views dan routing URL.

Sekarang, kita akan mempelajari tentang routing URL dan views di Django. Routing URL diwakili oleh file `urls.py`, sedangkan views diwakili oleh file `views.py`. File `urls.py` dan `views.py` adalah dua file inti yang bekerja sama untuk menangani permintaan (request) dari pengguna dan memberikan respons (response). Silahkan merujuk ke [Artikel HTTP Protokol](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) untuk memahami konsep request dan response.

## Apa itu Routing URL?
Routing URL adalah cara Django mengarahkan permintaan (request) dari pengguna ke **fungsi** atau **kelas** yang sesuai yang ada di Views untuk menangani permintaan tersebut.
Routing URL diatur dalam file `urls.py`. Setiap proyek Django memiliki file `urls.py` utama di dalam folder proyek (misalnya `website_django/urls.py`) dan setiap aplikasi juga dapat memiliki file `urls.py` sendiri (misalnya kita tambahkan `blogs/urls.py`).
Routing URL menggunakan pola (pattern) untuk mencocokkan URL yang diminta dengan fungsi atau kelas di Views. Pola ini ditulis menggunakan ekspresi reguler (regular expressions) atau path converters.
## Apa itu Views?
Views adalah bagian dari Django yang bertanggung jawab untuk menangani logika bisnis aplikasi web. Views menerima permintaan (request) dari pengguna, memprosesnya, dan mengembalikan respons (response) yang sesuai.
Views diatur dalam file `views.py`. Setiap aplikasi Django memiliki file `views.py` sendiri (misalnya `blogs/views.py`).
Views dapat berupa fungsi atau kelas. Fungsi views adalah fungsi Python biasa yang menerima objek request sebagai argumen dan mengembalikan objek response. Kelas views adalah kelas Python yang mewarisi dari kelas dasar Django seperti `View`, `TemplateView`, atau `ListView`.
## Contoh Implementasi Routing URL dan Views di Django
Mari kita lihat contoh implementasi routing URL dan views di Django. Kita akan menambahkan routing URL dan views untuk menampilkan Judul halaman blog kita.
### Langkah 1: Membuat Fungsi View di `views.py`
Buka file `blogs/views.py` dan tambahkan fungsi view untuk menampilkan halaman blog:
```python
from django.http import HttpResponse

def home(request):
    html_header_and_title = "<h1>Selamat Datang di Blog Saya</h1>"
    return HttpResponse(html_header_and_title)
```
Pada kode di atas, kita mengimpor `HttpResponse` dari `django.http` untuk mengembalikan respons HTTP. Fungsi `home` menerima objek `request` sebagai argumen dan mengembalikan respons berupa HTML sederhana yang menampilkan judul halaman blog.

### Langkah 2: Menambahkan Routing URL di `urls.py`
Buka file `blogs/urls.py` (jika belum ada, buat file tersebut) dan tambahkan routing URL untuk fungsi view `home`:
```python
from django.urls import path
from .views import home
urlpatterns = [
    path('', home, name='home'),
]
```
Pada kode di atas, kita mengimpor fungsi `path` dari `django.urls` dan fungsi view `home` dari file `views.py`. Perhatikan fungsi `path` yang digunakan untuk mendefinisikan pola URL. Terdapat tiga argumen utama di dalam fungsi `path`:
1. Pola URL (dalam contoh ini adalah string kosong `''` yang berarti URL dasar dari aplikasi `blogs`).
2. Fungsi atau kelas view yang akan dipanggil ketika pola URL cocok (dalam contoh ini adalah fungsi `home`).
3. Nama pola URL (opsional) yang dapat digunakan untuk merujuk ke pola URL ini di tempat lain dalam kode (misalnya dalam template--akan kita bahas lebih lanjut di artikel selanjutnya).


### Langkah 3: Menghubungkan Routing URL Aplikasi ke Proyek
Buka file `website_django/urls.py` yang merupakan file routing URL utama untuk proyek Django Anda dan tambahkan routing URL aplikasi `blogs`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls')),
]
```
Tambahan `path('blogs/', include('blogs.urls'))` menghubungkan routing URL aplikasi `blogs` ke proyek utama. Dengan ini, setiap permintaan yang dimulai dengan `blogs/` akan diteruskan ke file `blogs/urls.py` untuk penanganan lebih lanjut. Misalnya, jika Anda mengakses URL `http://127.0.0.1:8000/blogs/`, maka fungsi `home` di `blogs/views.py` akan dipanggil.
### Langkah 4: Menjalankan Server dan Mengakses Halaman Blog
Sekarang, jalankan server Django dengan perintah berikut:
```bash
python manage.py runserver
```
Buka browser dan akses URL `http://127.0.0.1:8000/blogs/`. Anda akan melihat halaman blog yang telah Anda buat di fungsi view `home`.

![Halaman Blog Menampilkan Judul]({{ '/assets/images/django-part5-blogs-page.png' }})*Figure 1: Tampilan Halaman Blog dari alamat http://127.0.0.1:8000/blogs/*
{: style="display:block;text-align:center;font-size:0.9em;color:#555;" }

Di artikel selanjutnya, kita akan menambahkan lebih banyak fitur ke halaman blog ini, seperti menampilkan daftar postingan blog dari database.
## Kesimpulan
Routing URL dan Views adalah dua komponen penting dalam pengembangan aplikasi web dengan Django. Routing URL mengarahkan permintaan pengguna ke fungsi atau kelas di Views, sedangkan Views menangani logika bisnis dan mengembalikan respons yang sesuai. Dengan memahami konsep ini, Anda dapat mulai membangun aplikasi web yang dinamis dan interaktif menggunakan Django. Pada bagian selanjutnya, kita akan mempelajari tentang template di Django untuk membuat tampilan halaman web yang lebih menarik.

## Referensi Lanjutan
- [Django Documentation - URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Django Documentation - Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Documentation - Writing your first Django app, part 4](https://docs.djangoproject.com/en/stable/intro/tutorial04/)
- [MDN Web Docs - HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)