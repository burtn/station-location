""" 
Current Wikipedia layout is as follows

Letter Page (e.g. /UK_railway_stations_-_Y
All station pages end in _railway_station

Station page (e.g. /Yarm_railway_station)
<span class="geo">54.493860; -1.351600</span>
<a rel="nofollow" class="external text" href="http://toolserver.org/~rhaworth/os/coor_g.php?pagename=Yarm_railway_station&amp;params=NZ420111_region%3AGB_scale%3A25000">NZ420111</a>
<a rel="nofollow" class="external text" href="http://toolserver.org/~rhaworth/os/coor_g.php?pagename=Accrington_railway_station&amp;params=SD757285_region%3AGB_scale%3A25000">SD757285</a>
<a rel="nofollow" class="external text" href="http://toolserver.org/~rhaworth/os/coor_g.php?pagename=Aldershot_railway_station&amp;params=SU866504_region%3AGB_scale%3A25000">SU866504</a>

"""
import urllib2
import re
from time import sleep
from random import randint

useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17"

noGEODATA = open('noGEODATA.txt', 'w+')
noGRIDREF = open('noGRIDREF.txt', 'w+')
data_file = open('data.csv', 'w+')

EXP_LATLONG = re.compile('<span class="geo">[0-9]+\.[0-9]+; \-*[0-9]+\.[0-9]+</span>')
EXP_GRIDREF = re.compile('<a .+ href="http://toolserver.org/~rhaworth/os/coor_g.php?.+>.+</a>')
EXP_STATIONURL = re.compile('"/wiki/.+_railway_station"')

MIN_WAIT = 0
MAX_WAIT = 10

data_file.write("Station,Latitude,Longitude,OS Grid Ref\n")

def get_station_links(html):
	# Return an array of URLS to station pages
	links = re.findall(EXP_STATIONURL, html)
	for i in range(len(links)):
		links[i] = links[i].replace('"', "")
	return links
	
	
def get_latlong(html):
	latlongs = re.findall(EXP_LATLONG, html)
	if not latlongs:
		return ""
	latlongs[0] = latlongs[0].replace('<span class="geo">', "").replace('</span>', "")
	return latlongs[0]
	
def get_gridref(html):
	gridref = re.findall(EXP_GRIDREF, html)
	print gridref
	if not gridref:
		return ""
	gridref[0] = re.sub('<a .+ href="http://toolserver.org/~rhaworth/os/coor_g.php?.+>\\b', '', gridref[0]).replace('</a>', '')
	return gridref[0]
	
def get_station_name(URLPart):
	return URLPart.replace("/wiki/", '').replace("_railway_station", '')

# Create the alphabet
Alphabet = map(chr, range(65, 91))

for letter in Alphabet:
	req = urllib2.Request('http://en.wikipedia.org/wiki/UK_railway_stations_-_' + letter, headers={'User-Agent' : useragent}) 
	response = urllib2.urlopen(req)
	stations = get_station_links(response.read())
	for station in stations:
		sleep(randint(MIN_WAIT,MAX_WAIT))
		req = urllib2.Request('http://en.wikipedia.org' + station, headers={'User-Agent' : useragent}) 
		response = urllib2.urlopen(req)
		html = response.read()
		(latlong, gridref) = get_latlong(html), get_gridref(html)
		if (latlong == ""):
			print "No GEODATA for " + get_station_name(station)
			noGEODATA.write(station)
		if (gridref == ""):
			print "No GRIDREF for " + get_station_name(station)
			noGRIDREF.write(station)
		print get_station_name(station) + ": " + get_latlong(html)
		print " OS Ref: " + get_gridref(html)
		data_file.write(get_station_name(station) + "," + latlong.split(" ")[0].replace(";", '') + "," + latlong.split(" ")[1] + "," + gridref + "\n")
		
	
	
	