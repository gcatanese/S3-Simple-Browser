def sanitize_key(key):
    return key.replace("/", "-")


def rebuild_key(key):
    return key.replace("-", "/")


def get_path(key):
    s = key.split("/")
    return "/".join(s[:len(s) - 1])


def get_filename(key):
    s = key.split("/")
    return s[len(s) - 1]


def get_paths(objects):
    ret = [Path(".", ".")]

    for obj in objects:
        s = obj.split("/")
        if len(s) > 1:
            key = '/'.join(s[:len(s) - 1])
            ret.append(Path(key, sanitize_key(key)))

    return ret


class Path:
    key = ""
    normalized_key = ""

    def __init__(self, key, normalized_key):
        self.key = key
        self.normalized_key = normalized_key
