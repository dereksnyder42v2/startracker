#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

print("Did you update the current time?")

"""
My coordinates on Earth;
35.955278*N, 84.154167*W
Approx. 300 M elevation
"""

myLocation = EarthLocation(lat=35.955278*u.deg, lon=84.154167*u.deg, height=300*u.m)
myLocation2 = EarthLocation(lat=35.931944*u.deg, lon=84.067222*u.deg, height=300*u.m)
utcOffset = -4*u.hour # Eastern Daylight Time offset from UTC
time = Time('2019-7-16 13:35:00') - utcOffset
print(time)

"""
Polaris coordinates
RA      2h 57m 2.8s (44.2625 deg)
DEC     89*20' 48.9"(89.3469 deg)
"""

print("Current azimuth/ altitude of Polaris")
polaris = SkyCoord(ra=44.2625*u.deg, dec=89.3469*u.deg)
polarisAltAz = polaris.transform_to(AltAz(obstime=time, location=myLocation))
print(polarisAltAz)

"""
A couple pulsars...

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

print("Current altitude/ azimuth of PSR B1919+21")
psr_b1919_p21 = SkyCoord(ra=290.4375*u.deg, dec=21.8839*u.deg)
psr_b1919_p21_AltAz = psr_b1919_p21.transform_to(AltAz(obstime=time, location=myLocation))
print(psr_b1919_p21_AltAz)

print("Current altitude/ azimuth of PSR B1509-58")
psr_b1509_m58 = SkyCoord(ra=228.4833*u.deg, dec=-59.1358*u.deg)
psr_b1509_m58_AltAz = psr_b1509_m58.transform_to(AltAz(obstime=time, location=myLocation))
print(psr_b1509_m58_AltAz)

print("Current altitude/ azimuth of PSR B1257+12")
psr_b1257_p12 = SkyCoord(ra=195.0042*u.deg, dec=12.6825*u.deg)
psr_b1257_p12_AltAz = psr_b1257_p12.transform_to(AltAz(obstime=time, location=myLocation))
print(psr_b1257_p12_AltAz)

print("Current altitude/ azimuth of PSR B1620-26")
psr_b1620_m26 = SkyCoord(ra=245.9083*u.deg, dec=-26.5317*u.deg)
psr_b1620_m26_AltAz = psr_b1620_m26.transform_to(AltAz(obstime=time, location=myLocation))
print(psr_b1620_m26_AltAz)



