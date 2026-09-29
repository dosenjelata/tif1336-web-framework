from django.urls import path
from .views import get_blog_posts, post_detail, ContactView, ContactThanksView
urlpatterns = [
    path('', get_blog_posts, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact/thanks/", ContactThanksView.as_view(), name="contact_thanks"),
]
