from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="inici"),
    path("posts/", views.posts, name="posts"),
    path('posts/<int:post_id>/', views.post_detall, name='post_detall'),
    path("autors/", views.autors, name="autors"),
    path('autors/<int:autors_id>/', views.autors_detall, name='autors_detall'),
    path("tags/", views.tags, name="tags"),
    path('tags/<int:tags_id>/', views.tags_posts, name='tags_posts'),
]