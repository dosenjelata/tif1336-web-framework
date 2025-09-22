# Django untuk pemula - Part 2. Membuat Blog App
Kali ini kita akan membuat app di dalam Django. App tersebut adalah sebuah Blog. Kita akan memulai dari blog yang sederhana, yaitu isi blog di masukan oleh admin dan ditampilkan di halaman blog website.

> User Story: Sebagai admin, saya ingin bisa membuat postingan blog di website Django saya. Saya juga ingin bisa mengupdate postingan tersebut dan bisa menghapusnya.

## Membuat dan menambahkan app
Untuk membuat app, perintah yang kita gunakan adalah:
```bash
python manage.py startapp blogs
```
Perintah ini akan membuat folder `blogs` di dalam direktori proyek Django kita. Struktur foldernya akan terlihat seperti ini:
```
website_django/
    ├── blogs/
    │   ├── migrations/
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
Membuat app saja tidaklah cukup. Agar app tersebut terbaca oleh Django, setelah membuat app, kita perlu mendaftarkannya di dalam `settings.py` agar Django mengenalinya. Buka file `settings.py` yang ada di dalam folder `website_django/website_django/` dan tambahkan aplikasi blogs ke dalam daftar `INSTALLED_APPS`.
Secara default, django Framework sudah menyiapkan 6 buah aplikasi bawaan yang tercantum di bagian INSTALLED_APPS , seperti yang tampil di bawah ini.
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Tambahkan `'blogs.apps.BlogsConfig',` di bagian akhir daftar `INSTALLED_APPS` sehingga menjadi seperti berikut:
```python
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs.apps.BlogsConfig',
]
```
Perhatikan bahwa menambahkan `blogs.apps.BlogsConfig` adalah cara yang direkomendasikan oleh Django untuk mendaftarkan aplikasi. `BlogsConfig` adalah kelas konfigurasi aplikasi yang dibuat secara otomatis di dalam file `apps.py` di dalam folder `blogs/` ketika kita membuat app. Dengan menambahkan aplikasi ke dalam `INSTALLED_APPS`, Django akan mengenali aplikasi tersebut dan kita dapat mulai menggunakannya dalam proyek kita.
## Kesimpulan
Dalam tutorial ini, kita telah berhasil membuat aplikasi blog di dalam proyek Django kita dan mendaftarkannya di dalam `settings.py`. Dengan langkah ini, kita telah menyiapkan dasar untuk mengembangkan aplikasi blog lebih lanjut. Pada tutorial berikutnya, kita akan menambahkan fitur post ke dalam aplikasi blog kita. Tetap ikuti tutorial selanjutnya untuk melanjutkan pengembangan aplikasi blog kita!
## Referensi Lanjutan
1. File settings.py di Django: https://docs.djangoproject.com/en/5.2/topics/settings/
2. Referensi settings.py: https://docs.djangoproject.com/en/5.2/ref/settings/
3. Panduan Lengkap tentang INSTALLED_APPS di Django: https://docs.djangoproject.com/en/5.2/ref/settings/#installed-apps
4. Konfigurasi Aplikasi di Django: https://docs.djangoproject.com/en/5.2/ref/applications/