#!/usr/bin/env python2.7

"""
=========================================================================
= urluser.py
=========================================================================
= Demo Code to use URL Tester Object 
=========================================================================
= Code is releaseed under GNU GPL V3 Please see liscence for details
= Code Source: https://github.com/gsilvers/urltester
= Contact greg.silverstein@gmail.com
=========================================================================
"""

import Queue
import threading
import urllib2

# called by each thread
def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

theurls = '''http://google.com http://yahoo.com'''.split()

q = Queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args = (q,u))
    t.daemon = True
    t.start()

s = q.get()
print s
