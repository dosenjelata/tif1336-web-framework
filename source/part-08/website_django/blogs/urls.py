from django.urls import path
from .views import get_blog_posts, post_detail
urlpatterns = [
    path('', get_blog_posts, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
]
