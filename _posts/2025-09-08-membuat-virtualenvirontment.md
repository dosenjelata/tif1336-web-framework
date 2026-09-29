---
layout: post
title: "Django untuk pemula - Part 0. Membuat Virtual Environment di Python"
date: 2025-09-08 10:00:00 +0700
categories: [Python, Virtual Environment, Django]
tags: [Python, Virtual Environment, Django]
---

Sebelum mulai membangun website dengan Django, kita perlu memahami konsep virtual environment terlebih dahulu. Pada bagian ini kita akan berlatih membuat virtual environment dengan cara bawaan Python, yaitu `venv` dan `pip`. Proyek Django yang sebenarnya akan kita siapkan pada Part 1.

## Apa itu Virtual Environment?
Virtual environment adalah alat yang membantu mengelola dependensi proyek Python secara terpisah. Dengan menggunakan virtual environment, Anda dapat menghindari konflik antara paket yang dibutuhkan oleh proyek yang berbeda.

## Kenapa kita perlu Virtual Environment?
1. **Isolasi Proyek**: Setiap proyek dapat memiliki dependensi yang berbeda tanpa saling mengganggu.
2. **Manajemen Versi**: Memungkinkan penggunaan versi paket yang berbeda untuk proyek yang berbeda.
3. **Kemudahan Distribusi**: Memudahkan distribusi proyek dengan menyertakan file `requirements.txt` yang berisi daftar paket yang dibutuhkan.
4. **Pengujian**: Memudahkan pengujian kode dalam lingkungan yang bersih.
5. **Keamanan**: Mengurangi risiko konflik antara paket yang dapat menyebabkan masalah keamanan.
6. **Konsistensi Lingkungan**: Memastikan bahwa lingkungan pengembangan (dev) dan produksi (prod) memiliki konfigurasi yang sama.
7. **Pengelolaan Dependensi**: Memudahkan pengelolaan dan pembaruan paket tanpa mempengaruhi sistem Python global.
8. **Portabilitas**: Memudahkan pemindahan proyek antar mesin tanpa khawatir tentang dependensi yang hilang atau konflik.
9. **Pengembangan Kolaboratif**: Memudahkan tim pengembang untuk bekerja pada proyek yang sama dengan lingkungan yang konsisten.


## Langkah-langkah Membuat Virtual Environment
Studi Kasus: Membuat virtual environment untuk latihan dan menginstal Django di dalamnya. Kita akan membuat folder latihan bernama `latihan_venv`. Folder ini hanya untuk latihan dan boleh dihapus setelah selesai. Proyek blog kita, `website_django`, akan dibuat dengan cara yang berbeda pada Part 1.
1. **Buka terminal atau command prompt dan buat folder latihan**
   ```bash
   mkdir latihan_venv
   ```
2. **Masuk ke direktori proyek Anda**
   Gunakan perintah `cd` untuk berpindah ke direktori di mana Anda ingin membuat virtual environment.
   ```bash
    cd latihan_venv
    ```
3. **Pastikan Python sudah terinstal**
   ```bash
   python --version
   ```
   akan menampilkan versi Python yang terinstal di sistem Anda. Jika belum terinstal, silakan unduh dan instal dari [situs resmi Python](https://www.python.org/downloads/).
4. **Buat virtual environment dengan paket `venv`**
   Gunakan paket `venv` untuk membuat virtual environment.
   ```bash
   python -m venv .venv
   ```
   Di sini, `-m` adalah opsi/flag di python untuk menjalankan paket/modul sebagai skrip. `venv` adalah modul yang digunakan untuk membuat virtual environment. `.venv` adalah nama folder di mana virtual environment akan dibuat. Penggunaan `.` di awal nama folder adalah konvensi untuk menandakan bahwa folder tersebut adalah folder tersembunyi dan sebagian besar editor modern, termasuk VS Code, mendeteksi folder ini secara otomatis.
5. **Aktifkan virtual environment**
   - Di Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - Di macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
6. **Install paket Django**
    Setelah virtual environment diaktifkan, Anda dapat menginstal paket yang dibutuhkan menggunakan `pip`. Misalnya, untuk menginstal Django, gunakan perintah:
    ```bash
    pip install Django
    ```
7. **Cek paket yang terinstal**
   Untuk melihat daftar paket yang telah diinstal dalam virtual environment, gunakan perintah:
   ```bash
   pip list
   ```
   Di sana tampak paket Django yang baru saja diinstal.
   Untuk memastikan Django telah tersedia dan mengetahui versi Django yang terinstal, gunakan perintah:
   ```bash
    python -m django --version
    ```
    Jika berhasil, perintah tersebut akan menampilkan versi Django yang terinstal, misalnya:
    ```bash
    5.2.6
    ```
8. **Membuat file requirements.txt (opsional)**
   Untuk menyimpan daftar paket yang diinstal dalam virtual environment, Anda dapat membuat file `requirements.txt` dengan perintah:
   ```bash
   pip freeze > requirements.txt
   ```
   File ini dapat digunakan untuk menginstal ulang paket di lingkungan lain dengan perintah:
   ```bash
   pip install -r requirements.txt
   ```
9. **Menonaktifkan virtual environment**
   Setelah selesai bekerja, Anda dapat menonaktifkan virtual environment dengan perintah:
   ```bash
   deactivate
   ```

Dengan mengikuti langkah-langkah di atas, Anda dapat dengan mudah membuat dan mengelola virtual environment untuk proyek Python Anda.

## Selanjutnya: Mengenal uv
Cara `venv` + `pip` di atas sudah berfungsi dengan baik, tetapi ada beberapa hal yang harus kita ingat sendiri: mengaktifkan virtual environment setiap kali membuka terminal, dan memperbarui `requirements.txt` setiap kali menambah paket. Ada alat modern bernama **uv** yang mengurus semua itu secara otomatis dan jauh lebih cepat.

Mulai [Part 1]({% post_url 2025-09-08-django-part1-menyiapkan-proyek-django-dengan-uv %}), kita akan menggunakan uv untuk menyiapkan proyek `website_django` dan menjalankan semua perintah Django di seri tutorial ini.