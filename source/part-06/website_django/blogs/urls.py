from django.urls import path
# from .views import home
from .views import get_blog_posts

urlpatterns = [
    # path('', home, name='home'),
    path('', get_blog_posts, name='post_list'),
]
