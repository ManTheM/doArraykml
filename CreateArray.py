# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 01:32:23 2022
@author: MSA

Create nested two triangle shape in Google earth(.kml) for SPAC measurement 
with given parameters
(put this script in same folder with "triangular.py" before run)
"""
import simplekml
from triangular import array, convert
###########################
#### Define Parameters ####
#==============================================================================
name    = 'fatma'     # Name of the .kml file
#=====================================
flag    = 0                # 0 = degree / 1 = UTM
br      = 326                # Bearing = Azimuth (degree)
d       = 1000
#d       = 866.0254              # Triangular Edge Distance (m)
# if flag "0" ========================
c_lat   = 39.812236        # Center Latitude (with decimal degree)
c_lon   = 30.610951        # Center Longitude (with decimal degree)
# if flag "1" ========================
c_east  = 295525.71
c_north = 4409652.17
hemi    = 'N' # N or S, Hemisphere
zone    = 36
#==============================================================================
if flag == 0:
    # Convert Center Coordinates to Deg to UTM / return utmx, utmy
    coordinate = convert.deg2utm(c_lat, c_lon)
    utmx, utmy = coordinate
else:
    utmx = c_east
    utmy = c_north

# Add UTM Coordinates to Cartesian Values / return N0, N1, N2, N3
ucgen_utm = array.cartesian(utmx, utmy, br, d)
  
ucgen_degg = []
for i in ucgen_utm:
    z = convert.utm2deg(zone, hemi, i[0], i[1])
    ucgen_degg.append(z)

#### Do .kml file
kml = simplekml.Kml()
for i in range(7):
    kml.newpoint(name=i, 
                 description = f"{ucgen_degg[i][1]:.5f} Lon , {ucgen_degg[i][0]:.5f} Lat\n{ucgen_utm[i][1]:.2f} D , {ucgen_utm[i][0]:.2f} K\nL={d}m Azim={br}", 
                 coords = [(ucgen_degg[i][1], ucgen_degg[i][0])])
#### Array Triangle Polygon
pol = kml.newpolygon(name=name)
# Placed in Longitude, Latitude into boundaries
pol.outerboundaryis.coords = [(ucgen_degg[1][1],ucgen_degg[1][0]), 
                              (ucgen_degg[2][1],ucgen_degg[2][0]), 
                              (ucgen_degg[3][1],ucgen_degg[3][0]), 
                              (ucgen_degg[1][1],ucgen_degg[1][0])]
pol.innerboundaryis =        [(ucgen_degg[4][1],ucgen_degg[4][0]), 
                              (ucgen_degg[5][1],ucgen_degg[5][0]), 
                              (ucgen_degg[6][1],ucgen_degg[6][0]), 
                              (ucgen_degg[4][1],ucgen_degg[4][0])]
#### Polygon Style
pol.style.linestyle.color = simplekml.Color.lawngreen
pol.style.linestyle.width = 3
pol.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.red)

# print(array.distance(c_lat, c_lon, points[0][0], points[0][1]), "K.M")
# print(array.haversine(c_lat, c_lon, points[0][0], points[0][1]), "K.M.")

kml.save(f"{name}.kml")

# =============================================================================
#     with open('arraypoints','w') as f:
#         print(f.outer_points)
# =============================================================================