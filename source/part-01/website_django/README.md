# Kode Sumber Part 1: Menyiapkan Proyek Django dengan uv

Folder ini berisi kode **hasil akhir** tutorial [Part 1. Menyiapkan Proyek Django dengan uv](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/08/django-part1-menyiapkan-proyek-django-dengan-uv/).
Folder ini juga menjadi **titik awal** untuk mengerjakan [Part 2. Membuat Blog App](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/15/django-part2-membuat-blog-app/).

## Cara Menjalankan

Salin folder `website_django` ini ke folder kerja Anda, lalu jalankan perintah berikut dari dalam folder tersebut:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

- `uv sync` membuat virtual environment dan menginstal Django sesuai versi di `uv.lock`.
- `migrate` membuat file database `db.sqlite3`. File database tidak disertakan di repository, jadi database Anda akan kosong.
