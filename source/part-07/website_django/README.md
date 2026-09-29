# Kode Sumber Part 7: Menampilkan Detail Postingan Blog

Folder ini berisi kode **hasil akhir** tutorial [Part 7. Menampilkan Detail Postingan Blog](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/22/django-part7-menampilkan-detail-postingan-blog/).
Folder ini juga menjadi **titik awal** untuk mengerjakan [Part 8. Membuat Base Template dan Menambahkan Bootstrap CSS](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/25/django-part8-membuat-base-template-dan-menambah-bootstrap-css/).

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
