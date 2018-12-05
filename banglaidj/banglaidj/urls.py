# banglaidj/urls.py
from django.contrib import admin
from django.urls import path,include
try:
    from blog_posts import views
except:
    from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cost/', include('cost_management.urls'), name='cost'),
    path('blog_posts/', include('blog_posts.urls'), name='blog_posts'),
    path('user/', include('user_info.urls'), name='user')
]
