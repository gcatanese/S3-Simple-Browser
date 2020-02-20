from django.shortcuts import render

from s3_simple_browser.bucket_mgr import *
from s3_simple_browser.utils import *
from s3_simple_browser.s3_mgr import *

from django.http import HttpResponse
from django.template import loader


def index(request):
    print(request)

    template = loader.get_template('s3_simple_browser/index.html')
    context = {
        'bucket_list': bucket_list(),
    }
    return HttpResponse(template.render(context, request))


def bucket(request, bucket_name):
    print(bucket_name)

    list = get_paths(item_key_list(bucket_name))

    template = loader.get_template('s3_simple_browser/bucket.html')
    context = {
        'list': list,
        'bucket_name': bucket_name
    }
    return HttpResponse(template.render(context, request))


def root(request, bucket_name):

    list = item_list(bucket_name)

    template = loader.get_template('s3_simple_browser/container.html')
    context = {
        'list': list,
        'object_key': 'Root'
    }
    return HttpResponse(template.render(context, request))


def container(request, bucket_name, object_key):

    object_key = rebuild_key(object_key)

    list = item_list(bucket_name, object_key)

    template = loader.get_template('s3_simple_browser/container.html')
    context = {
        'list': list,
        'bucket_name': bucket_name,
        'object_key': object_key
    }
    return HttpResponse(template.render(context, request))


def delete(request, bucket_name, object_key):

    object_key = rebuild_key(object_key)

    delete_object(bucket_name, object_key)

    template = loader.get_template('s3_simple_browser/message.html')
    context = {
        'message': object_key + 'has been deleted'
    }
    return HttpResponse(template.render(context, request))


def download(request, bucket_name, object_key):

    object_key = rebuild_key(object_key)

    filename = download_object(bucket_name, object_key, get_download_folder())

    template = loader.get_template('s3_simple_browser/message.html')
    context = {
        'message': 'Object ' + object_key + ' has been download to ' + filename
    }
    return HttpResponse(template.render(context, request))


def upload(request, bucket_name, object_key):

    object_key = rebuild_key(object_key)

    filename = upload_object(bucket_name, object_key, "/tmp/file.txt")

    template = loader.get_template('s3_simple_browser/message.html')
    context = {
        'message': 'File ' + object_key + ' has been download to ' + filename
    }
    return HttpResponse(template.render(context, request))




