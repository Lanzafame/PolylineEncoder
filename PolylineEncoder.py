#!/usr/bin/python

# PolylineEncoder.py
# Author: Adrian Lanzafame

class Point:
  'A point consists of a Lat/Lon'
  
  def __init__(self, lat, lon):
    self.lat = int(lat * 1e5)
    self.lon = int(lon * 1e5)
    
    
  def deltaPoint(firstPoint):
    self.lat = self.lat - firstPoint.lat
    self.lon = self.lon - firstPoint.lon
    
