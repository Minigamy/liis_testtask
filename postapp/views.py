from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from postapp.forms import PostForm
from postapp.models import Post


def post_list(request):
    if request.user.has_perm('postapp.view_post'):
        posts = Post.objects.all().order_by('published_date')
        return render(request, 'postapp/post_list.html', {'posts': posts})
    else:
        posts = Post.objects.filter(private=False).order_by('published_date')
        return render(request, 'postapp/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.private:
        if request.user.has_perm('postapp.view_post'):
            return render(request, 'postapp/post_detail.html', {'post': post})
        else:
            return render(request, 'postapp/access_denied.html')
    return render(request, 'postapp/post_detail.html', {'post': post})


def post_new(request):
    if request.user.has_perm('postapp.add_post'):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'postapp/post_edit.html', {'form': form})
    else:
        return render(request, 'postapp/access_denied.html')


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.has_perm('postapp.change_post') and request.user.id == post.author_id:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'postapp/post_edit.html', {'form': form})
    else:
        return render(request, 'postapp/access_denied.html')


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.user.has_perm('postapp.change_post') and request.user.id == post.author_id:
        if request.method == "GET":
            post.delete()
            return redirect('home')
    else:
        return render(request, 'postapp/access_denied.html')
