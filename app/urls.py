from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = "app"

urlpatterns = [

    # /app/
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.index, name="index"),


    # /app/about/
    path("about/", views.AboutView.as_view(), name="about"),

    # /app/11/
    path("<int:pk>/", views.DetailView.as_view(), name="album_info"),

    # /app/11/favorite/
    #path("<int:album_id>/favorite/", views.favorite, name="favorite"),

    # /app/login/
    # path("login/$", auth_views.login, name='login'),
    path("login/", auth_views.login, {'template_name': 'app/login.html'}, name='login'),

    # /app/logout/
    # path("logout/$", auth_views.logout, name='logout'),
    path("logout/", auth_views.logout, {'template_name': 'app/about.html'}, name='logout'),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()