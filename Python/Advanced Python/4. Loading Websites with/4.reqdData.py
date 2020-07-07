import urllib.parse
reqdData = urllib.parse.urlencode(values)
reqdData = data.encode("utf-8")
# data should be bytes
request = urllib.request.Request(url, reqdData)
responseData = urllib.request.urlopen(request)
responseData = respose.read()
print(responseData)
