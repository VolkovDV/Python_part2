#!/usr/bin/env python
# coding: utf-8

str1, str2, str3 = "разработка", "сокет", "декоратор"

l1 = [strr.encode() for strr in (str1, str2, str3)]

l1

l2 = [strr.decode() for strr in l1]

l2

encodelist = [el.encode('cp1251') for el in l2]
encodelist

decodelist = [el.decode('cp1251') for el in encodelist]
decodelist

encodelist16 = [el.encode('utf-16') for el in l2]
encodelist16

decodelist16 = [el.decode('utf-16') for el in encodelist16]
decodelist16
