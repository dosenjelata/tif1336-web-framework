# Django untuk pemula - Part 7. Menampilkan Detail Postingan Blog
Pada bagian sebelumnya, kita telah mempelajari cara menampilkan daftar judul semua postingan blog di halaman web. Pada bagian ini, kita akan mempelajari cara menampilkan detail dari setiap postingan blog ketika pengguna mengklik judul postingan tersebut. 

Kita akan membuat fungsi view untuk mengambil data detail postingan dari database, membuat template HTML untuk menampilkan detail tersebut, dan menghubungkan semuanya melalui routing URL.

## Langkah 1: Membuat Fungsi View untuk Menampilkan Detail Postingan
Buka file `blogs/views.py` dan tambahkan fungsi view untuk menampilkan detail postingan berdasarkan ID postingan. Berikut adalah contoh kode untuk fungsi view tersebut:
```python
from django.shortcuts import render, get_object_or_404
from .models import Post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogs/post_detail.html', {'post': post})
```
Pada kode di atas, kita mengimpor fungsi `get_object_or_404` dari `django.shortcuts` untuk mengambil objek `Post` berdasarkan ID yang diberikan. Jika objek tidak ditemukan, maka akan mengembalikan halaman 404. Fungsi `post_detail` mengambil data postingan berdasarkan `post_id` dan mengirimkannya ke template `post_detail.html` melalui konteks `{'post': post}`.
Langkah selanjutnya adalah membuat template `post_detail.html` untuk menampilkan detail postingan.
## Langkah 2: Membuat Template HTML untuk Menampilkan Detail Postingan
Buat file `post_detail.html` di dalam folder `blogs/templates/blogs/` dan tambahkan kode HTML berikut:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <small>Published on {{ post.created_at }}</small>
    <br>
    <a href="{% url 'blog_list' %}">Back to Blog List</a>
</body>
</html>
```
Pada kode di atas, kita menampilkan judul, konten, dan tanggal pembuatan postingan menggunakan sintaks template Django. Variabel `post` yang kita kirim dari fungsi view digunakan untuk mengakses atribut-atribut dari model `Post`. Kita juga menambahkan link navigasi kembali ke halaman daftar blog di bagian bawah halaman detail.
## Langkah 3: Menambahkan Routing URL untuk Fungsi View Detail Postingan
Buka file `blogs/urls.py` dan tambahkan routing URL untuk fungsi view `post_detail`. Berikut adalah contoh kode untuk menambahkan routing URL:
```python
from django.urls import path
from .views import blog_list, post_detail
urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
]
```
Pada kode di atas, kita menambahkan routing URL baru yang menerima parameter `post_id` sebagai integer. URL ini akan mengarahkan permintaan ke fungsi view `post_detail` yang telah kita buat sebelumnya.
## Langkah 4: Menghubungkan Detail Postingan dari Daftar Blog
Sekarang, kita perlu mengubah template `blog_list.html` agar setiap judul postingan dapat diklik dan mengarahkan pengguna ke halaman detail postingan. Buka file `blog_list.html` dan ubah kode HTML untuk menambahkan tautan pada judul postingan:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Blog List</title>
</head>
<body>
    <h1>Blog List</h1>
    <ul>
        {% for post in blog_posts %}
            <li>
                <h2><a href="{% url 'post_detail' post.id %}">{{ post.title }}</a></h2>
            </li>
        {% empty %}
            <li>No blog posts available.</li>
        {% endfor %}
    </ul>
</body>
</html>
```
Pada kode di atas, kita menambahkan elemen `<a>` di sekitar judul postingan yang menggunakan tag template `{% url 'post_detail' post.id %}` untuk membuat tautan ke halaman detail postingan berdasarkan ID postingan.
## Langkah 5: Menjalankan Server dan Menguji Fitur Detail Postingan
Sekarang, jalankan server Django dengan perintah berikut:
```bash
python manage.py runserver
```
Buka browser dan akses URL `http://127.0.0.1:8000/` untuk melihat daftar postingan blog. Klik pada judul postingan untuk melihat detailnya. Pastikan semua fitur berfungsi dengan baik. Jika Anda mengikuti langkah-langkah di atas dengan benar, Anda sekarang dapat melihat detail dari setiap postingan blog ketika mengklik judulnya.
## Kesimpulan
Pada bagian ini, kita telah mempelajari cara menampilkan detail dari setiap postingan blog di halaman web menggunakan Django. Kita membuat fungsi view untuk mengambil data detail postingan, membuat template HTML untuk menampilkan detail tersebut, dan menghubungkannya melalui routing URL. Dengan memahami konsep ini, Anda dapat membuat aplikasi web yang lebih interaktif dan informatif menggunakan Django.

## Referensi Lanjutan
- [Django Documentation - Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Documentation - URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)