#!/usr/bin/env.exe python
# -*-	coding: utf-8 -*-
import sys
print(100 +200 +300)
print('one','two','three')
print('100 + 200 =', 100 + 200)

print('please input a name for hello:')
name=input()
print('hello', name, ', type is', type(name))

print(0xFFFF, 12e9)
print("i'm \"ok!\"")
print("i'm \"ok!\"")
print(r'i\'m "ok!"')
print(r'\\\t\\')

print('''line2
line2
line3''')

print(type(9/3), type(10//3))
print(10%3)

print(ord('A'))
print(chr(20013))
print('\u4e2d\u6587')

x = b'ABC'
print('ABC'.encode('ascii'))
print('\u4e2d\u6587'.encode('utf-8'))
print(len('ABC'))
print(len('\u4e2d\u6587'), bytes('\u4e2d\u6587'.encode('utf-8')))
print(len('\u4e2d\u6587'.encode('utf-8')))
print(u'中文')

print('\u4e2d\u6587'.encode('utf-8').decode())

print('hello, %s' % 'world')

print('%2d-%02d' % (3, 1))
