import hashlib


def md5(src):
    m2 = hashlib.md5()
    m2.update(src.encode("utf8"))
    return m2.hexdigest()