#!/usr/bin/env python2.7

"""
=========================================================================
= urltester.py
=========================================================================
= This python class will take a list of urls and in multiple threads 
= then hit each server and retrieve the document specified in the url
= the threads will place their output into a que the top of the que
= will be returned as the fastest page.
=========================================================================
= Output will be returned in the format of
=========================================================================
 NEWRECORD URL Time Retrieved  Returned URL Document 

 Code will print ALL results to terminal and output variable
=========================================================================
= Output will be acccessable through fucntion parse it or print it to 
= stdio see urluser.py for basics
= 
= Use this class to test new server configurations 
=========================================================================
= Code is releaseed under GNU GPL V3 Please see liscence for details
= Code Source: https://github.com/gsilvers/urltester
= Contact greg.silverstein@gmail.com
=========================================================================
"""

import Queue
import threading
import urllib2
import datetime
import time

class urltester:

    def __init__(self):
        ## Initialize Required Structures Output Que and URL List ##
        ## Add Defaults for URL List                              ##
        self.outQue = Queue.Queue()              
        self.urlList =  ['http://fooples.com/db_editor/index.php','http://fooples.com/index.php']

    def updateUrlList(self,newList):
        ## Very Complex Function to update urlList to new Value   ##
        self.urlList = newList

    def getUrl(self,urlToRetr):
        ## This function will be our thread worker will add to    ##
        ## output Queue                                           ##

        ## get document and timestamp                             ##
        retDocument = urllib2.urlopen(urlToRetr).read()
        tmpTimeStamp = datetime.datetime.now()
        retTimeStamp = tmpTimeStamp.strftime('%m/%d/%Y%H/%M/%S/%f')

        ## Combine to output format                               ##
        combinedResult = "NEWRECORD" + urlToRetr + "  " + retTimeStamp + "  " + retDocument       
        self.outQue.put(combinedResult)   ## Finally Put on Queue ##

    def compareUrls(self):
        ## Execute Actual Comparison                              ##
                      
        ## now for each url spawn a worker thread and get         ##
        for url in self.urlList:
            wThread = threading.Thread(target=self.getUrl,args = (url,))
            wThread.daemon = True
            wThread.start()

    def getResults(self):
        ## Wait for workers to expire                             ##
        while threading.active_count() > 1:
            ## Debugging Code ##
            print "active threads:" 
            print threading.active_count()
            ## End Debugging Code ##
            time.sleep(1)
        ## Once done put a stop in que                            ##
        self.outQue.put('STOP')
        ## Print output to screen as well as return as variable   ##
        ## First Iterate Through Queue and dump to list           ##
        result = []
        for item in iter(self.outQue.get, 'STOP'):
            print "dumping output" 
            result.append(item)
        ## Now Print ## 
        print ' \n'.join(result) 
        return result

        

