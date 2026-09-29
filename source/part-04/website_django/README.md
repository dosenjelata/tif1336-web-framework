# Kode Sumber Part 4: Mengenal Django Admin

Folder ini berisi kode **hasil akhir** tutorial [Part 4. Mengenal Django Admin](https://dosenjelata.github.io/tif1336-web-framework/django/admin/python/2025/09/15/django-part4-mengenal-django-admin/).
Folder ini juga menjadi **titik awal** untuk mengerjakan [Part 5. Mengenal Routing URL dan Views di Django](https://dosenjelata.github.io/tif1336-web-framework/django/url%20routing/views/python/2025/09/22/django-part5-mengenal-routing-url/).

## Cara Menjalankan

Salin folder `website_django` ini ke folder kerja Anda, lalu jalankan perintah berikut dari dalam folder tersebut:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

- `uv sync` membuat virtual environment dan menginstal Django sesuai versi di `uv.lock`.
- `migrate` membuat file database `db.sqlite3`. File database tidak disertakan di repository, jadi database Anda akan kosong.
- `createsuperuser` membuat akun untuk masuk ke halaman admin (`http://127.0.0.1:8000/admin/`). Tambahkan beberapa postingan melalui halaman admin agar halaman blog tidak kosong.
