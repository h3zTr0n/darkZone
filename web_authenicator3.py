#!/usr/bin/env python3
# calling usefull modules
# Author: Alison Mukoma _kernel21
import urllib.request, urllib.error, urllib.parse

LOGIN  = 'alison'
PASSWD = "you'illNeverGuess"
URL    = 'http://localhost'
REALM  = 'Secure Archive'
url = 'http://python.org/'
# Setting up secure request connection
def handler_version(url):
 	from urllib.parse import urlparse
 	hndlr = urllib.request.HTTPBasicAuthHandler()
 	hndlr.add_password(REALM,
 		urlparse(url)[1], LOGIN, PASSWD)
 	opener = urllib.request.build_opener(hndlr)
 	urllib.request.install_opener(opener)
 	return url

def request_version(url):
	from base64 import encodestring
	req = urllib.request.Request(url)
	b64str = encodestring('%s:%s' % (LOGIN, PASSWD,'utf-8'))[:-1]
	req.add_header("Authorization", "Basic %s" % b64str,'utf-8')
	return req

for funcType in ('handler', 'Request'):
	print('***Using %s:' % funcType.upper())
	f = urllib.request.urlopen(url)
	print(str(f.readline(), 'utf-8'))
	f.close()
