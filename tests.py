import unittest
import pytricks


class TestPytricks(unittest.TestCase):

    def test_bytes2str(self):
        self.assertEqual(b"123".str(), "123")

    def test_str2bytes(self):
        self.assertEqual("123".bytes(), b"123")

    def test_str2str(self):
        self.assertEqual("123".str(), "123")

    def test_bytes2bytes(self):
        self.assertEqual(b"123".bytes(), b"123")

    def test_hex(self):
        self.assertEqual("123".hex(), b"313233")
        self.assertEqual(b"123".hex(), b"313233")

    def test_unhex(self):
        self.assertEqual("313233".unhex(), b"123")
        self.assertEqual(b"313233".unhex(), b"123")

    def test_base64(self):
        self.assertEqual("123".base64(), b"MTIz")
        self.assertEqual(b"123".base64(), b"MTIz")

    def test_unbase64(self):
        self.assertEqual("MTIz".unbase64(), b"123")
        self.assertEqual(b"MTIz".unbase64(), b"123")
        self.assertEqual(b"MTIzNA".unbase64(), b"1234")  # auto padding

    def test_urlencode(self):
        self.assertEqual("!@#=1aA你".urlencode(), "%21%40%23%3D1aA%E4%BD%A0")
        self.assertEqual(b"!@#=1aA\xe4\xbd\xa0".urlencode(), "%21%40%23%3D1aA%E4%BD%A0")

    def test_urldecode(self):
        self.assertEqual("%21%40%23%3D1aA%E4%BD%A0".urldecode(), "!@#=1aA你")
        self.assertEqual(b"%21%40%23%3D1aA%E4%BD%A0".urldecode(), "!@#=1aA你")

    def test_findall(self):
        self.assertEqual("112233".findall(".."), ["11", "22", "33"])
        self.assertEqual("112233".findall("a"), [])

    def test_match(self):
        self.assertEqual("112233".match("1."), True)
        self.assertEqual("112233".match("a"), False)

    def test_md5(self):
        self.assertEqual("123456".md5(), "e10adc3949ba59abbe56e057f20f883e")
        self.assertEqual(b"123456".md5(), "e10adc3949ba59abbe56e057f20f883e")

    def test_sha1(self):
        self.assertEqual("123456".sha1(), "7c4a8d09ca3762af61e59520943dc26494f8941b")
        self.assertEqual(b"123456".sha1(), "7c4a8d09ca3762af61e59520943dc26494f8941b")

    def test_sha256(self):
        self.assertEqual("123456".sha256(), "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92")
        self.assertEqual(b"123456".sha256(), "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92")

    def test_len(self):
        self.assertEqual("123456".len, 6)
        self.assertEqual(b"123456".len, 6)
        self.assertEqual([1, 2, 3, 4, 5, 6].len, 6)

    def test_xor(self):
        self.assertEqual(b"123" ^ b"456", b"\x05\x07\x05")
        self.assertEqual(b"123" ^ b"1", b"\x00")
        self.assertEqual("123" ^ "456", b"\x05\x07\x05")

    def test_map(self):
        self.assertEqual([1, 2, 3, 4].map(lambda x: x * 2), [2, 4, 6, 8])

    def test_filter(self):
        self.assertEqual([1, 2, 3, 4].filter(lambda x: x % 2 == 0), [2, 4])

    def test_reduce(self):
        self.assertEqual([1, 2, 3, 4].reduce(lambda x, y: x+y), 10)

    def test_join(self):
        self.assertEqual([1, 2, 3, 4].join(), "1234")
        self.assertEqual([1, 2, 3, 4].join(","), "1,2,3,4")

    def test_date(self):
        n = 1234567890
        self.assertEqual(n.date(), "2009-02-14 07:31:30")
        self.assertEqual("2009-02-14 07:31:30".time(), n)
        self.assertEqual(n.date("%Y-%m-%d"), "2009-02-14")
        self.assertEqual("2009-02-14".time("%Y-%m-%d"), 1234540800)

    def test_unpack(self):
        self.assertEqual(b"\x00\x01\x00\x02\x00\x00\x00\x03".unpack(">hhl"), (1, 2, 3))

    def test_from_json(self):
        self.assertEqual(b'{"a": ["1", 2, 3]}'.json(), {"a": ["1", 2, 3]})
        self.assertEqual('{"a": ["1", 2, 3]}'.json(), {"a": ["1", 2, 3]})

    def test_to_json(self):
        self.assertEqual({"a": ["1", 2, 3]}.to_json(), '{"a": ["1", 2, 3]}')
        self.assertEqual(["1", 2, 3].to_json(), '["1", 2, 3]')

    def test_copy_to_clip(self):
        try:
            import pyperclip
            "abc".clip()
            self.assertEqual("abc", pyperclip.paste())
        except ModuleNotFoundError:
            pass
        except pyperclip.PyperclipException:
            pass

    def test_pates_from_clip(self):
        try:
            import pyperclip
            pyperclip.copy("abc")
            self.assertEqual("".from_clip(), "abc")
        except ModuleNotFoundError:
            pass
        except pyperclip.PyperclipException:
            pass

    def test_ascii(self):
        self.assertEqual("abc".ascii(), [97, 98, 99])
        self.assertEqual(b"\x81\x82\x83".ascii(), [129, 130, 131])

    def test_ascii_fromat(self):
        self.assertEqual("abc".ascii_format("%x", ","), "61,62,63")
        self.assertEqual(b"\x81\x82\x83".ascii_format("%x", ","), "81,82,83")
        self.assertEqual("abc".ascii_format(format="\\x%02x", sep=""), "\\x61\\x62\\x63")
        self.assertEqual(b"\x81\x82\x83".ascii_format(format="\\%03o", sep=""), "\\201\\202\\203")

    def test_html_escape(self):
        self.assertEqual("""a <"'&> b""".htmlescape(),"a &lt;&quot;&#x27;&amp;&gt; b")
        self.assertEqual(b"""a <"'&> b""".htmlescape(),"a &lt;&quot;&#x27;&amp;&gt; b")

    def test_html_unescape(self):
        self.assertEqual("""&#x61;&#32;&lt;&quot;&#x27;&amp;&gt;&#32;&#x62;""".htmlunescape(),"""a <"'&> b""")
        self.assertEqual(b"""&#x61;&#32;&lt;&quot;&#x27;&amp;&gt;&#32;&#x62;""".htmlunescape(),"""a <"'&> b""")


if __name__ == "__main__":
    unittest.main()
