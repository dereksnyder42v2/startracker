#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

from math import pi
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

import Planet
import mayaUtils

# Argument types: ra, dec, lat, long, time string
# eg. (planet).ra, (planet).dec, 44.3, 89.3, 300, '2019-8-22 12:00:00'
def getAz(ra, dec, lat, lon, elev, timeStr):
	loc = EarthLocation(lat = lat*u.deg, lon = lon*u.deg, height=elev*u.m)
	skyObj = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
	skyObjAltAz = skyObj.transform_to(AltAz(obstime=timeStr, location=loc))
	return skyObjAltAz.az.deg

def getAlt(ra, dec, lat, lon, elev, timeStr):
	loc = EarthLocation(lat = lat*u.deg, lon = lon*u.deg, height=elev*u.m)
	skyObj = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
	skyObjAltAz = skyObj.transform_to(AltAz(obstime=timeStr, location=loc))
	return skyObjAltAz.alt.deg

def convert_HH_MM_SS(hours, minutes, seconds):
	"""
	1 hr 	= 15 deg
	1 min 	= 1/60 hr
	1 sec	= 1/60 min	= 1/3600 hr 
	"""
	return hours*15 + minutes*(15/60) + seconds*(15/3600)

def convert_DEG_MIN_SEC(deg, min, sec):
	if deg >= 0:
		return deg + min/60 + sec/3600
	else:
		return deg - min/60 - sec/3600

# dimensionality of both args must be the same!
def polarGraph(rSeries, thetaSeries):
	fig = plt.figure(figsize=(5,10)) #width, height
	ax = plt.subplot(1, 1, 1, projection='polar')
	trans_offset = mtransforms.offset_copy(ax.transData, fig=fig, y=6, units='dots')
	for x, y, in zip(rSeries, thetaSeries):
		plt.polar(x, y, 'ro')
		plt.text(x, y, '%d, %d' % (int(x), int(y)),
			transform=trans_offset,
			horizontalalignment='center',
			verticalalignment='bottom')
	plt.show()
	return

# FOR NOW, prints results. TODO return array
# planet, date, hour, min, az, alt,
def getPlanetPath(planet, startTime, endTime, lat, lon, elev, subDivsPerHour=0):
	return

# convert deg/ min/ sec latitude to decimal...NORTH positive, SOUTH negative
# eg (35, 57, 33, 'N')
def latConvert(deg, min, sec, direc):
	ans = deg + min/60 + sec/3600
	if direc == 'N':
		return ans
	elif direc == 'S':
		return -1*ans
	else:
		print("did not recognize direction in latitude conversion! exiting")
		exit(-1)

# convert deg/ min/ sec latitude to decimal...NORTH positive, SOUTH negative
# eg (83, 55, 22, 'W')
def lonConvert(deg, min, sec, direc):
	ans = deg + min/60 + sec/3600
	if direc == 'E':
		return ans
	elif direc == 'W':
		return -1*ans
	else:
		print("did not recognize direction in longitude conversion! exiting")
		exit(-1)

# just feet to meters conversion bro
def elevConvert(feet):
	meters = feet/3.281
	return meters

def main():
	"""
	My coordinates on Earth;
	35.955278*N, 84.154167*W
	Approx. 300 M elevation
	
	Polaris coordinates
	RA      2h 57m 2.8s  (44.2625 deg)
	DEC     89*20' 48.9" (89.3469 deg)

	A couple pulsars...

	PSR B0833-45 ( V e l a )
	RA      8h  35m 20.6 (128.836083) 	
	DEC    -45* 10' 35.1 (-45.176416) 

	PSR B1919+21
	RA      19h 21m 44.8 (290.4375 deg)
	DEC     21* 53' 2.3" (21.8839 deg)

	PSR B1509-58
	RA      15h 13m 55.5 (228.4833 deg)
	DEC    -59* 8'  8.8" (-59.1358 deg)

	PSR B1257+12
	RA      13h 00m 1s   (195.0042 deg)
	DEC     12* 40' 57"  (12.6825 deg)

	PSR B1620-26
	RA      16h 23m 38.2 (245.9083 deg)
	DEC    -26* 31' 54"  (-26.5317 deg)
	"""
	
	MYLAT = latConvert(35, 57, 31, 'N')
	MYLON = lonConvert(83, 55, 28, 'W')
	MYELEV = elevConvert(870)
	#myLocation = EarthLocation(lat = 35.955278*u.deg, lon = 84.154167*u.deg, height=300*u.m)
	utcOffset = -4*u.hour # Eastern Daylight Time offset from UTC 
	#time = Time('2019-8-1 14:26:00') - utcOffset
	
	planets = []
	polaris = Planet.Planet("Polaris", 44.3, 89.3)
	sirius = Planet.Planet("Sirius", 101.2833, -16.7231)
	vela = Planet.Planet("Vela pulsar", 128.84, -45.2)
	
	#planets.append(polaris)
	planets.append(sirius)
	#planets.append(vela)
	
	graphAlt = []
	graphAz = []
	print("Planet,Hour,Azimuth,Altitude,")
	for p in planets:
		for ts in mayaUtils.getSeries(	'2019-08-29 00:00:00',
										'2019-08-30 00:00:00',
										stepSeconds=1800):
			
			#print(ts)
			thisAz = getAz(p.ra, p.dec, MYLAT, MYLON, MYELEV, Time(ts) - utcOffset)
			thisAlt = getAlt(p.ra, p.dec, MYLAT, MYLON, MYELEV, Time(ts) - utcOffset)
			
			if thisAlt >= 0: #don't plot points below the horizon
				graphAlt.append(thisAlt)
			else:
				graphAlt.append(0)
			graphAz.append(thisAz*(pi/180))
			
			# For .CSV format...
			# date, hour(24), hour as integer, azimuth*, altitude*)
			print("%s,%s,%f,%f," % (p.id, str(ts), thisAz, thisAlt) )
			
	# for graphing altitude and azimuth
	#polarGraph(graphAz, graphAlt)

if __name__ == "__main__":
	main()
