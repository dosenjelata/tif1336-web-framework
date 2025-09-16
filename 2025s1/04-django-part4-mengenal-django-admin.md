---
layout: post
title: Django untuk pemula - Part 4. Mengelola Data melalui Halaman Admin
---
Setelah kita berhasil membuat aplikasi blog dan menambahkan fitur postingan pada artikel sebelumnya, sekarang kita akan mengelola data postingan blog dengan halaman admin.

## Mengelola Data Post melalui Halaman Admin
Halaman admin sangat berguna untuk mengelola data pada aplikasi web yang kita buat. Dengan halaman admin, kita dapat dengan mudah menambahkan, mengedit, dan menghapus data tanpa perlu membuat antarmuka pengguna secara manual.

## Apa itu Django Admin?
Django Admin adalah aplikasi yang disediakan oleh Django secara default untuk mengelola data aplikasi web. Halaman admin ini memungkinkan kita untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada model yang telah kita buat.

## Mengaktifkan Django Admin
Secara default, Django Admin sudah diaktifkan ketika kita membuat project Django. Jika kita melihat daftar aplikasi yang terinstal di file `settings.py`, kita akan menemukan bahwa `django.contrib.admin` sudah termasuk di dalamnya:
```python
INSTALLED_APPS = [
    ...
    'django.contrib.admin',
    ...
]
```

Namun, untuk dapat mengaksesnya, kita perlu membuat superuser terlebih dahulu. Superuser adalah akun dengan hak akses penuh yang dapat mengelola semua aspek dari aplikasi Django.
### Langkah-langkah membuat superuser
1. Buka terminal dan pastikan Anda berada di direktori proyek Django Anda (misalnya `website_django`).
2. Jalankan perintah berikut untuk membuat superuser:
   ```bash
   python manage.py createsuperuser
   ```
3. Ikuti instruksi di terminal untuk memasukkan username, email, dan password untuk superuser.
4. Setelah superuser berhasil dibuat, jalankan server Django dengan perintah:
   ```bash
   python manage.py runserver
   ```
5. Buka browser dan akses halaman admin Django di `http://127.0.0.1:8000/admin/`.  Masukkan username dan password superuser yang telah dibuat sebelumnya untuk masuk ke halaman admin.
6. Jika berhasil, Anda akan melihat halaman admin Django yang menampilkan berbagai model yang telah didaftarkan. Untuk saat ini hanya model User dan Group yang tersedia secara default. Model `Post` yang kita buat sebelumnya belum muncul karena kita belum mendaftarkannya di halaman admin.
## Menambahkan Model Post ke Django Admin
Agar model yang kita buat di aplikasi blog dapat dikelola melalui halaman admin, kita perlu mendaftarkannya di file `admin.py` di dalam folder aplikasi blog. Berikut adalah langkah-langkahnya:
1. Buka file `admin.py` di dalam folder `blogs/`.
2. Tambahkan kode berikut untuk mendaftarkan model `Post`:
   ```python
   from django.contrib import admin
   from .models import Post

   admin.site.register(Post)
   ```
3. Simpan perubahan pada file `admin.py`.
4. Sekarang, ketika Anda masuk ke halaman admin Django, Anda akan melihat model `Post` yang telah didaftarkan. Anda dapat menambahkan, mengedit, dan menghapus postingan blog melalui antarmuka admin ini.

## Kesimpulan
Django Admin adalah alat yang sangat berguna untuk mengelola data aplikasi Django. Dengan mengikuti langkah-langkah di atas, Anda dapat dengan mudah membuat superuser dan mendaftarkan model ke halaman admin. Halaman admin ini akan membantu Anda dalam mengelola konten aplikasi tanpa perlu membuat antarmuka pengguna secara manual. Selamat mencoba!

## Referensi lanjutan
1. Membuat Superuser di Django: https://docs.djangoproject.com/en/5.2/ref/django-admin/#createsuperuser
2. Mengatur dan mengkustomisasi halaman admin: https://docs.djangoproject.com/en/5.2/ref/contrib/admin/
