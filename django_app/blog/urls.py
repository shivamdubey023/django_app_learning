from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name ='blog-about'),
    path('sum/', views.sum, name='sum'),
    path('post/<int:post_id>/', views.get_post_detail, name='post-detail'),
    path('category/<str:category_name>/', views.get_post_by_category, name='post-by-category'),
    path('article/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.article_detail, name='article-detail'),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.article_year, name='article-year')
]