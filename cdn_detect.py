import socket
import dns.resolver
import MySQLdb as mdb
import sys
from multiprocessing import Pool

def get_cdn(site):
	try:
		answers = dns.resolver.query(site, 'CNAME')
		if len(ansers)>1:
        		print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', answers.qname
		print ' query qname:', answers.qname, ' num ans.', len(answers)
        	for rdata in answers:
            		print ' cname target address:', rdata.target
	except:
		pass


sites=[]
try:
    con = mdb.connect('localhost', 'root', 'root', 'http2_new');
    cur = con.cursor()
    select_sql="select uri from result where support_http2=1"
    cur.execute(select_sql)
    rows = cur.fetchall()
    for row in rows:
        sites.append(row[0])
except mdb.Error, e:

 #   print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:

    if con:
        con.close()
'''
for site in sites:
    try:
	i=i+1
	print i
	test_site=site[8:]
    	answers = dns.resolver.query(site, 'CNAME')
    	if len(answers)>1:
		print ' query qname:', answers.qname, ' num ans.', len(answers)
#        for rdata in answers:
#            print ' cname target address:', rdata.target
	
    except:
        continue
'''
if __name__ == '__main__':
        p =Pool(300)
        p.map(get_cdn,sites)

# Basic query
'''for rdata in dns.resolver.query('e5110.e15.akamaiedge.net', 'CNAME') :
    print rdata.target
'''
# Set the DNS Server
'''resolver = dns.resolver.Resolver()
resolver.nameservers=[socket.gethostbyname('ns1.cisco.com')]
for rdata in resolver.query('www.asus.com', 'CNAME') :
    print rdata.target
'''
