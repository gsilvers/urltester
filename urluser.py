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

from urltester import urltester

myTester = urltester()

## Replace Default URLS with List of URLS
myTester.updateUrlList(['http://www.fooples.com/index.php','http://www.google.com','http://www.github.com'])

## Compare when ready
myTester.compareUrls()

## Get results, threading waiting etc is encapsulated no need to wait or delay
resData = myTester.getResults()
