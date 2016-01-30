#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import os
import MySQLdb as mdb
import sys
import re

i=0
sites=[]
'''
with open('top-1m.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile,delimiter=' ',quotechar='|')
        for row in spamreader:
                i=i+1
                split_row=row[0].split(',')
                sites.append(split_row[1])
                print i
'''

def check(sequence):
	A=sequence.find('1')
#	print A
        B=sequence.find('3')
        C=sequence.find('5')
        D=sequence.find('7')
        E=sequence.find('9')
        F=sequence.find('11')
        if (A>=0) & (B>=0) &(C>=0) & (D>=0) &(E>=0)&(F>=0)&(D<A)&(A<B)&(A<C)&(A<F)&(C<E):
	    return True
	else:
	    return False	

result={}



try:
    con = mdb.connect('localhost', 'root', 'root', 'http2_new');
    y=[]
    x=[]
    index=0
    cur = con.cursor()
    print "before while"
#	print index
    select_sql="select recv_sequence,finish_sequence,server from result where support_http2=1"
        #print update_sql
        #print select_sql
    cur.execute(select_sql)
	#print 
	#x.append(index)
	#index=index+10000
	#print index
    rows = cur.fetchall()
    for row in rows:
#	print row[0]
	if check(row[1])&check(row[0]):
	    key=result.get(row[2],None)
	    if key == None:
	        result[row[2]]=1
	    else:
	        result[row[2]]=result[row[2]]+1
    print result
#        print row[0]
	#y.append(rows[0])
    #print x
    #print y
        #if(rows==0):
        #    print site
    #for row in rows:
    #    print row
    
#    print "Database version : %s " % ver
    
except mdb.Error, e:
  
 #   print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()
