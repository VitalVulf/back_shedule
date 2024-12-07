from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from zadach import views
from zadach.views import ListSpecApi, ListGroupApi, ListPrepodApi, ListErrorApi, NewsApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('zadach.urls')),
    path('api/v1/zadach/',ListSpecApi.as_view()),
    path('api/v1/zadach/<int:pk>/', ListSpecApi.as_view()),  # Для получения одной задачи по id
    path('api/v2/zadach/',ListGroupApi.as_view()),
    path('api/v2/zadach/<int:pk>/',ListGroupApi.as_view()),
    path('api/v3/prepodovatel/', ListPrepodApi.as_view()),
    path('api/v3/prepodovatel/<int:pk>/',ListPrepodApi.as_view()),
    path('api/v4/error',ListErrorApi.as_view()),
    path('api/v5/news/', NewsApi.as_view()),
    path('api/v5/news/<int:pk>/', NewsApi.as_view()),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
