from s3_simple_browser.s3_mgr import *
from s3_simple_browser.utils import *


def bucket_list():

    s3 = get_client()

    ret = []

    list = s3.list_buckets()['Buckets']
    for bucket in list:
        ret.append(Bucket(bucket["Name"], bucket["CreationDate"]))

    print(f"Found {len(list)} bucket(s)")

    return ret


def item_list(bucket_name, prefix=""):
    print(f"item_list bucket_name:{bucket_name} prefix:{prefix}")

    s3 = get_client()

    ret = []

    items = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    if items["KeyCount"] > 0:
        for item in items['Contents']:
            if prefix == get_path(item["Key"]):
                normalized_key = sanitize_key(item["Key"]);
                ret.append(Item(item["Key"], normalized_key, item["LastModified"], item["Size"]))

    return ret


def item_key_list(bucket_name, prefix=""):
    print(f"item_key_list bucket_name:{bucket_name} prefix:{prefix}")

    s3 = get_client()

    ret = []

    items = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    if items["KeyCount"] > 0:
        for item in items['Contents']:
            ret.append(item["Key"])

    return ret


def delete_object(bucket_name, key):
    key = rebuild_key(key)

    s3 = get_client()

    s3.delete_object(Bucket=bucket_name, Key=key);

    print(f"{key} has been deleted")


def download_object(bucket_name, key, dest_folder):
    key = rebuild_key(key)

    print(f"dest_folder {dest_folder}")

    s3 = get_client()

    filename = dest_folder + "/" + get_filename(key)
    print(filename)

    s3.download_file(Bucket=bucket_name, Key=key, Filename=filename)

    print(f"Object {key} has been downloaded to " + filename)

    return filename


def upload_object(bucket_name, key, filename):
    key = rebuild_key(key)

    print(key)

    s3 = get_client()

    s3.upload_file(Bucket=bucket_name, Key=key, Filename=filename)

    print(f"File {filename} has been uploaded to " + key)

    return key


class Bucket:
    name = ""
    created_date = None

    def __init__(self, name, last_modified):
        self.name = name
        self.last_modified = last_modified


class Item:
    key = ""
    normalized_key = ""
    last_modified = None
    size = None

    def __init__(self, key, normalized_key, last_modified, size):
        self.key = key
        self.normalized_key = normalized_key
        self.last_modified = last_modified
        self.size = size
