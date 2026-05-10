from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name ='blog-about'),
    path('sum/', views.sum, name='sum'),
    path('post/<int:post_id>/', views.get_post_detail, name='post-detail'),
    path('category/<str:category_name>/', views.get_post_by_category, name='post-by-category')
]