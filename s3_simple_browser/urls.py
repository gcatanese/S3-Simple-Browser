from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bucket/<str:bucket_name>', views.bucket, name='bucket'),
    path('container/<str:bucket_name>/view/', views.root, name='container'),
    path('container/<str:bucket_name>/view/<str:object_key>', views.container, name='container'),
    path('container/<str:bucket_name>/delete/<str:object_key>', views.delete, name='message'),
    path('container/<str:bucket_name>/download/<str:object_key>', views.download, name='message'),
]