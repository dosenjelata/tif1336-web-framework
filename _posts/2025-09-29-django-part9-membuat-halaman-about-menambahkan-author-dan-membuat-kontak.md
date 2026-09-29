---
layout: post
title: "Django untuk pemula - Part 9. Menambahkan Author, Membuat Halaman About dan Halaman Contact"
date: 2025-09-29 07:02:00 +0700
categories: [Django, Blog App, Python]
tags: [Django, Blog App, Python]
---
{% raw %}

Pada bagian sebelumnya, kita telah berhasil membuat website blog sederhana menggunakan Django. Website ini sangat sederhana, tetapi berfungsi dengan baik dan memiliki tampilan yang rapi berkat penggunaan Bootstrap. Beberapa best practices juga telah kita terapkan, seperti penggunaan base template untuk menghindari duplikasi kode.


Sebagai bagian dari **Continuous Improvement**, pada tutorial ini, kita akan memperbaiki beberapa aspek dari aplikasi blog kita untuk meningkatkan fungsionalitas dan tampilan.

Daftar perbaikan yang akan kita lakukan:
1. Menambahkan halaman About.
2. Menambahkan field `author` pada model `Post`.
3. Menambahkan halaman Contact.
   1. Membuat model `ContactMessage` untuk menyimpan pesan dari halaman Contact.
   2. Membuat form untuk halaman Contact.
   3. Menampilkan pesan error (validasi) pada form Contact.
   4. Membuat class-based view untuk menangani form Contact.
   5. Menambahkan admin interface untuk model `ContactMessage`.

## Langkah 1: Menambahkan Halaman About
Kita akan menambahkan halaman About yang berisi informasi tentang blog kita. Pertama, buat file `about.html` di dalam folder project `templates`, yaitu `templates/about.html`. Isi file tersebut dengan konten berikut:
```html
{% extends "base.html" %}
{% block title %}About - MyBlog{% endblock %}

{% block content %}
<div class="py-4">
  <h1 class="mb-3">About</h1>
  <p class="text-muted">
    MyBlog is a simple project built with Django and Bootstrap.
  </p>
</div>
{% endblock %}
```
Selanjutnya, tambahkan URL untuk halaman About di file `website_django/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls')),
    path('about/', views.about, name='about'),  # Menambahkan URL untuk halaman About
]
```
Jangan lupa untuk menambahkan fungsi `about` di file `website_django/views.py`, tepat di bawah fungsi `home` yang sudah ada dari Part 8:
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
```
Paling terakhir, update href di navbar bagian About yang ada di file `templates/partials/_header.html` yang sebelumnya masih mengarah ke `#` menjadi seperti berikut:
```html
<a href="{% url 'about' %}" class="text-decoration-none">About</a>
```

## Langkah 2: Menambahkan Field Author pada Model Post
Buka file `models.py` di dalam aplikasi `blogs` dan tambahkan field `author` pada model `Post`. Jangan lupa menambahkan baris import `User` di bagian paling atas.
```python
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Menambahkan field author
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
```
`ForeignKey` membuat relasi antara dua tabel: setiap postingan dimiliki oleh satu user (penulis), dan satu user bisa memiliki banyak postingan. Model `User` adalah model bawaan Django, yaitu user yang sama dengan akun superuser yang kita buat di Part 4. Opsi `on_delete=models.CASCADE` berarti jika seorang user dihapus, semua postingannya juga ikut terhapus.

Setelah menambahkan field `author`, kita perlu membuat dan menjalankan migrasi untuk memperbarui database:
```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```
Apabila ketika menjalankan migrasi muncul pertanyaan berikut:
```bash
It is impossible to add a non-nullable field 
'author' to post without specifying a default. 
This is because the database needs something to 
populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 
```

Pertanyaan ini muncul karena database kita sudah berisi beberapa postingan, sedangkan field `author` wajib diisi. Django perlu tahu siapa author untuk postingan-postingan lama tersebut. Kita bisa menetapkan user admin sebagai author untuk semua postingan lama:
1. Ketik `1` lalu tekan Enter untuk memilih opsi "Provide a one-off default now".
2. Django akan meminta nilai default. Ketik ID user admin, biasanya `1` (superuser pertama yang kita buat di Part 4), lalu tekan Enter.
3. Setelah file migrasi berhasil dibuat, jalankan `uv run python manage.py migrate`.

Alternatif lainnya agar tidak muncul pertanyaan ketika migrasi adalah dengan cara:
1. Menuliskan default user ke dalam field `author`.
```python
author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Ganti 1 dengan ID user admin Anda jika berbeda
```
2. Mengijinkan field `author` untuk menerima nilai `null` dan `blank` sementara waktu:
```python
author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
```
Tetapi, cara kedua ini tidak direkomendasikan karena field `author` seharusnya wajib diisi. Jika Anda menggunakan cara ini, pastikan semua postingan memiliki author dengan cara mengupdate data di database setelah migrasi selesai, misalnya melalui Django Admin.

## Langkah 3: Memperbarui Tampilan Post Detail
Buka file `blogs/templates/blogs/post_detail.html` dan perbarui tampilannya untuk menampilkan informasi author. Ubah isinya menjadi seperti berikut:
```html
{% extends "base.html" %}
{% block title %}{{ post.title }} - MyBlog{% endblock %}

{% block content %}
<article class="py-3">
  <h1 class="h2 mb-2">{{ post.title }}</h1>
  <p class="text-muted small mb-3">
    By <strong>{{ post.author.get_full_name|default:post.author.username }}</strong>
    — {{ post.published_date|date:"F j, Y, g:i a" }}
  </p>
  <hr>
  <div class="mt-3">
    {{ post.content|linebreaks }}
  </div>
</article>

<a href="{% url 'post_list' %}" class="btn btn-outline-secondary mt-4">← Back to Blog</a>
{% endblock %}
```
Karena `author` adalah relasi ke model `User`, kita bisa mengakses data user melalui `post.author`. Filter `default` pada `{{ post.author.get_full_name|default:post.author.username }}` berarti: tampilkan nama lengkap author, tetapi jika nama lengkapnya kosong, tampilkan username-nya.

## Langkah 4: Menambahkan Halaman Contact
Buat model baru untuk menyimpan pesan dari halaman Contact. Buka file `models.py` di dalam aplikasi `blogs` dan tambahkan model `ContactMessage` di bawah model `Post` (baris import di atas tidak perlu ditulis ulang):
```python
class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.subject or 'No subject'}"
```
Beberapa hal baru pada model ini:
- `EmailField` adalah field teks yang otomatis memeriksa apakah isinya berformat email yang valid.
- `blank=True` pada `subject` berarti field ini boleh dikosongkan saat mengisi form.
- `auto_now_add=True` pada `created_at` berarti tanggal dan waktu diisi otomatis saat pesan pertama kali disimpan.
- `class Meta` dengan `ordering = ['-created_at']` mengurutkan pesan dari yang terbaru (tanda `-` berarti urutan menurun).

Setelah menambahkan model `ContactMessage`, buat dan jalankan migrasi:
```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

Setelah model dibuat, kita akan membuat form untuk halaman Contact. Buat file baru bernama `forms.py` di dalam aplikasi `blogs` dan tambahkan kode berikut:
```python
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@example.com"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Optional"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "How can we help?"}),
        }
```
`ModelForm` adalah form yang dibuat otomatis berdasarkan model. Kita cukup menyebutkan model dan field yang ingin ditampilkan, dan Django akan membuat input form beserta validasinya (misalnya `name` dan `message` wajib diisi, `email` harus berformat email). Bagian `widgets` digunakan untuk menambahkan class Bootstrap `form-control` dan teks placeholder pada setiap input.

Selanjutnya, buat view untuk menangani form Contact. Buka file `blogs/views.py`, tambahkan baris-baris import berikut di bagian atas file, lalu tambahkan kedua class di bagian bawah file (fungsi `get_blog_posts` dan `post_detail` tetap ada):
```python
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import ContactForm
from .models import ContactMessage


class ContactView(CreateView):
    template_name = "blogs/contact.html"
    form_class = ContactForm
    model = ContactMessage
    success_url = reverse_lazy("contact_thanks")

class ContactThanksView(TemplateView):
    template_name = "blogs/contact_thanks.html"
```
Berbeda dengan view sebelumnya yang berupa fungsi, kali ini kita menggunakan **class-based view**, yaitu view berbentuk class yang sudah disediakan Django untuk pekerjaan yang umum:
- `CreateView` menangani form untuk membuat data baru. Ketika halaman dibuka, form kosong ditampilkan. Ketika form dikirim, Django memvalidasi isinya. Jika valid, data disimpan ke database dan pengguna diarahkan ke `success_url`. Jika tidak valid, form ditampilkan lagi beserta pesan error-nya.
- `TemplateView` hanya menampilkan sebuah template tanpa logika tambahan, cocok untuk halaman terima kasih.
- `reverse_lazy("contact_thanks")` membuat URL berdasarkan nama routing, sama seperti tag `{% url %}` di template.

Selanjutnya, buat file `contact.html` di dalam folder `blogs/templates/blogs/`, sehingga lokasinya menjadi `blogs/templates/blogs/contact.html`, dan tambahkan kode berikut:
```html
{% extends "base.html" %}
{% block title %}Contact - MyBlog{% endblock %}

{% block content %}
<div class="py-4">
  <h1 class="mb-3">Contact</h1>
  <p class="text-muted">Send us a message. We’ll get back to you soon.</p>

  <form method="post" class="mt-3">
    {% csrf_token %}
    <div class="mb-3">
      <label class="form-label">Name</label>
      {{ form.name }}
      {% if form.name.errors %}<div class="text-danger small">{{ form.name.errors|striptags }}</div>{% endif %}
    </div>

    <div class="mb-3">
      <label class="form-label">Email</label>
      {{ form.email }}
      {% if form.email.errors %}<div class="text-danger small">{{ form.email.errors|striptags }}</div>{% endif %}
    </div>

    <div class="mb-3">
      <label class="form-label">Subject</label>
      {{ form.subject }}
      {% if form.subject.errors %}<div class="text-danger small">{{ form.subject.errors|striptags }}</div>{% endif %}
    </div>

    <div class="mb-3">
      <label class="form-label">Message</label>
      {{ form.message }}
      {% if form.message.errors %}<div class="text-danger small">{{ form.message.errors|striptags }}</div>{% endif %}
    </div>

    <button type="submit" class="btn btn-primary">Send</button>
  </form>
</div>
{% endblock %}
```
Beberapa hal penting pada template ini:
- `method="post"` berarti data form dikirim dengan metode HTTP POST, yang digunakan untuk mengirim data ke server.
- `{% csrf_token %}` wajib ada di setiap form POST. Tag ini menambahkan token keamanan untuk mencegah serangan CSRF (*Cross-Site Request Forgery*). Tanpa tag ini, Django akan menolak form dengan error 403.
- `{{ form.name }}` menampilkan input untuk field `name`, dan `{{ form.name.errors }}` menampilkan pesan error jika isian field tersebut tidak valid. Coba kirim form dengan email yang salah format untuk melihat pesan error-nya.

Terakhir, buat file `contact_thanks.html` di folder yang sama, yaitu `blogs/templates/blogs/contact_thanks.html`, dan tambahkan kode berikut:
```html
{% extends "base.html" %}
{% block title %}Thanks - MyBlog{% endblock %}

{% block content %}
<div class="py-5 text-center">
  <h1 class="fw-bold">Thank you!</h1>
  <p class="text-muted">Your message has been received.</p>
  <a href="{% url 'home' %}" class="btn btn-outline-secondary mt-3">Back to Home</a>
</div>
{% endblock %}
```
Selanjutnya, tambahkan URL untuk halaman Contact di file `blogs/urls.py`:
```python
from django.urls import path
from .views import get_blog_posts, post_detail, ContactView, ContactThanksView
urlpatterns = [
    path('', get_blog_posts, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact/thanks/", ContactThanksView.as_view(), name="contact_thanks"),
]
```
Jangan lupa untuk mengupdate href di navbar bagian Contact yang ada di file `templates/partials/_header.html` yang sebelumnya masih mengarah ke # menjadi seperti berikut:
```html
<a href="{% url 'contact' %}" class="text-decoration-none">Contact</a>
```
## Langkah 5: Menambahkan Admin Interface untuk Model ContactMessage
Buka file `admin.py` di dalam aplikasi `blogs` dan tambahkan model `ContactMessage` ke admin interface. Perhatikan bahwa model `Post` dari Part 4 tetap didaftarkan, jadi isi lengkap file `admin.py` menjadi seperti berikut:
```python
from django.contrib import admin
from .models import Post, ContactMessage

admin.site.register(Post)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    list_filter = ("created_at",)
```
Di sini kita menggunakan cara yang lebih lengkap dibanding `admin.site.register(Post)`. Decorator `@admin.register(ContactMessage)` mendaftarkan model sekaligus pengaturan tampilannya di class `ContactMessageAdmin`:
- `list_display` menentukan kolom yang ditampilkan pada daftar pesan.
- `search_fields` menambahkan kotak pencarian berdasarkan field tersebut.
- `readonly_fields` membuat `created_at` hanya bisa dibaca, tidak bisa diubah.
- `ordering` mengurutkan pesan dari yang terbaru.
- `list_filter` menambahkan filter berdasarkan tanggal di sisi kanan halaman.

Sekarang, jalankan server Django dan pergi ke halaman Contact untuk menguji form Contact. Isi form dan kirimkan. Anda akan diarahkan ke halaman terima kasih. Pesan yang dikirim akan disimpan di database. Setelah itu, buka halaman admin untuk melihat model `ContactMessage` di admin interface.
{% endraw %}
## Melihat Hasilnya
Sekarang, kita dapat melihat hasil perbaikan aplikasi blog kita dengan mengunjungi beberapa URL berikut:
### Halaman Home: `http://localhost:8000/` 
![Home Page]({{ '/assets/images/08-home.png' | relative_url }})
### Halaman About: `http://localhost:8000/about/`
![About Page]({{ '/assets/images/09-about.png' | relative_url }})
### Halaman Blog: `http://localhost:8000/blogs/`
![Blog Page]({{ '/assets/images/08-blogs.png' | relative_url }})
### Halaman Detail Post: `http://localhost:8000/blogs/<post_id>/` (ganti `<post_id>` dengan ID post yang ada)
![Post Detail Page]({{ '/assets/images/08-post-detail.png' | relative_url }})
### Halaman Contact: `http://localhost:8000/blogs/contact/`
![Contact Page]({{ '/assets/images/09-contact.png' | relative_url }})
### Halaman Terima Kasih Contact: `http://localhost:8000/blogs/contact/thanks/`
![Contact Thanks Page]({{ '/assets/images/09-thankyou.png' | relative_url }})
### Halaman Admin: `http://localhost:8000/admin/`
![Admin Page]({{ '/assets/images/09-admin.png' | relative_url }})
![Admin Page Contact Message]({{ '/assets/images/09-admin-messages.png' | relative_url }})

## Kesimpulan
Dengan langkah-langkah di atas, kita telah berhasil memperbaiki aplikasi blog kita dengan menambahkan halaman About, menambahkan field `author` pada model `Post`, serta menambahkan halaman Contact lengkap dengan form dan penyimpanan pesan ke database. Selain itu, kita juga menambahkan admin interface untuk model `ContactMessage` agar kita dapat mengelola pesan yang masuk melalui halaman admin Django.

Beberapa konsep baru yang kita pelajari pada bagian ini:
- **Relasi antar model** dengan `ForeignKey`, yang menghubungkan setiap postingan dengan penulisnya.
- **Migrasi pada tabel yang sudah berisi data**, termasuk cara memberikan nilai default untuk field baru.
- **ModelForm**, yaitu form yang dibuat otomatis dari model beserta validasinya.
- **Class-based view** (`CreateView` dan `TemplateView`) sebagai alternatif dari view berbentuk fungsi.
- **CSRF token** untuk mengamankan form yang dikirim dengan metode POST.
- **Kustomisasi halaman admin** dengan `ModelAdmin`.

## Referensi Lanjutan
1. Field `ForeignKey` dan opsi `on_delete`: https://docs.djangoproject.com/en/6.1/ref/models/fields/#foreignkey
2. Membuat form dari model (ModelForm): https://docs.djangoproject.com/en/6.1/topics/forms/modelforms/
3. Class-based view untuk form (`CreateView`): https://docs.djangoproject.com/en/6.1/ref/class-based-views/generic-editing/
4. `TemplateView` dan class-based view dasar: https://docs.djangoproject.com/en/6.1/ref/class-based-views/base/
5. Perlindungan CSRF di Django: https://docs.djangoproject.com/en/6.1/howto/csrf/
6. Kustomisasi halaman admin (`ModelAdmin`): https://docs.djangoproject.com/en/6.1/ref/contrib/admin/

