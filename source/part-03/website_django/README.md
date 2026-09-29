# Kode Sumber Part 3: Menambahkan Fitur Post ke Aplikasi Blog

Folder ini berisi kode **hasil akhir** tutorial [Part 3. Menambahkan Fitur Post ke Aplikasi Blog](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/15/django-part3-menambahkan-data-post-ke-aplikasi-blog/).
Folder ini juga menjadi **titik awal** untuk mengerjakan [Part 4. Mengenal Django Admin](https://dosenjelata.github.io/tif1336-web-framework/django/admin/python/2025/09/15/django-part4-mengenal-django-admin/).

## Cara Menjalankan

Salin folder `website_django` ini ke folder kerja Anda, lalu jalankan perintah berikut dari dalam folder tersebut:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

- `uv sync` membuat virtual environment dan menginstal Django sesuai versi di `uv.lock`.
- `migrate` membuat file database `db.sqlite3`. File database tidak disertakan di repository, jadi database Anda akan kosong.
