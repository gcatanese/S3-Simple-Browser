from s3_simple_browser.s3_mgr import *
from s3_simple_browser.utils import *


def bucket_list():
    print("bucket_list")

    s3 = get_client()

    ret = []

    for bucket in s3.list_buckets()['Buckets']:
        ret.append(Bucket(bucket["Name"], bucket["CreationDate"]))

    return ret


def item_list(bucket_name, prefix=""):
    print(f"item_list bucket_name:{bucket_name} prefix:{prefix}")

    s3 = get_client()

    ret = []

    for item in s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)['Contents']:
        if prefix == get_path(item["Key"]):
            normalized_key = sanitize_key(item["Key"]);
            ret.append(Item(item["Key"], normalized_key, item["LastModified"], item["Size"]))

    return ret


def item_key_list(bucket_name, prefix=""):
    print(f"item_key_list bucket_name:{bucket_name} prefix:{prefix}")

    s3 = get_client()

    ret = []

    for item in s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)['Contents']:
        ret.append(item["Key"])

    return ret


def get_paths(objects):

    ret = [Path(".", ".")]

    for obj in objects:
        s = obj.split("/")
        if len(s) > 1:
            key = '/'.join(s[:len(s) - 1])
            ret.append(Path(key, sanitize_key(key)))

    return ret


def get_path(key):
    s = key.split("/")
    return "/".join(s[:len(s) - 1])


def delete_object(bucket_name, key):
    key = rebuild_key(key)

    s3 = get_client()

    s3.delete_object(Bucket=bucket_name, Key=key);

    print(f"{key} has been deleted")


class Bucket:
    name = ""
    created_date = None

    def __init__(self, name, last_modified):
        self.name = name
        self.last_modified = last_modified


class Path:
    key = ""
    normalized_key = ""

    def __init__(self, key, normalized_key):
        self.key = key
        self.normalized_key = normalized_key


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
