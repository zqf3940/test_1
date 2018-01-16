# -*- coding: UTF-8 -*-
print('包含中文');
print(ord('A'));
print(ord('是'));
print(chr(65));
print(chr(25991));
print('\u4e2d\u6587');
x=b'ABC';
print(x);
print('ABC'.encode('ascii'));
print('中文'.encode('UTF-8'));
print(b'ABC'.decode('ascii'));
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('UTF-8'));
print(b'\xe4\xb8\xad\xff'.decode('UTF-8',errors='ignore'));#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(len('ass'));
print(len('中文'));
print(len(b'ABC'));
print(len('中文'.encode('UTF-8')));
print('Hello,%s'%'world');
print('Hi,%s,you have $%d.'%('Michael',10000));
print('%1d-%02d'%(3,1));
print('%.2f'%3.1415826);