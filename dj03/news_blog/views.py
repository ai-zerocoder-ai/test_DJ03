from django.shortcuts import render
from .models import NewsPost

def news_list(request):
    news_posts = NewsPost.objects.all().order_by('-pub_date')
    return render(request, 'news_blog/news.html', {'news_posts': news_posts})
