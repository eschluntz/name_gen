import Queue
import threading
import whois
from itertools import product
import time
import socket


# check a url
def test_url(url):
	try:
		record = whois.whois(url)
	except KeyboardInterrupt:
		raise
	except socket.error:
		# let's just try again!
		time.sleep(.3)
		test_url(url)
	except:
		# domain not registered!
		print url

# run queue
def run_q(q, url):
	q.put(test_url(url))

with open('pre.txt', 'r') as f:
	pre_words = f.read().splitlines()

with open('post.txt', 'r') as f:
	post_words = f.read().splitlines() + ['']

with open('endings.txt', 'r') as f:
	endings = f.read().splitlines()

# trying all combos
urls = [pre.capitalize() + post.capitalize() + "." + end for \
		pre, post, end in product(pre_words, post_words, endings)]

q = Queue.Queue()

# spinning off threads so we don't have to wait for responses one at a time
for url in urls:
	t = threading.Thread(target=run_q, args = (q, url))
	t.daemon = True
	t.start()
	time.sleep(.2) # faster = more errors

# let the threads start finishing before we end
time.sleep(1)