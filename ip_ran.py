#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Coded by Salih ACAY
# Started     :Thu Dec 25 15:00:18 2014
# Last update :Fri Dec 26 11:06:32 2014
import re
f = open("tr.txt","r")
w = open("out.txt","w")
s = re.compile("([0-9]{1,3}).([0-9]{1,3})")

for line in f:
    m =s.match(line)
    if m:
        w.write("%s.%s/16\n"%m.groups())


