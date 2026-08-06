from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.

def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1)
    
    if cat_name:
        posts = posts.filter(category__name__iexact = cat_name)
    
    if author_username:
        # when we want to point out to a field in another table that it relates to my element, 
        posts = posts.filter(author__username__iexact = author_username)
        
    context = {'posts':posts}
    
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts , pk=pid)
    context = {'post':post}
    
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    
    # The __iexact lookup is case-insensitive,
    # so it doesn't distinguish between uppercase and lowercase letters.
    posts = posts.filter(category__name__iexact=cat_name)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def test_view(request):
    return render(request, 'test.html')