#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thu 02 Oct 2014 04:23:02 PM EEST
# Coded by Salih ACAY
import psutil
import time

while True:
    before_list = list(psutil.process_iter())
    time.sleep(0.05)
    after_list = list(psutil.process_iter())
    now = time.localtime(time.time())
    now_str = time.strftime("%Y-%m-%d [%H:%M:%S]", now)
    for a_proc in after_list:
        if a_proc in before_list:
            pass
        else:
            try:
                print "[+]", now_str, a_proc.name, a_proc.pid
            except:
                print "interesting", now_str, a_proc.pid
    for a_proc in before_list:
        if a_proc in after_list:
            pass
        else:
            try:
                print "[-]", now_str, a_proc.name, a_proc.pid
            except:
                print "terminated", now_str, a_proc.pid
