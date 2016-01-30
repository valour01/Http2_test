import csv
import os
import errno
import signal
from functools import wraps
from multiprocessing import Pool

sites=[]
i=0
with open('top-1m.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile,delimiter=' ',quotechar='|')
	for row in spamreader:
		i=i+1
		split_row=row[0].split(',')
		print i
		sites.append(split_row[1])
		print split_row[1]

def command(site):
        command='./http-test_new https://www.'+site
        os.system(command)

if __name__ == '__main__':
        p =Pool(300)
        p.map(command,sites)
