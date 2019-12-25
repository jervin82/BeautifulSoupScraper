from bs4 import BeautifulSoup
import urllib

resource = urllib.urlopen('http://jjervin.com/aboutme.html')
for image in resource:
	output = open("file%s.jpg"  % (1+2),"wb")
	output.write(resource.read())
	output.close()
