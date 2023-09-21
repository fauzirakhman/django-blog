from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    # print (categories)
    featured_posts = Blog.objects.filter(is_featured=True, status='published').order_by('updated_at').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='published')
    print (posts, 'posts')
    context = {
        # 'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }

    # return HttpResponse('<h2>Homepage</h2>')
    return render(request, 'home.html', context)