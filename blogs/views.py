from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category

# Create your views here.

def posts_by_category(requests, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='published', category=category_id)
    # Use try/except when we want to do some custom action if the category does not exist
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    
    # Use get_object_or_404 when you want to show 404 error page
    category = get_object_or_404(Category, pk=category_id)
    
    # return HttpResponse(posts)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(requests, 'posts_by_category.html', context)