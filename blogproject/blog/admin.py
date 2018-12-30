from django.contrib import admin
from blog.models import post

# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display = ["title","slug","author","body","publish","created","update","status"]
    prepopulated_fields = {'slug':('title',)}
    list_filter = ("status","author","created","publish")
    search_fields = ("titles","body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
from blog.models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name","email","post","body","created","updated","active"]
    #raw_id_fields = ("post",)
admin.site.register(post,postAdmin)
admin.site.register(Comment,CommentAdmin)

