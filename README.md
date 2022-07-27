# pytricks

A series of python patches based on **forbiddenfruit** to improve the experience of REPL (or scripts)

# docs

Pytricks provides a number of handy extensions to python's built-in types. These extensions are anti-pythonic, but can help you program comfortable.

| type | method | examples |
| ---- | ---- | ---- |
| str,bytes | bytes | `"123".bytes() => b"123"` |
| str,bytes | str | `b"123".bytes() => "123"` |
| str,bytes | hex | `"123".hex() => b"313233"` |
| str,bytes | unhex | `"313233".unhex() => b"123"` |
| str,bytes | base64 | `"123".base64() => b"MTIz"` |
| str,bytes | unbase64 | `"MTIz".unbase64() => b"123"` |
| str,bytes | urlencode | `"#".urlencode() => "%23"` |
| str,bytes | urldecode | `"%23".urldecode() => "#"` |
| str | findall | `"112233".findall("..") => ["11", "22", "33"]` |
| str | match |  `"112233".match("1.") => True` |
| str,bytes | md5 | `"123456".md5() => "e10adc3949ba59abbe56e057f20f883e"` |
| str,bytes | sha1 | `"123456".sha1() => "7c4a8d09ca3762af61e59520943dc26494f8941b"` |
| str,bytes | sha256 | `"123456".sha256() =>  "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"` |
| str,bytes,list | len(property) | `"123456".len => 6` |
| str,bytes | \_\_xor\_\_ | `b"123" ^ b"456" => b"\x05\x07\x05"` |
| list | map | `[1, 2, 3, 4].map(lambda x: x * 2) =>  [2, 4, 6, 8]` |
| list | filter | `[1, 2, 3, 4].filter(lambda x: x % 2 == 0) => [2, 4]` |
| list | reduce | `[1, 2, 3, 4].reduce(lambda x, y: x+y) => 10` |
| list | join | `[1, 2, 3, 4].join() => "1234"`|
| int | date | `(1234567890).date =>  "2009-02-14 07:31:30"` | 
| str | time | `"2009-02-14 07:31:30".time() => 1234567890` |
| bytes | unpack | `b"\x00\x01".unpack(">h") => (1,)` |
| str,bytes | json | `"[1,2]".json() => [1,2]` |
| dict,list | to_json | `[1,2].to_json() => "[1, 2]"` |

# install

```bash
pip install -U git+https://github.com/HSwift/pytricks
```

note: pytricks only support **CPython**.

# ipython integration

```bash
echo "import pytricks" >> ~/.ipython/profile_default/startup/auto_import.py
```

# requirements

- CPython >= 3.3
- forbiddenfruit

# references

https://github.com/zardus/fuckpy3

https://github.com/clarete/forbiddenfruit

https://github.com/EZForever/pytrickz
