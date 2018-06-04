
# Author: RED1
# Tested on AP model: TL-WR940N
# Date: 30/05/2018
# Email: sam.rad@hotmail.fr

# Description: 
# This code allows to enable/disable Tp-link wifi radio signal
# The authentication method is a combination of ASCII characters and MD5 ex: base64(admin:MD5_password)

import requests
import urllib2
import base64
import hashlib

######################################
# Enter the access point credentials #
######################################
login    = 'admin'
password = 'admin'
ip       = '192.168.1.7'
wifi_control = False

######################################
# Prepare the cookie for http request#
######################################
hash = hashlib.md5(password)
pass_hash = hash.hexdigest()
prepared_cookie = login + ':' + pass_hash
prepared_cookie = base64.b64encode(prepared_cookie.encode('utf8'))

# HTTP request for login #
##########################
myServer = 'http://'+ ip +'/userRpm/LoginRpm.htm?Save=Save'
headers = {
'Host': ip,
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language':'en-US,en;q=0.5',
'Accept-Encoding':'gzip, deflate',
'Referer':'http://'+ ip + '/',
'Cookie':'Authorization=Basic%20'+prepared_cookie,
'Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'Pragma':'no-cache',
 }

# HTTP request to enable/disable WIFI interface #
#################################################
header_control = {
'Host': ip,
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://'+ip+'/BQKSCNDBZFMGDQGB/userRpm/WlanNetworkRpm.htm',
'Cookie': 'Authorization=Basic%20'+prepared_cookie,
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
 }
 
# HTTP response and parsing treatment #
#######################################

req = urllib2.Request(myServer, None, headers)
openedUrl = urllib2.urlopen(req)
html = openedUrl.read()
control_url = html[67:-27]
control_url = control_url[0:-9]

############################################################
# Here you have to enter the name of your wifi and channel #
# To enable the wifi:  ap=1
# To disable the wifi: ap=0
############################################################
if wifi_control == True:
	control_url = control_url + "WlanNetworkRpm_AP.htm?operMode=0&ssid1=Netw0rk&channel=7&mode=6&chanWidth=2&rate=71&addrType=1&ap=1&broadcast=2&Save=Save"
else:
	control_url = control_url + "WlanNetworkRpm_AP.htm?operMode=0&ssid1=Netw0rk&channel=7&mode=6&chanWidth=2&rate=71&addrType=1&ap=0&broadcast=2&Save=Save"

if "http://" in control_url:
	req = urllib2.Request(control_url, None, header_control)
	openedUrl = urllib2.urlopen(req)
	html = openedUrl.read()
	# print html # For debug purpose
else:
	print "Error occured"
