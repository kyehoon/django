"""
URL configuration for firstsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import yehoon.views
from django.urls import path
from .views import PhotoListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', yehoon.views.lion, name='lion'),
    path('blog/<int:blog_id>/', yehoon.views.detail, name = "detail"),
    path('newblog/',views.blogpost,name='nowblog'),
    path('photos/', PhotoListView.as_view(), name='photo-list'),
]
