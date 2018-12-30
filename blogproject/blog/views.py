from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
import csv
import os
from blog.models import post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def post_list_view(request,tag_slug=None):
    post_list=post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list ,2)
    page_number=request.GET.get("page")
    try:
        post_list=paginator.page(page_number)

    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)

    #return render(request,'blog/post_list.html', {"post_list":post_list,"tag":tag})
    return render(request, 'blog/post_list_check.html', {"post_list": post_list, "tag": tag})
from blog.form import CommentForm
def post_detail_view(request,month,year,day,pst):
    pst=get_object_or_404(post,slug=pst,
                          status="draft",
                          publish__year=year,
                          publish__month=month,
                          publish__day=day
                          )
    comments=pst.comments.filter(active=True)
    csubmit=False
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.post=pst
            new_form.save()
            csubmit=True
    else:
       form=CommentForm()

    #return render(request,"blog/post_detail.html",{"post":pst,"form":form,"csubmit":csubmit,"comments":comments})
    return render(request,"blog/post_detail_check.html",{"post":pst,"form":form,"csubmit":csubmit,"comments":comments})

from django.core.mail import send_mail
from blog.form import EmailSendForm

def mail_send_view(request,id):
    pst = get_object_or_404(post, id=id, status="draft")
    sent=False
    if request.method=="POST":
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            url=request.build_absolute_uri(pst.get_absolute_url())
            message="read post\n {} \n \n{} coment's \n{}".format(url,cd["name"],cd["comment"])
            send_mail("subject",message,"from Blog",[cd["to"]])
            sent=True


    form=EmailSendForm()
    return render(request,"blog/sharebymail.html",{"form":form,"post":pst,"sent":sent})

def tag(request,tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    print(type(tag))
    return render(request,"blog/test.html",{"tag":tag})

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response,delimiter=",")
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response


def download(request):
    #file_name = #get the filename of desired excel file
    #path_to_file = #get the path of desired excel file

    with open("static/upload/aryan.jpg","rb") as file:
       send= file.read()
    response = HttpResponse(send,content_type='image/jpeg')
    response['Content-Disposition'] = 'attachment; filename=' + "static/upload/aryan.jpg"

    #response['X-Sendfile'] = smart_str(path_to_file)
    return response
def index_check(request):
    return render(request,"blog/about.html")
def about(request):
    return render(request,"blog/about.html")

def counts(request):
    obj=post.objects.all()
    v=Comment.objects.filter(post_id=obj[1].id)
    """ for ob in obj:
    v=ob.comments.all()

    print(v)
 circuits = Circuits.objects.filter(site_data__id=1)
 for cm in circuits:
     maintenances = cm.maintenance.all()
     for maintenance in maintenances:
         print(maintenance)"""
    return render(request, "blog/about.html",{"v":v})