#import astropy.units as u
#from astropy.time import Time
#from astropy.coordinates import SkyCoord, EarthLocation, AltAz

class Planet:
	def __init__(self, id, ra, dec):
		self.id = id	# eg. "PSR B1919" TODO naming convention?
		self.ra = ra	# right ascension
		self.dec = dec	# declination

	def __str__(self):
		return "%s, ra=%f, dec=%f" % (self.id, self.ra, self.dec)

def main():
	print("hello world!")
	psr = Planet("PSR B1919", 44.3, 89.3)
	print(psr)

if __name__ == "__main__":
	main()
	
