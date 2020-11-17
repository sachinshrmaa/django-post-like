
from django.contrib import admin
from django.urls import path

from post.views import post_view, post_like, PostLikeAPIToggle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_view, name="all-post"),
    path('p/<int:pk>/like/', post_like, name="post-like"),
    path('p/<int:pk>/like/api/', PostLikeAPIToggle.as_view(), name="post-like-api"),
]
