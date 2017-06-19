from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import models

# Create your views here.
def post_list(request):
    posts = models.BlogPost.objects.order_by('-published_date').filter(published_date__lte=timezone.now())

    return render(request, 'blog/post_list.html', {'posts':posts})

def post_details(request, pk):
    #post = models.BlogPost.objects.get(pk=pk)
    post = get_object_or_404(models.BlogPost, pk=pk)
    return render(request, 'blog/post_details.html', {'post':post})

def publish_post(request, pk):
    post = get_object_or_404(models.BlogPost, pk=pk)
    models.BlogPost.publish(post)
    return redirect('post_detail', pk=pk)
