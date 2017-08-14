"""mysite URL Configuration

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
from polls import views as v

app_name = "polls"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', v.CategoryListView.as_view(), name="main_page"),
    url(r'^CreateCategory/$', v.CategoryCreateView.as_view(), name="CreateCategory"),
    url(r'^CategoryDetails/(?P<pk>\d+)/$', v.CategoryDetailView.as_view(), name="CategoryDetails"),
    url(r'^QuestionCreate/(?P<pk>\d+)/$', v.QuestionCreateView.as_view(), name="QuestionCreate"),
    url(r'^ChoiceList/(?P<pk>\d+)/$', v.ChoiceListView.as_view(), name="ChoiceList"),
    url(r'^ChoiceCreate/$', v.ChoiceCreateView.as_view(), name="ChoiceCreate")



]
