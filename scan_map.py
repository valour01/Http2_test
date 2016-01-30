import os
import errno
import signal
from functools import wraps
from multiprocessing import Pool
class TimeoutError(Exception):
	pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

fp=open('/home/jmh/filter')
sites=[]

#@timeout
def command(site):
	command='./http-test https://www.'+site
	os.system(command)

while 1:
	line = fp.readline()
	if not line:
		break
	#print line
	sites.append(line)
#for site in sites:
#	print site
#map(command,sites)
if __name__ == '__main__':
	p =Pool(200)
	p.map(command,sites)
#os.system('ls');
