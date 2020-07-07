import urllib.request
# gettiing data of google.
x = urllib.request.urlopen("https://www.google.com")
print(x.read())
