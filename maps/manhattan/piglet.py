"""
POST request. You do this once.
"""

import urllib.parse
import urllib.request
import json
import requests

url = 'https://api.yelp.com/oath2/token'
values = {'grant_type': 'client_credentials', 'client_id':'OGACsAdCi6eXU6RN2w-oDg', 'client_secret': 'vdECCCmfeLMt3EskqckMQytgQxcfztBLsUv1sUQDltmaTG1Iy9yNiWFJPufENaoZ'}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url,data)

with urllib.request.urlopen(req) as response:
	the_page = response.read()

#print(the_page)
#at this point you should get the access token, below:
#b'{"access_token": "EyTtFNQ_63RWCCxDU88XotQhuMQ-_jSRMlQiMPcGA7Qa-OQGqYGpQyrzcFstRglKbnd_DUGVBoZji35Od0MVZFcqwwafIJWfmSfwQAsniqJxuq-RRFDr5UT7Zj0bWnYx", "expires_in": 635748309, "token_type": "Bearer"}'

"""
GET request. You do this every time you want a new thing. Look at untitled.py for the GET request + writing the result to a new file -- this is just a draft.
"""

#def get_search_parameters(city_):
	#values = {}
	#values['location'] = str(city_)
	#values['limit'] = '50'
	#return values

url = 'https://api.yelp.com/v3/businesses/search'
token = 'EyTtFNQ_63RWCCxDU88XotQhuMQ-_jSRMlQiMPcGA7Qa-OQGqYGpQyrzcFstRglKbnd_DUGVBoZji35Od0MVZFcqwwafIJWfmSfwQAsniqJxuq-RRFDr5UT7Zj0bWnYx'
values = {'location': 'New York City','limit':'50'}
headers = {'Bearer': token}
data = urllib.parse.urlencode(values)
get_url = url + '?' + data
req = urllib.request.Request(get_url)
req.add_header("Authorization", "Bearer " + token)
with urllib.request.urlopen(req) as response:
	the_page = response.read()


"""
writing the result to a new file
"""

	#f.write(json.dumps(the_page))