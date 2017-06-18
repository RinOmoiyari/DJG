from django.shortcuts import render
from django.utils import timezone
from . import models

# Create your views here.
def post_list(request):
    posts = models.BlogPost.objects.order_by('-published_date').filter(published_date__lte=timezone.now())

    return render(request, 'blog/post_list.html', {'posts':posts})
