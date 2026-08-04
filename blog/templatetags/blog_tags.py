from django import template
from blog.models import Post

register = template.Library()

#  ---Tests fun---
@register.simple_tag(name='totalposts')
def fun ():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def fun ():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + '...'

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('published_date')
    return {'posts': posts}


# ---Main fun---
@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(arg = 3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}