"""
GET request. You do this every time you want a new thing.
"""

#def get_search_parameters(city_):
	#values = {}
	#values['location'] = str(city_)
	#values['limit'] = '50'
	#return values

import urllib.parse
import urllib.request
import json

url = 'https://api.yelp.com/v3/businesses/search'
token = 'EyTtFNQ_63RWCCxDU88XotQhuMQ-_jSRMlQiMPcGA7Qa-OQGqYGpQyrzcFstRglKbnd_DUGVBoZji35Od0MVZFcqwwafIJWfmSfwQAsniqJxuq-RRFDr5UT7Zj0bWnYx'
values = {'location': 'New York City','limit':'50'}
headers = {'Bearer': token}
data = urllib.parse.urlencode(values)
get_url = url + '?' + data
req = urllib.request.Request(get_url)
req.add_header("Authorization", "Bearer " + token)
with urllib.request.urlopen(req) as r:
	result = json.loads(r.read().decode(r.headers.get_content_charset('UTF-8')))

with open("newfilename.json","a+") as f:
	for elem in result["businesses"]:
		f.write(json.dumps(elem))
		f.write('\n')

#the_page = response.read()
#the_page.decode('UTF-8')
#print(the_page)