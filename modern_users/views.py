from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import ModernUsers

from notices.models import Notice

from post.models import Post


@login_required
def index(request):
    user = ModernUsers.objects.get(id=user_id)
    post = Post.objects.filter(posted_by=request.creator)
    local_posts = Post.object.creator.filter(locals=request.creator.zipcode).objects.filter(posted_by__in=request.user.following.all())
    notice = Notice.object.TypeOf()

    return render(request, 'profile.html',
        {
            "notice": notice,
            "posts": post,
            "local_post": local_posts,
        
        })


def create_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = ModernUsers.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse('homepage'))
    form = SignUpForm()
    return render(request, 'generic_form.html', {'form': form})


def user_profile(request, user_id):
    profile = ModernUsers.objects.get(id=user_id)
    posts = Post.objects.filter(posted_by=profile)
    notifications = request.Notice.all()
    return render(request, "user_profile.html",
        {
            "profile": profile,
            "posts": posts,
            "notification": notifications
        }
    )
