# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:12:32 2022

@author: MSA
"""
#%%
import simplekml
from math import acos, cos, sin, asin, sqrt, radians, degrees

alat = -34.051422
alon =  18.363143
dist = 1.49
alat, alon = map(radians, [alat, alon])


blat = alat + (dist * cos(252))
blon = alon + (dist * sin(252))
# print(blat, blon)
blat, blon = map(degrees, [blat, blon])
print(alat,alon, blat, blon)

def calc_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km



# =============================================================================
# """Lat/Lon/Alt = phi/theta/rho"""
# phi=-34.051881
# theta=18.363517
# rho=1
# x = math.cos(phi) * math.cos(theta) * rho
# y = math.cos(phi) * math.sin(theta) * rho
# z = math.sin(phi) * rho # z is 'up'
# print(x,y,z)
# =============================================================================



# a = calc_distance(-34.051881, 18.363517, -34.055571, 18.347412)
# print(a)
#%%
kml = simplekml.Kml()
# kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])
# kml.save("botanicalgardennn.kml")
name    = 'Array'
c_lon   = 28.630357
c_lat   = 41.004467
hankei  = 50   # metre
hankei2 = hankei * math.atan()
hankei3 = 0
azi     = 0

pol = kml.newpolygon(name=name)
pol.outerboundaryis = [(18.333868,-34.038274), (18.370618,-34.034421),
                       (18.350616,-34.051677),(18.333868,-34.038274)]
pol.innerboundaryis = [(18.347171,-34.040177), (18.355741,-34.039730),
                        (18.350467,-34.048388),(18.347171,-34.040177)]

pol.style.linestyle.color = simplekml.Color.green
pol.style.linestyle.width = 5
pol.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.green)

# =============================================================================
# multipnt = kml.newmultigeometry(name="MultiPoint")
# multipnt.style.labelstyle.scale = 0  # Remove the labels from all the points
# multipnt.style.iconstyle.color = simplekml.Color.red
# for lon in range(2):  # Generate longitude values
#     for lat in range(2): # Generate latitude values
#         multipnt.newpoint(coords=[(lon, lat)])
#
# =============================================================================
kml.save(f"{name}.kml")

#%%
import math

def next_point(lat, lon, br, d):
    """
    Known using Degree point, bearing and distance to calculate another point
        lat = Latitude (Decimal Degree)
        Lon = Longitude (Decimal Degree)
        br  = Bearing (Angle degree between two points)
        d   = Distance in km
    """
    R = 6378.1 #Radius of the Earth
    brng_deg = math.radians(br) 
    brng = brng_deg #Bearing is 90 degrees converted to radians.
    
    # lat1 = math.radians(lat) #Current lat point converted to radians
    # lon1 = math.radians(lon) #Current long point converted to radians
    lat1, lon1 = map(radians, [lat, lon]) #Current lat,lon converted to radians
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
           math.cos(lat1)*math.sin(d/R)*math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
           math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    # lat2 = math.degrees(lat2)
    # lon2 = math.degrees(lon2)
    lat2, lon2 = map(degrees, [lat2, lon2]) #converted to degrees
    return lat2, lon2

a = next_point(-34.047190, 18.390146, 62.29, 0.16)

print(a)