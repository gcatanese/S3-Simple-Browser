from django.urls import path

from . import views
from s3_simple_browser.bucket_mgr import *

urlpatterns = [
    path('', views.index, name='index'),
    path('bucket/<str:bucket_name>', views.bucket, name='bucket'),
    path('container/<str:bucket_name>/view/', views.root, name='container'),
    path('container/<str:bucket_name>/view/<str:object_key>', views.container, name='container'),
    path('container/<str:bucket_name>/delete/<str:object_key>', views.delete, name='message'),
    path('container/<str:bucket_name>/download/<str:object_key>', views.download, name='message'),
    path('container/<str:bucket_name>/upload/<str:folder>', views.upload, name='message'),
]


# create 'data-bucket' if no Bucket is found
def on_startup():
    print("on_startup")

    if len(bucket_list()) == 0:
        create_bucket("data-bucket")


on_startup()
