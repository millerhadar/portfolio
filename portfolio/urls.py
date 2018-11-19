"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
import jobs.views
import pols.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home,name='home'),
    path('blog/', include('blog.urls')),
    path('pols/', pols.views.IndexView.as_view(), name='pols'),
    path('pols/<int:pk>/', pols.views.DetailView.as_view(), name='detail'),
    path('pols/<int:pk>/results/', pols.views.ResultsView.as_view(), name='results'),
    path('pols/<int:question_id>/vote/', pols.views.vote, name='vote'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
