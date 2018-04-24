"""from django.shortcuts import render, get_object_or_404
from . models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    return render(request, "app/index.html", {"all_albums": all_albums})


def about(request):
    return render(request, "app/about.html")


def album_info(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, "app/album_info.html", {"album": album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST["song"])
    except (KeyError, Song.DoesNotExist):
        return render(request, "app/album_info.html", {
            "album": album,
            "error_message": "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, "app/album_info.html", {"album": album})"""

from django.views import generic

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Album, Song
from . serializers import AlbumSerializer

class AlbumList(APIView):

    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)


class IndexView(generic.ListView):
    template_name = "app/index.html"

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = "app/album_info.html"

class AboutView(generic.TemplateView):
    template_name = "app/about.html"