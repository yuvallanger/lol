#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thu 02 Oct 2014 04:23:02 PM EEST
# Coded by Salih ACAY
import psutil
import time

while True:
    a = psutil.get_process_list()
    time.sleep(0.05)
    b = psutil.get_process_list()
    now = time.localtime(time.time())
    t = "%s-%s-%s [%s:%s:%s]"%(now.tm_mday,now.tm_mon,now.tm_year,now.      tm_hour,now.tm_min,now.tm_sec)
    for i in b:
        if i in a:
            pass
        else:
            try:
                print "[+]",t,i.name,i.pid
            except:
                print "interesting",i.pid
    for i in a:
        if i in b:
            pass
        else:
            try:
                print "[-]",t,i.name,i.pid
            except:
                print "terminated",i.pid
