from django.shortcuts import render, reverse, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views import View
from .forms import CommentForm
from .models import Comment, Video
from playlist.models import Playlist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from taggit.models import Tag
from django.db.models import Q


class Index(ListView):
    model = Video
    template_name = 'videos/index.html'
    order_by = '-data_posted'


class UploadVideo(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail', 'tags']
    template_name = 'videos/upload_video.html'

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('video_detail', kwargs={'pk': self.object.pk})


class DetailVideo(View):
    def get(self, request, pk, *args, **kwargs):
        video = Video.objects.get(pk=pk)

        if request.user not in video.views.all():
            if request.user.is_authenticated:
                video.views.add(request.user)

        views_count = video.views.all().count()

        liked_by_user = False
        if request.user in video.likes.all():
            liked_by_user = True

        likes_count = video.likes.all().count()

        comment_form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by('-date_posted')
        comments_count = comments.count()

        saved_by_user = False
        if request.user in video.saved.all():
            saved_by_user = True

        playlists = []
        added_to_playlists = []

        if request.user.is_authenticated:
            playlists = Playlist.objects.filter(user=request.user).order_by('-date_posted')
            added_to_playlists = Playlist.objects.filter(user=request.user).filter(videos=video)

        context = {
            'object': video,
            'views_count': views_count,
            'liked_by_user': liked_by_user,
            'likes_count': likes_count,
            'comments': comments,
            'comments_count': comments_count,
            'comment_form': comment_form,
            'saved_by_user': saved_by_user,
            'playlists': playlists,
            'added_to_playlists': added_to_playlists,
        }

        return render(request, 'videos/video_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        video = Video.objects.get(pk=pk)

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                video=video,
                user=request.user,
                comment=comment_form.cleaned_data['comment']
            )
            comment.save()

        views_count = video.views.all().count()

        liked_by_user = False
        if request.user in video.likes.all():
            liked_by_user = True

        likes_count = video.likes.all().count()

        comment_form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by('-date_posted')
        comments_count = comments.count()

        saved_by_user = False
        if request.user in video.saved.all():
            saved_by_user = True

        playlists = []
        added_to_playlists = []

        if request.user.is_authenticated:
            playlists = Playlist.objects.filter(user=request.user).order_by('-date_posted')
            added_to_playlists = Playlist.objects.filter(user=request.user).filter(videos=video)

        context = {
            'object': video,
            'views_count': views_count,
            'liked_by_user': liked_by_user,
            'likes_count': likes_count,
            'comments': comments,
            'comments_count': comments_count,
            'comment_form': comment_form,
            'saved_by_user': saved_by_user,
            'playlists': playlists,
            'added_to_playlists': added_to_playlists,
        }

        return render(request, 'videos/video_detail.html', context)


class DeleteVideo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    template_name = 'videos/delete_video.html'

    def get_success_url(self):
        video = self.get_object()
        added_to_playlists = Playlist.objects.filter(user=self.request.user)
        for playlist in added_to_playlists:
            playlist.videos.remove(video)
        return reverse('home')

    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader


def index(request):
    return redirect('home')


def add_like(request, pk):
    video = Video.objects.get(pk=pk)
    if request.user in video.likes.all():
        video.likes.remove(request.user)
    else:
        video.likes.add(request.user)
    return redirect('video_detail', pk=pk)


class SearchVideo(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        query_list = Video.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(
            tags__name__icontains=query) | Q(uploader__username__icontains=query)).distinct()
        context = {
            'query_list': query_list,
            'query': query,
        }
        return render(request, 'videos/search_video.html', context)


def save_video(request, pk):
    video = Video.objects.get(pk=pk)
    if request.user in video.saved.all():
        video.saved.remove(request.user)
    else:
        video.saved.add(request.user)
    return redirect('video_detail', pk=pk)


class SavedVideo(View):
    def get(self, request, *args, **kwargs):
        saved_list = Video.objects.filter(saved=request.user)
        context = {
            'saved_list': saved_list,
        }
        return render(request, 'videos/saved_video.html', context)
