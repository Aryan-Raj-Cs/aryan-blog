from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your models here.
from taggit.managers import TaggableManager
class post(models.Model):
    STATUS_CHOICE=(("draft","draft"),("published","published"))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date="publish")
    author=models.ForeignKey(User,related_name="blog_post")
    body=models.TextField()
    publish=models.DateField(default=timezone.now)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default="draft")
    tags=TaggableManager()
    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail",args=[self.publish.year,self.publish.strftime("%m"),self.publish.strftime("%d"),self.slug])
    def get(self):
        return reverse("rvs",args=[self.publish.year])
class Comment(models.Model):
    post=models.ForeignKey(post,related_name="comments")
    name=models.CharField(max_length=60)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=("-created",)
    def __str__(self):
        return 'commented by {} on {}'.format(self.name,self.post)

