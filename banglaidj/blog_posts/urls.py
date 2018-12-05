
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('all_posts/', views.all_posts, name='all_posts'),
    path('single_post/<post_id>', views.single_post, name='single_post'),

]