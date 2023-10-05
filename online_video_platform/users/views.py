from django.shortcuts import render, redirect, reverse
from videos.models import Video
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views import View
from .models import Profile

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('signin')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        videos = Video.objects.all().filter(uploader=pk).order_by('-date_posted')

        context = {
            'videos': videos
        }

        return render(request, 'users/profile.html', context)
    
class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['bio', 'description']
    template_name = 'users/update_profile.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})
