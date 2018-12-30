from blog.models import post
from django import template
register=template.Library()

@register.simple_tag
def total_posts():
    return post.objects.count()

@register.inclusion_tag("blog/show_latest.html")
def show_latest_post():
    latest_post=post.objects.order_by("-publish")[:3]
    return {"latest_post":latest_post}
from django.db.models import Count
@register.assignment_tag
def get_most_commented_posts(count=3):
   return post.objects.annotate(total_comments=Count("comments")).order_by("-total_comments")[:count]

