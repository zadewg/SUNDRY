

import urllib, json, io

#baseurl = 'https://hackerone.com/programs/search?query=type:hackerone&sort=published_at:descending&page={}'
baseurl = "https://hackerone.com/directory?query=type%3Ahackerone&sort=published_at%3Adescending&page={}"
paths, scope = [], []

i = 1
while True:
	r = urllib.urlopen(baseurl.format(i))
	if r.getcode() == 500:
		break
	else:
		scope.append(baseurl.format(i))
	i += 1

print(scope)

for url in scope:
	response = urllib.urlopen(url)
	outdata = json.loads(json.dumps(response.read(), ensure_ascii=False, indent=4))
	a = json.loads(outdata)
	
	with io.open("testfile.json", "w", encoding='utf-8') as FILE:
		for i in range(0,len(a["results"])):
			data = ("{} : {}\n").format((a["results"][i]["name"]), ("https://hackerone.com" + a["results"][i]["url"]))
			FILE.write(data)

