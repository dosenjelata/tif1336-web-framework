---
layout: post
title: "Django untuk pemula - Part 3. Menambahkan Fitur Post ke Aplikasi Blog"
date: 2025-09-15 10:00:00 +0700
categories: [Django, Blog App, Python]
tags: [Django, Blog App, Python]
---

Dalam tutorial ini, kita akan menambahkan fitur post ke aplikasi blog yang telah kita buat sebelumnya.

## Membuat model untuk blog
Agar kita dapat menyimpan data postingan blog, kita perlu membuat model. Model adalah representasi dari tabel di database. Kita akan membuat model untuk postingan blog yang berisi judul, konten, dan tanggal publikasi. Buka file `models.py` di dalam folder `blogs/` dan ubah isinya menjadi seperti berikut:
```python
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
```
Penjelasan setiap field:
- `title` menyimpan judul postingan. `CharField` digunakan untuk teks pendek, dan `max_length=200` membatasi panjangnya maksimal 200 karakter.
- `content` menyimpan isi postingan. `TextField` digunakan untuk teks panjang tanpa batas karakter.
- `published_date` menyimpan tanggal dan waktu publikasi. `default=timezone.now` berarti jika tidak diisi, tanggalnya otomatis diisi dengan waktu saat data dibuat.
- Fungsi `__str__` menentukan teks yang ditampilkan untuk setiap objek `Post`, misalnya di halaman admin nanti. Di sini kita menampilkan judulnya.

Setelah membuat model, kita perlu membuat migrasi untuk menerapkan perubahan ini ke database. Proses ini melibatkan dua langkah: 
1. membuat file migrasi, dan 
2. menerapkan migrasi tersebut ke database.

Membuat file migrasi dilakukan dengan perintah berikut di terminal:
```bash
uv run python manage.py makemigrations
```
Perintah `makemigrations` akan membuat file migrasi berdasarkan perubahan yang kita buat di model. Hasil dari perintah ini adalah sebuah file migrasi yang berisi instruksi untuk membuat tabel `Post` di database. File migrasi ini biasanya disimpan di dalam folder `migrations/` di dalam aplikasi `blogs/`. Struktur foldernya akan terlihat seperti ini:
```
website_django/
    ├── blogs/
    │   ├── migrations/
    │   │   ├── __init__.py
    │   │   └── 0001_initial.py
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── website_django/
    ├── manage.py
    └── ...
```
File `0001_initial.py` adalah file migrasi yang baru saja dibuat.

Setelah berhasil membuat file migrasi, langkah selanjutnya adalah menerapkan migrasi tersebut ke database dengan perintah berikut:
```bash
uv run python manage.py migrate
```
Jika perintah ini berhasil dijalankan, maka tabel untuk model `Post` akan dibuat di database sesuai dengan definisi model yang telah kita buat. Selain itu, perintah `migrate` juga membuat tabel-tabel untuk aplikasi bawaan Django (misalnya tabel user untuk login admin), sehingga peringatan *unapplied migrations* dari Part 1 tidak akan muncul lagi.

Secara default, Django menggunakan database SQLite yang disimpan dalam file `db.sqlite3` di folder proyek. Nama tabel dibentuk dari nama app dan nama model dalam huruf kecil, sehingga tabel untuk model `Post` bernama `blogs_post`. Jika ingin melihat isi database, Anda dapat membuka file `db.sqlite3` menggunakan aplikasi seperti [DB Browser for SQLite](https://sqlitebrowser.org/) atau ekstensi SQLite di VS Code.

Setelah tabel `Post` berhasil dibuat di database, kita dapat melanjutkan ke langkah berikutnya, yaitu mengelola data postingan blog melalui halaman admin Django.

## Kesimpulan
Dalam tutorial ini, kita telah berhasil menambahkan fitur post ke aplikasi blog dengan membuat model untuk postingan blog dan menerapkan migrasi ke database. Selanjutnya, kita akan belajar bagaimana mengelola data postingan blog melalui halaman admin Django. Tetap ikuti tutorial selanjutnya untuk melanjutkan pengembangan aplikasi blog kita!

## Referensi Lanjutan
1. Membuat Model di Django: https://docs.djangoproject.com/en/6.1/topics/db/models/
2. Migrasi Database di Django: https://docs.djangoproject.com/en/6.1/topics/migrations/
3. Tutorial Django membuat model dan mensetup database: https://docs.djangoproject.com/en/6.1/intro/tutorial02/