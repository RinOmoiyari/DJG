from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import models, forms

# Create your views here.
def post_list(request):
    subheader = 'Recent Posts'
    posts = models.BlogPost.objects.order_by('-published_date').filter(published_date__lte=timezone.now())

    return render(request, 'blog/post_list.html', {'posts':posts, 'subheader':subheader})

def post_unpublished(request):
    subheader = 'Unpublished Posts'
    posts = models.BlogPost.objects.filter(published_date__isnull=True)

    return render(request, 'blog/post_list.html', {'posts':posts, 'subheader':subheader})

def post_details(request, pk):
    #post = models.BlogPost.objects.get(pk=pk)
    post = get_object_or_404(models.BlogPost, pk=pk)
    return render(request, 'blog/post_details.html', {'post':post})

def post_publish(request, pk):
    post = get_object_or_404(models.BlogPost, pk=pk)
    models.BlogPost.publish(post)
    return redirect('post_detail', pk=pk)

def post_new(request):
    subheader = 'Create a New Post'
    if request.method == "POST":
        form = forms.PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()


            return redirect('post_detail', pk=post.pk)

    else:
        form = forms.PostForm()
        return render(request, 'blog/post_edit.html', {'form':form, 'subheader':subheader})

def post_edit(request, pk):
    post = get_object_or_404(models.BlogPost, pk=pk)
    subheader = 'Edit Post '
    if request.method == "POST":
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()


            return redirect('post_detail', pk=post.pk)

    else:
        form = forms.PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form':form, 'subheader':subheader})
