# pytricks

python no more python

# usage

```python
import pytricks

'你好'.len # 2
'你好'.bytes() # b'\xe4\xbd\xa0\xe5\xa5\xbd'
b'\xe4\xbd\xa0\xe5\xa5\xbd'.str() # '你好'
'abcabc'.base64() # b'YWJjYWJj'
'abcabc'.md5() # '900150983cd24fb0d6963f7d28e17f72'
'aabbccdd'.findall(r'..') # ['aa', 'bb', 'cc', 'dd']
b'123456' ^ b'abcde' # b'PPPPP'
[65,66,67,68,69].map(lambda x:chr(x)).join() # 'ABCDE'
[65,66,67,68,69].filter(lambda x:x%2).map(lambda x:chr(x)).join() # 'ACE'
[1,2,3,4,5].reduce(lambda x,y:x+y) # 15
```

# requirements

- CPython
- Python >= 3.3
- forbiddenfruit

# references

https://github.com/zardus/fuckpy3

https://github.com/clarete/forbiddenfruit