---
layout: post
title: "Django untuk pemula - Part 1. Menyiapkan Proyek Django dengan uv"
date: 2025-09-08 11:00:00 +0700
categories: [Django, Blog App, Python]
tags: [Django, Python, uv]
---

> **Kode sumber:** hasil akhir tutorial ini ada di folder [`part-01`](https://github.com/dosenjelata/tif1336-web-framework/tree/main/source/part-01/website_django). Lihat juga [daftar kode sumber semua part](https://github.com/dosenjelata/tif1336-web-framework/tree/main/source).

Pada seri tutorial ini, kita akan membangun sebuah website blog menggunakan Django. Sebelum menulis kode, kita perlu menyiapkan lingkungan kerja terlebih dahulu. Pada bagian pertama ini, kita akan menggunakan **uv** untuk mengelola versi Python, virtual environment, dan paket-paket yang dibutuhkan, lalu membuat proyek Django bernama `website_django`.

## Apa itu uv?
[uv](https://docs.astral.sh/uv/) adalah *package manager* dan *project manager* untuk Python yang dikembangkan oleh Astral. uv menggantikan beberapa alat sekaligus, seperti `pip`, `venv`, dan `pip-tools`.

Pada [Part 0]({{ site.baseurl }}{% post_url 2025-09-08-membuat-virtualenvirontment %}), kita sudah mengenal cara membuat virtual environment dengan `python -m venv`, mengaktifkannya, lalu menginstal paket dengan `pip`. Dengan uv, langkah-langkah tersebut menjadi lebih sederhana:

| Kebutuhan | Cara lama (`venv` + `pip`) | Dengan uv |
|---|---|---|
| Membuat virtual environment | `python -m venv .venv` | otomatis saat `uv add` / `uv run` |
| Mengaktifkan virtual environment | `source .venv/bin/activate` | tidak perlu, cukup `uv run` |
| Menginstal paket | `pip install Django` | `uv add django` |
| Mencatat daftar paket | `pip freeze > requirements.txt` | otomatis di `pyproject.toml` dan `uv.lock` |
| Menginstal ulang di komputer lain | `pip install -r requirements.txt` | `uv sync` |
| Menginstal versi Python tertentu | unduh manual dari python.org | `uv python install 3.13` |

Kelebihan lain dari uv adalah kecepatannya. uv ditulis dengan bahasa Rust dan dapat menginstal paket jauh lebih cepat dibandingkan `pip`.

## Langkah 1: Menginstal uv
- Di macOS/Linux:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- Di Windows (PowerShell):
  ```bash
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

Setelah instalasi selesai, tutup lalu buka kembali terminal Anda, kemudian pastikan uv sudah terinstal:
```bash
uv --version
```
Perintah ini akan menampilkan versi uv yang terinstal, misalnya `uv 0.11.16`.

## Langkah 2: Membuat Proyek dengan `uv init`
Buka terminal, masuk ke folder tempat Anda biasa menyimpan proyek, lalu jalankan:
```bash
uv init website_django --python 3.13
cd website_django
```
Perintah `uv init` membuat folder `website_django` beserta beberapa file awal. Opsi `--python 3.13` menentukan versi Python yang digunakan proyek. Jika Python 3.13 belum ada di komputer Anda, uv akan mengunduhnya secara otomatis, jadi Anda tidak perlu menginstal Python secara manual. Kita menggunakan Python 3.13 karena Django 6 yang akan kita pakai membutuhkan minimal Python 3.12.

Struktur folder yang dihasilkan:
```
website_django/
    ├── .gitignore
    ├── .python-version
    ├── README.md
    ├── main.py
    └── pyproject.toml
```
- `.python-version` berisi versi Python yang digunakan proyek.
- `pyproject.toml` adalah file konfigurasi proyek, termasuk daftar paket (dependensi) yang dibutuhkan.
- `main.py` adalah contoh file Python. File ini tidak kita perlukan dan boleh dihapus.

## Langkah 3: Menambahkan Django
Untuk menginstal Django, gunakan perintah `uv add`:
```bash
uv add django
```
Perintah ini melakukan tiga hal sekaligus:
1. Membuat virtual environment di folder `.venv` (jika belum ada).
2. Menginstal Django ke dalam virtual environment tersebut.
3. Mencatat Django sebagai dependensi di `pyproject.toml` dan mengunci versi pastinya di file `uv.lock`.

Buka file `pyproject.toml`, maka Django akan tercantum di bagian `dependencies`:
```toml
[project]
name = "website-django"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "django>=6.1.1",
]
```

Untuk memastikan Django telah terinstal dan melihat versinya, gunakan perintah:
```bash
uv run python -m django --version
```
Jika berhasil, perintah tersebut akan menampilkan versi Django yang terinstal, misalnya:
```bash
6.1.1
```

## Mengenal `uv run`
Perhatikan bahwa kita tidak mengaktifkan virtual environment sama sekali. Perintah `uv run` menjalankan perintah di dalam virtual environment proyek secara otomatis. Sebelum menjalankan perintah, uv juga memastikan semua paket di `pyproject.toml` sudah terinstal.

Oleh karena itu, pada seluruh seri tutorial ini, setiap perintah Python dan Django akan diawali dengan `uv run`, misalnya:
```bash
uv run python manage.py runserver
```

## Langkah 4: Membuat Proyek Django
Masih di dalam folder `website_django`, jalankan perintah berikut:
```bash
uv run django-admin startproject website_django .
```
Tanda titik (`.`) di akhir perintah berarti proyek Django dibuat di folder saat ini, sehingga tidak ada folder bersarang tambahan. Hapus juga file `main.py` karena tidak digunakan. Struktur folder sekarang menjadi:
```
website_django/
    ├── .venv/
    ├── website_django/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── .gitignore
    ├── .python-version
    ├── README.md
    ├── manage.py
    ├── pyproject.toml
    └── uv.lock
```
- `manage.py` adalah skrip untuk menjalankan berbagai perintah Django, seperti menjalankan server dan migrasi database.
- Folder `website_django/website_django/` berisi konfigurasi proyek, antara lain `settings.py` dan `urls.py`.

## Langkah 5: Menjalankan Server Pengembangan
Jalankan server pengembangan Django dengan perintah:
```bash
uv run python manage.py runserver
```
Buka browser dan akses alamat `http://127.0.0.1:8000/`. Jika berhasil, Anda akan melihat halaman selamat datang Django bergambar roket.

Di terminal mungkin muncul peringatan `You have 18 unapplied migration(s)`. Peringatan ini normal dan akan kita selesaikan pada Part 3 saat menjalankan perintah `migrate`. Tekan `Ctrl+C` untuk menghentikan server.

## Langkah 6: Menghubungkan VS Code dengan Virtual Environment
Agar VS Code mengenali Django (untuk autocomplete dan pengecekan error), pilih interpreter Python dari virtual environment proyek:
1. Tekan `Ctrl+Shift+P` (atau `Cmd+Shift+P` di macOS).
2. Pilih **Python: Select Interpreter**.
3. Pilih interpreter yang berada di folder `.venv`.

## Tips: Bekerja di Komputer Lain
Jika Anda meng-clone proyek ini ke komputer lain (misalnya dari GitHub), cukup jalankan:
```bash
uv sync
```
uv akan membuat virtual environment dan menginstal paket-paket persis sesuai versi yang tercatat di `uv.lock`. Karena itu, file `pyproject.toml` dan `uv.lock` perlu ikut di-commit ke Git, sedangkan folder `.venv` tidak (sudah diabaikan melalui `.gitignore`).

## Kesimpulan
Dalam tutorial ini, kita telah menginstal uv, membuat proyek Python dengan `uv init`, menambahkan Django dengan `uv add`, membuat proyek Django dengan `django-admin startproject`, dan menjalankan server pengembangan dengan `uv run`. Pada tutorial berikutnya, kita akan membuat aplikasi blog di dalam proyek Django ini.

## Referensi Lanjutan
1. Dokumentasi uv: https://docs.astral.sh/uv/
2. Bekerja dengan proyek di uv: https://docs.astral.sh/uv/guides/projects/
3. Menginstal Python dengan uv: https://docs.astral.sh/uv/guides/install-python/
4. Tutorial resmi Django, part 1: https://docs.djangoproject.com/en/6.1/intro/tutorial01/
