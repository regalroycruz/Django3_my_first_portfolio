from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog import views

app_name = 'portfolio'


urlpatterns = [
    path('', views.all_blogs, name='all_blogss'),
    path('<int:blog_id>', views.detail, name='detail'),

]