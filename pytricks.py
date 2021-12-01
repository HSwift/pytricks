import platform
import logging
import functools


def toBytes(func):
    @functools.wraps(func)
    def wrapper(x):
        if type(x) == str:
            x = x.encode()
        return func(x)
    return wrapper

def toStr(func):
    @functools.wraps(func)
    def wrapper(x):
        if type(x) == bytes:
            x = x.decode()
        return func(x)
    return wrapper


if platform.python_implementation() == "CPython":
    import forbiddenfruit
    import binascii
    import base64
    import re
    import hashlib
    import datetime
    import time
    import urllib.parse
    import struct

    def _str(x, encoding='utf-8'):
        return x.decode(encoding)

    def _bytes(x, encoding='utf-8'):
        return x.encode(encoding)

    @toBytes
    def _hex(x):
        return binascii.b2a_hex(x)

    @toBytes
    def _unhex(x):
        return binascii.a2b_hex(x)

    @toBytes
    def _base64(x):
        return base64.b64encode(x)

    @toBytes
    def _unbase64(x):
        return base64.b64decode(x)

    def _findall(x, pattern):
        return re.findall(pattern, x)

    def _match(x, pattern):
        return re.match(pattern, x)

    @toBytes
    def _md5(x):
        return hashlib.md5(x).hexdigest()

    @toBytes
    def _sha1(x):
        return hashlib.sha1(x).hexdigest()

    @toBytes
    def _sha256(x):
        return hashlib.sha256(x).hexdigest()

    @property
    def _len(x):
        return len(x)

    def _xor(x, y):
        if type(x) != bytes:
            raise TypeError
        return bytes(a ^ b for a, b in zip(x, y))

    def _map(x, callback):
        return list(map(callback, x))

    def _filter(x, callback):
        return list(filter(callback, x))

    def _reduce(x, callback):
        return functools.reduce(callback, x)

    def _join(x, separator=''):
        return separator.join(x)

    def _date(x, format='%Y-%m-%d %H:%M:%S'):
        time_struct = datetime.datetime.fromtimestamp(x)
        return time_struct.strftime(format)

    def _time(x, format='%Y-%m-%d %H:%M:%S'):
        time_struct = time.strptime(x, format)
        return int(time.mktime(time_struct))

    def _nop(x):
        return x

    @toBytes
    def _urlencode(x):
        return urllib.parse.quote_plus(x)

    def _urldecode(x):
        return urllib.parse.unquote_plus(x)

    def _unpack(x, format):
        return struct.unpack(format, x)


    forbiddenfruit.curse(bytes, "str", _str)
    forbiddenfruit.curse(bytes, "bytes", _nop)
    forbiddenfruit.curse(str, "bytes", _bytes)
    forbiddenfruit.curse(str, "str", _nop)

    forbiddenfruit.curse(str, "hex", _hex)
    forbiddenfruit.curse(str, "unhex", _unhex)
    forbiddenfruit.curse(bytes, "hex", _hex)
    forbiddenfruit.curse(bytes, "unhex", _unhex)

    forbiddenfruit.curse(str, "base64", _base64)
    forbiddenfruit.curse(str, "unbase64", _unbase64)
    forbiddenfruit.curse(bytes, "base64", _base64)
    forbiddenfruit.curse(bytes, "unbase64", _unbase64)

    forbiddenfruit.curse(str, "urlencode", _urlencode)
    forbiddenfruit.curse(str, "urldecode", _urldecode)
    forbiddenfruit.curse(bytes, "urlencode", _urlencode)

    forbiddenfruit.curse(str, "findall", _findall)
    forbiddenfruit.curse(str, "len", _len)
    forbiddenfruit.curse(str, "match", _match)
    forbiddenfruit.curse(str, "md5", _md5)
    forbiddenfruit.curse(str, "sha1", _sha1)
    forbiddenfruit.curse(str, "sha256", _sha256)
    forbiddenfruit.curse(bytes, "__xor__", _xor)
    forbiddenfruit.curse(bytes, "len", _len)
    forbiddenfruit.curse(bytes, "md5", _md5)
    forbiddenfruit.curse(bytes, "sha1", _sha1)
    forbiddenfruit.curse(bytes, "sha256", _sha256)

    forbiddenfruit.curse(bytes, "unpack", _unpack)

    forbiddenfruit.curse(list, "len", _len)
    forbiddenfruit.curse(list, "map", _map)
    forbiddenfruit.curse(list, "filter", _filter)
    forbiddenfruit.curse(list, "reduce", _reduce)
    forbiddenfruit.curse(list, "join", _join)

    forbiddenfruit.curse(int, "date", _date)
    forbiddenfruit.curse(str, "time", _time)


else:
    logging.error("Unsupported python variant.")
