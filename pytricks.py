from ast import Num
import platform
import logging
import functools


def toBytes(func):
    @functools.wraps(func)
    def wrapper(x, *args, **kwargs):
        if type(x) == str:
            x = x.encode()
        return func(x, *args, **kwargs)
    return wrapper


def toStr(func):
    @functools.wraps(func)
    def wrapper(x, *args, **kwargs):
        if type(x) == bytes:
            x = x.decode()
        return func(x, *args, **kwargs)
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
    import json
    import html

    def _nop(x: any, *args) -> any:
        return x

    def _str(x: str | bytes, encoding: str = 'utf-8') -> str:
        return x.decode(encoding)

    forbiddenfruit.curse(bytes, "str", _str)
    forbiddenfruit.curse(str, "str", _nop)

    def _bytes(x: str | bytes, encoding: str = 'utf-8') -> bytes:
        return x.encode(encoding)

    forbiddenfruit.curse(bytes, "bytes", _nop)
    forbiddenfruit.curse(str, "bytes", _bytes)

    @toBytes
    def _ascii(x: bytes) -> str:
        return list(x)

    forbiddenfruit.curse(bytes, "ascii", _ascii)
    forbiddenfruit.curse(str, "ascii", _ascii)

    @toBytes
    def _ascii_format(x: bytes, format: str = "%x", sep: str = ",") -> str:
        return sep.join(map(lambda x: format % x, list(x)))

    forbiddenfruit.curse(bytes, "ascii_format", _ascii_format)
    forbiddenfruit.curse(str, "ascii_format", _ascii_format)

    @toBytes
    def _hex(x: bytes) -> bytes:
        return binascii.b2a_hex(x)

    forbiddenfruit.curse(str, "hex", _hex)
    forbiddenfruit.curse(bytes, "hex", _hex)

    @toBytes
    def _unhex(x: bytes) -> bytes:
        return binascii.a2b_hex(x)

    forbiddenfruit.curse(str, "unhex", _unhex)
    forbiddenfruit.curse(bytes, "unhex", _unhex)

    @toBytes
    def _base64(x: bytes) -> bytes:
        return base64.b64encode(x)

    forbiddenfruit.curse(str, "base64", _base64)
    forbiddenfruit.curse(bytes, "base64", _base64)

    @toBytes
    def _unbase64(x: bytes) -> bytes:
        return base64.b64decode(x + b'=' * (-len(x) % 4))

    forbiddenfruit.curse(str, "unbase64", _unbase64)
    forbiddenfruit.curse(bytes, "unbase64", _unbase64)

    def _findall(x: str, pattern: str) -> list:
        return re.findall(pattern, x)

    forbiddenfruit.curse(str, "findall", _findall)

    def _match(x: str, pattern: str) -> bool:
        return re.match(pattern, x) != None

    forbiddenfruit.curse(str, "match", _match)

    @toBytes
    def _md5(x: str | bytes) -> str:
        return hashlib.md5(x).hexdigest()

    forbiddenfruit.curse(str, "md5", _md5)
    forbiddenfruit.curse(bytes, "md5", _md5)

    @toBytes
    def _sha1(x: str | bytes) -> str:
        return hashlib.sha1(x).hexdigest()

    forbiddenfruit.curse(str, "sha1", _sha1)
    forbiddenfruit.curse(bytes, "sha1", _sha1)

    @toBytes
    def _sha256(x: str | bytes) -> str:
        return hashlib.sha256(x).hexdigest()

    forbiddenfruit.curse(str, "sha256", _sha256)
    forbiddenfruit.curse(bytes, "sha256", _sha256)

    @property
    def _len(x: str | bytes | list) -> int:
        return len(x)

    forbiddenfruit.curse(str, "len", _len)
    forbiddenfruit.curse(bytes, "len", _len)
    forbiddenfruit.curse(list, "len", _len)

    @toBytes
    def _xor(x: bytes, y: str | bytes) -> bytes:
        z = y.bytes()
        return bytes(a ^ b for a, b in zip(x, z))

    forbiddenfruit.curse(str, "__xor__", _xor)
    forbiddenfruit.curse(bytes, "__xor__", _xor)

    def _map(x: list, callback: callable) -> bytes:
        return list(map(callback, x))

    forbiddenfruit.curse(list, "map", _map)

    def _filter(x: list, callback: callable) -> bytes:
        return list(filter(callback, x))

    forbiddenfruit.curse(list, "filter", _filter)

    def _reduce(x: list, callback: callable) -> bytes:
        return functools.reduce(callback, x)

    forbiddenfruit.curse(list, "reduce", _reduce)

    def _join(x: list, separator: str = '') -> str:
        return separator.join(map(str, x))

    forbiddenfruit.curse(list, "join", _join)

    def _date(x: int, format: str = '%Y-%m-%d %H:%M:%S') -> str:
        time_struct = datetime.datetime.fromtimestamp(x)
        return time_struct.strftime(format)

    forbiddenfruit.curse(int, "date", _date)

    def _time(x: str, format: str = '%Y-%m-%d %H:%M:%S') -> int:
        time_struct = time.strptime(x, format)
        return int(time.mktime(time_struct))

    forbiddenfruit.curse(str, "time", _time)

    def _urlencode(x: str) -> str:
        return urllib.parse.quote_plus(x)

    forbiddenfruit.curse(str, "urlencode", _urlencode)
    forbiddenfruit.curse(bytes, "urlencode", _urlencode)

    @toStr
    def _urldecode(x: str) -> str:
        return urllib.parse.unquote_plus(x)

    forbiddenfruit.curse(str, "urldecode", _urldecode)
    forbiddenfruit.curse(bytes, "urldecode", _urldecode)

    def _unpack(x: bytes, format: str) -> tuple[any, ...]:
        return struct.unpack(format, x)

    forbiddenfruit.curse(bytes, "unpack", _unpack)

    def _json(x: str | bytes) -> any:
        return json.loads(x)

    forbiddenfruit.curse(str, "json", _json)
    forbiddenfruit.curse(bytes, "json", _json)

    def _to_json(x: dict | list) -> str:
        return json.dumps(x)

    forbiddenfruit.curse(dict, "to_json", _to_json)
    forbiddenfruit.curse(list, "to_json", _to_json)

    try:
        import pyperclip

        pyperclip.paste()

        def _copy_to_clip(x: str) -> None:
            pyperclip.copy(x)

        forbiddenfruit.curse(str, "clip", _copy_to_clip)

        def _paste_from_clip(x: str) -> str:
            return pyperclip.paste()

        forbiddenfruit.curse(str, "from_clip", _paste_from_clip)

    except:
        pass

    @toStr
    def _htmlescape(x: str) -> str:
        return html.escape(x)
    
    forbiddenfruit.curse(str, "htmlescape", _htmlescape)
    forbiddenfruit.curse(bytes, "htmlescape", _htmlescape)

    @toStr
    def _htmlunescape(x: str) -> str:
        return html.unescape(x)
    
    forbiddenfruit.curse(str, "htmlunescape", _htmlunescape)
    forbiddenfruit.curse(bytes, "htmlunescape", _htmlunescape)

else:
    logging.error("Unsupported python variant.")
