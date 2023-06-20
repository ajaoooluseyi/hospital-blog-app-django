from django.urls import path

from. import views


urlpatterns = [
    path('create/blog', views.create_blog_post, name='create_post'),
    path('blog/', views.blog_post_list, name='blog'),
    ]