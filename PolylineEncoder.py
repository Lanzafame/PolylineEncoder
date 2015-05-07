#!/usr/bin/python

# Polyline Encoder


class Point:
    'Point consists of lat and lon.'

    def __init__(self, lat, lon):
        self.lat = int(lat * 1e5)
        self.lon = int(lon * 1e5)
        self.latbin = 0
        self.lonbin = 0


    def diff(self, previous):
        self.lat = self.lat - previous.lat
        self.lon = self.lon - previous.lon

    def tobin(self):
        # convert to binary
        self.lat = bin(self.lat)
        self.lon = bin(self.lon)

        # if negative, invert and add 1
        if (self.lat < 0):
            self.lat = ~self.lat
            self.lat = self.lat + 1
        if (self.lon < 0):
            self.lon = ~self.lon
            self.lon = self.lon + 1

        # left-shift by one bit
        self.lat = self.lat << 1
        self.lon = self.lon << 1
        
        # if initial value was negative, invert
        if (self.lat < 0):
            self.lat = ~self.lat
        if (self.lon < 0):
            self.lon = ~self.lon

    def chunk(self):

        


initial = Point(39.5, -120)
second = Point(40, 23.780405)

print initial.lat
print initial.lon
print second.lat
print second.lon

second.diff(initial)
print second.lat
print second.lon

initial.tobin()
second.tobin()

print initial.lat
print initial.lon
print "\n"
print second.lat
print second.lon

 
