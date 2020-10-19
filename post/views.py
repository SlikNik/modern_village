from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddPostForm, EditPostForm
from .models import Post
# Create your views here.


class PostView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        return render(request, 'posts.html', {'form': AddPostForm(), 'data': Post.objects.all()})

    def post(self, request):
        form = AddPostForm(request.POST)
        if form.is_valid:
            data = form.data
            Post.objects.create(
                title=data.get('title'),
                body=data.get('body'),
                creator=request.user
            )
            return render(request, 'posts.html', {'form': form, 'data': Post.objects.all()})
        else:
            return render(request, 'posts.html', {'form': form, 'data': Post.objects.all()})


class PostReplyView(LoginRequiredMixin, TemplateView):
    def get(self, request, post_id):
        return render(request, 'postview.html', {'form': AddPostForm(), 'data': Post.objects.get(id=post_id)})

    def post(self, request, post_id):
        form = AddPostForm(request.POST)
        if form.is_valid:
            data = form.data
            Post.objects.create(
                title=data.get('title'),
                body=data.get('body'),
                creator=request.user,
                parent=Post.objects.get(id=post_id)
            )
            return HttpResponseRedirect(reverse('chat'))
        else:
            return HttpResponseRedirect(reverse('chat'))


def post_edit_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('chat'))
    form = EditPostForm(instance=post)
    if request.user == post.creator:
        return render(request, 'generic_form.html', {'form': form})
    return HttpResponseRedirect(reverse('chat'))


def post_delete_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.creator:
        post.delete()
    return HttpResponseRedirect(reverse('chat'))
