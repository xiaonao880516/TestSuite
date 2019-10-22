import hashlib


def md5(src):
    m2 = hashlib.md5()
    m2.update(src.encode("utf8"))
    return m2.hexdigest()


def percentage_2_float(percentage: str):
    if percentage is not None:
        return float(percentage.strip('%'))
    else:
        return 0.0