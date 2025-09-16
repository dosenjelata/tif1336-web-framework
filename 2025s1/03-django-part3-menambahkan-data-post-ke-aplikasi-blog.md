---
title: Django untuk pemula - Part 3. Menambahkan Fitur Post ke Aplikasi Blog
---
Dalam tutorial ini, kita akan menambahkan fitur post ke aplikasi blog yang telah kita buat sebelumnya.

## Membuat model untuk blog
Agar kita dapat menyimpan data postingan blog, kita perlu membuat model. Model adalah representasi dari tabel di database. Kita akan membuat model untuk postingan blog yang berisi judul, konten, dan tanggal publikasi. Buka file `models.py` di dalam folder `blogs/` dan tambahkan kode berikut:
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
Setelah membuat model, kita perlu membuat migrasi untuk menerapkan perubahan ini ke database. Proses ini melibatkan dua langkah: 
1. membuat file migrasi, dan 
2. menerapkan migrasi tersebut ke database.

Membuat file migrasi dilakukan dengan perintah berikut di terminal:
```bash
python manage.py makemigrations
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
python manage.py migrate
```
Jika perintah ini berhasil dijalankan, maka tabel `Post` akan dibuat di database sesuai dengan definisi model yang telah kita buat. Kita dapat memeriksa database untuk memastikan bahwa tabel tersebut telah dibuat dengan benar.
<<gambar tabel post di database sqlite>>
Setelah tabel `Post` berhasil dibuat di database, kita dapat melanjutkan ke langkah berikutnya, yaitu mengelola data postingan blog melalui halaman admin Django.

## Kesimpulan
Dalam tutorial ini, kita telah berhasil menambahkan fitur post ke aplikasi blog dengan membuat model untuk postingan blog dan menerapkan migrasi ke database. Selanjutnya, kita akan belajar bagaimana mengelola data postingan blog melalui halaman admin Django. Tetap ikuti tutorial selanjutnya untuk melanjutkan pengembangan aplikasi blog kita!

## Refensi Lanjutan
1. Membuat Model di Django: https://docs.djangoproject.com/en/5.2/topics/db/models/
2. Migrasi Database di Django: https://docs.djangoproject.com/en/5.2/topics/migrations/
3. Tutorial Django membuat model dan mensetup database: https://docs.djangoproject.com/en/5.2/intro/tutorial02/