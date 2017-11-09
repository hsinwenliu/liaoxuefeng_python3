print("I \'m OK.")
print(ord("A"))  # integer
print(chr(66))   # character
print(b'ABC')    # str to bytes # 一個字符對應一個字節
print('ABC'.encode('ascii'))   # b'ABC'
print(b'ABC'.decode('ascii'))  # 'ABC'
print('中文'.encode('utf -8'))  # b'\xe4\xb8\xad\xe6\x96\x87'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # '中文'

print(len('ABC'))   # 3  str 字符數
print(len('中文'))   # 2
print(len(b'ABC'))  # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # 6  bytes 字節數




