"""bar_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import handler400, handler403, handler404, handler500

from app import views


# handler400 = 'app.views.bad_request'
# handler403 = 'app.views.permission_denied'
handler404 = 'app.views.page_not_found'
# handler500 = 'app.views.server_error'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^available/', views.available, name="available"),
    url(r'^favorite/', views.favorite, name="favorite"),
    url(r'^special/', views.special, name="special"),
    url(r'^results/', views.search, name="search"),
    url(r'^vote/', views.vote, name="vote"),
    url(r'^page/(?P<page_id>[0-9]+)/$', views.page, name='page'),
]
