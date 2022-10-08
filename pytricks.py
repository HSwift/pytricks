from ast import Num
from operator import xor
import platform
import logging
import functools


def toBytes(func):
    @functools.wraps(func)
    def wrapper(x, *args, **kwargs):
        if type(x) == str:
            if 'encoding' in kwargs:
                x = x.encode(encoding=kwargs['encoding'])
                del kwargs['encoding']
            else:
                x = x.encode()
        return func(x, *args, **kwargs)
    return wrapper


def toStr(func):
    @functools.wraps(func)
    def wrapper(x, *args, **kwargs):
        if type(x) == bytes:
            if 'encoding' in kwargs:
                x = x.decode(encoding=kwargs['encoding'])
                del kwargs['encoding']
            else:
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
    def _ascii(x: bytes) -> list:
        return list(x)

    forbiddenfruit.curse(bytes, "ascii", _ascii)
    forbiddenfruit.curse(str, "ascii", _ascii)

    @toBytes
    def _ascii_format(x: bytes, format: str = "%x", sep: str = ",") -> str:
        return sep.join(map(lambda x: format % x, list(x)))

    forbiddenfruit.curse(bytes, "ascii_format", _ascii_format)
    forbiddenfruit.curse(str, "ascii_format", _ascii_format)

    @toStr
    def _unicode(x: str) -> list:
        return list(map(ord, x))

    forbiddenfruit.curse(bytes, "unicode", _unicode)
    forbiddenfruit.curse(str, "unicode", _unicode)

    @toStr
    def _unicode_format(x: str, format: str = "%x", sep: str = ",") -> str:
        return sep.join(map(lambda x: format % x, list(map(ord, x))))

    forbiddenfruit.curse(bytes, "unicode_format", _unicode_format)
    forbiddenfruit.curse(str, "unicode_format", _unicode_format)

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

    @toStr
    def _unicode_escape(x: str) -> str:
        # json.encoder.py_encode_basestring_ascii
        def encoder(s):
            n = ord(s)
            if n < 0x10000:
                return '\\u{0:04x}'.format(n)
                # return '\\u%04x' % (n,)
            else:
                # surrogate pair
                n -= 0x10000
                s1 = 0xd800 | ((n >> 10) & 0x3ff)
                s2 = 0xdc00 | (n & 0x3ff)
                return '\\u{0:04x}\\u{1:04x}'.format(s1, s2)

        return ''.join(map(encoder, x))

    forbiddenfruit.curse(str, "unicode_escape", _unicode_escape)
    forbiddenfruit.curse(bytes, "unicode_escape", _unicode_escape)

    @toStr
    def _unicode_unescape(x: str) -> str:
        # json.decoder.py_scanstring
        BACKSLASH = {
            '\\': '\\', '/': '/', 'b': '\b', 'f': '\f', 'n': '\n', 'r': '\r', 't': '\t',
        }

        def _decode_uXXXX(s, pos):
            esc = s[pos + 1:pos + 5]
            return int(esc, 16)

        def decoder(x):
            l = len(x)
            i = 0
            chars = []
            while i < l:
                if x[i] == "\\":
                    i += 1
                    if x[i] in BACKSLASH:
                        chars.append(BACKSLASH[x[i]])
                        i += 1
                    elif x[i] == "u":
                        uni = _decode_uXXXX(x, i)
                        i += 5
                        if 0xd800 <= uni <= 0xdbff and x[i:i + 2] == '\\u':
                            uni2 = _decode_uXXXX(x, i + 1)
                            if 0xdc00 <= uni2 <= 0xdfff:
                                uni = 0x10000 + (((uni - 0xd800) << 10) | (uni2 - 0xdc00))
                                i += 6
                        chars.append(chr(uni))
                else:
                    chars.append(x[i])
                    i += 1
            return ''.join(chars)
        return decoder(x)

    forbiddenfruit.curse(str, "unicode_unescape", _unicode_unescape)
    forbiddenfruit.curse(bytes, "unicode_unescape", _unicode_unescape)

else:
    logging.error("Unsupported python variant.")
