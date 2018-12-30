"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', views.about),
    url(r'^$', views.post_list_view),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list_view,name="post_list_by_tag_name"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<pst>[-\w]+)/$',
        views.post_detail_view,name="post_detail"),
#url(r'^(\d{4})/(\d{2})/(\d{2})/([-\w]+)/$', views.post_detail_view,name="post_detail"),
    url(r'^(?P<id>\d+)/share/$', views.mail_send_view),
    url(r'^test/(?P<tag_slug>[-\w]+)/$', views.tag),
    url(r'^hello/', views.some_view),
    url(r'^download/', views.download),
    url(r'^check/', views.index_check),
    url(r'^check1/', views.post_list_view),
    url(r'^hk/(\d{2})',views.index_check ,name="rvs"),
    url(r'^comment',views.counts)
]
