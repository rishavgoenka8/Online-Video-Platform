from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView
from django.views import View
from .models import Playlist
from videos.models import Video

# Create your views here.
class CreatePlaylist(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['name', 'thumbnail']
    template_name = 'playlist/create_playlist.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class Index(View):
    def get(self, request, *args, **kwargs):
        playlist_list = Playlist.objects.all().filter(user=request.user).order_by('-date_posted')

        context = {
            'playlist_list': playlist_list
        }

        return render(request, 'playlist/index.html', context)
    

class PlaylistVideos(View):
    def get(self, request, pk, *args, **kwargs):
        playlist = Playlist.objects.get(pk=pk)
        videos = playlist.videos.all().order_by('-date_posted')

        context = {
            'playlist': playlist,
            'videos': videos
        }

        return render(request, 'playlist/playlist_videos.html', context)
    

def add_to_playlist(request, pk1, pk2):
    video = Video.objects.get(pk=pk2)
    playlist = Playlist.objects.get(pk=pk1)

    playlist.videos.add(video)

    return redirect('video_detail', pk=pk2)
    

def delete_from_playlist(request, pk1, pk2):
    video = Video.objects.get(pk=pk2)
    playlist = Playlist.objects.get(pk=pk1)

    playlist.videos.remove(video)

    return redirect('video_detail', pk=pk2)
    

class DeletePlaylist(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Playlist
    template_name = 'playlist/delete_playlist.html'

    def get_success_url(self):
        return reverse('all_playlists')

    def test_func(self):
        playlist = self.get_object()
        return self.request.user == playlist.user