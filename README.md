# stringing
String calculator based on formula from The [Keyboard Stringing Guide
](http://a.co/1kLyV1E)

	-> % ./stringing.py --help
	usage: stringing.py [-h] [-m {iron,yellow brass,red brass}] 	[-t TENSION]
                    [-f FREQUENCY] [-l LENGTH] [-d DIAMETER] [-p DENSITY]

	CLI tool for working with keyboard stringing

	optional arguments:
  		-h, --help            show this help message and exit
  		-m {iron,yellow brass,red brass}, --material {iron,yellow 		brass,red brass}
                        String material
  		-t TENSION, --tension TENSION
                        Tension in kg.
  		-f FREQUENCY, --frequency FREQUENCY
                        Frequency in Hz.
  		-l LENGTH, --length LENGTH
                        String length in meters.
  		-d DIAMETER, --diameter DIAMETER
                        String diameter in meters.
  		-p DENSITY, --density DENSITY
                        String density factor (density*pi/g)