# Kode Sumber Tutorial Django untuk Pemula

Setiap folder `part-NN/website_django` berisi kode **hasil akhir** dari tutorial Part NN. Karena setiap part melanjutkan part sebelumnya, hasil akhir sebuah part juga menjadi **titik awal** part berikutnya.

| Tutorial | Mulai dari folder | Hasil akhir |
|---|---|---|
| [Part 1. Menyiapkan Proyek Django dengan uv](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/08/django-part1-menyiapkan-proyek-django-dengan-uv/) | (folder kosong) | [`part-01`](part-01/website_django) |
| [Part 2. Membuat Blog App](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/15/django-part2-membuat-blog-app/) | [`part-01`](part-01/website_django) | [`part-02`](part-02/website_django) |
| [Part 3. Menambahkan Fitur Post ke Aplikasi Blog](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/15/django-part3-menambahkan-data-post-ke-aplikasi-blog/) | [`part-02`](part-02/website_django) | [`part-03`](part-03/website_django) |
| [Part 4. Mengenal Django Admin](https://dosenjelata.github.io/tif1336-web-framework/django/admin/python/2025/09/15/django-part4-mengenal-django-admin/) | [`part-03`](part-03/website_django) | [`part-04`](part-04/website_django) |
| [Part 5. Mengenal Routing URL dan Views di Django](https://dosenjelata.github.io/tif1336-web-framework/django/url%20routing/views/python/2025/09/22/django-part5-mengenal-routing-url/) | [`part-04`](part-04/website_django) | [`part-05`](part-05/website_django) |
| [Part 6. Menampilkan Data Blog di Halaman Web](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/22/django-part6-menampilkan-data-blog-di-halaman-web/) | [`part-05`](part-05/website_django) | [`part-06`](part-06/website_django) |
| [Part 7. Menampilkan Detail Postingan Blog](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/22/django-part7-menampilkan-detail-postingan-blog/) | [`part-06`](part-06/website_django) | [`part-07`](part-07/website_django) |
| [Part 8. Membuat Base Template dan Menambahkan Bootstrap CSS](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/25/django-part8-membuat-base-template-dan-menambah-bootstrap-css/) | [`part-07`](part-07/website_django) | [`part-08`](part-08/website_django) |
| [Part 9. Menambahkan Author, Membuat Halaman About dan Halaman Contact](https://dosenjelata.github.io/tif1336-web-framework/django/blog%20app/python/2025/09/29/django-part9-membuat-halaman-about-menambahkan-author-dan-membuat-kontak/) | [`part-08`](part-08/website_django) | [`part-09`](part-09/website_django) |

Part 0 (virtual environment dengan `venv`) hanya latihan, sehingga tidak memiliki folder kode sumber.

## Cara Menggunakan

1. Salin folder `website_django` dari part yang ingin Anda kerjakan ke folder kerja Anda. Misalnya, untuk mengerjakan Part 6, salin `part-05/website_django`.
2. Masuk ke folder tersebut dan jalankan `uv sync` lalu `uv run python manage.py migrate`.
3. Ikuti tutorialnya. Jika hasil Anda tidak berjalan, bandingkan kode Anda dengan folder hasil akhir part tersebut.

File database (`db.sqlite3`) tidak disertakan, jadi setiap folder dimulai dengan database kosong. Mulai Part 4, buat akun admin dengan `uv run python manage.py createsuperuser` dan tambahkan beberapa postingan melalui halaman admin.
