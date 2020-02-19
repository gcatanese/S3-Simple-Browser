
def sanitize_key(key):
    return key.replace("/", "-")


def rebuild_key(key):
    return key.replace("-", "/")
