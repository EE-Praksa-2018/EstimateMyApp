from . import views
from django.urls import path

app_name = "app"

urlpatterns = [

    # /app/
    path("", views.IndexView.as_view(), name="index"),

    # /app/about/
    path("about/", views.AboutView.as_view(), name="about"),

    # /app/11/
    path("<int:pk>/", views.DetailView.as_view(), name="album_info"),

    # /app/11/favorite/
    #path("<int:album_id>/favorite/", views.favorite, name="favorite"),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()