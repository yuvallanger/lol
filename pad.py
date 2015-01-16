#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Sat 04 Oct 2014 09:43:40 PM EEST
# Coded by Salih ACAY
import string
import random
x = open("pad","wb")
def c():
    for i in range(32):
        irandom = random.choice(string.ascii_letters)#(string.printable)
        yield irandom
for i in c():
    x.write(i)


