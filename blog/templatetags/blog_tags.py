from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='totalposts')
def fun ():
    posts = Post.objects.filter(status=0).count()
    return posts

@register.simple_tag(name='posts')
def fun ():
    posts = Post.objects.filter(status=1)
    return posts