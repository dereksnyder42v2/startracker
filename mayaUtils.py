#!/usr/local/bin/python3

import maya

def main():
	xs = getSeries( '2019-08-28 00:00:00',
					'2019-08-29 00:00:00',
					stepSeconds=1800)
	for x in xs:
		print(x)

"""
   start fmt: yyyy-mm-dd hh:mm:ss
     end fmt: yyyy-mm-dd hh:mm:ss
 stepSeconds: interval size in seconds, eg...
				1 min...  60
				15 min... 900
				30 min... 1800
				1 hr...	  3600
"""
def getSeries(startD, endD, stepSeconds=3600):
	#startD = maya.when(startD, timezone='US/Eastern') # initiating T I M E Z O N E headache
	startD = maya.when(startD)
	#endD = maya.when(endD, timezone='US/Eastern')
	endD = maya.when(endD)
	timeseries = maya.intervals(start=startD, end=endD, interval=stepSeconds)
	output = []
	for d in timeseries:
		s = "%d-%02d-%02d %02d:%02d:%02d" % (d.year, d.month, d.day, d.hour, d.minute, d.second)
		output.append(s)
	# .intervals() doesn't produce the last entry, so here it is--
	# this could make it wacky if your start/ step/ end combo is wacky
	last = maya.when(s).add(seconds=stepSeconds)
	output.append("%d-%02d-%02d %02d:%02d:%02d" % (last.year, last.month, last.day, last.hour, last.minute, last.second))
	return output 

if __name__=="__main__":
	main()
