# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:30:39 2022

@author: MSA
"""

import math
from math import radians, degrees, cos, sin, asin, sqrt, pi, atan2
from pyproj import Proj
# import simplekml

class array:   
    
    def cartesian(east, north, azi, a):
        """
        Parameters
        ----------
        east : UTM
        north : UTM
        azi : Degree
        a : Edge distance (m)

        Returns
        -------
        Add UTM Coordinates to Cartesian Values
        """
        r = a/sqrt(3) # Radius of triangular
        # Cartesian Coordinate
        M_0 = [0, 0]
        M_1 = [math.sin(radians(0  +azi)) * r, math.cos(radians(0  +azi)) * r]
        M_2 = [math.sin(radians(120+azi)) * r, math.cos(radians(120+azi)) * r]
        M_3 = [math.sin(radians(240+azi)) * r, math.cos(radians(240+azi)) * r]
        M_4 = [math.sin(radians(60 +azi)) * r/2, math.cos(radians(60 +azi)) * r/2]
        M_5 = [math.sin(radians(180+azi)) * r/2, math.cos(radians(180+azi)) * r/2]
        M_6 = [math.sin(radians(300+azi)) * r/2, math.cos(radians(300+azi)) * r/2]
        # Add utm values to cartesian
            
        N_0 = [M_0[0]+east, M_0[1]+north]
        N_1 = [M_1[0]+east, M_1[1]+north]
        N_2 = [M_2[0]+east, M_2[1]+north]
        N_3 = [M_3[0]+east, M_3[1]+north]
        N_4 = [M_4[0]+east, M_4[1]+north]
        N_5 = [M_5[0]+east, M_5[1]+north]
        N_6 = [M_6[0]+east, M_6[1]+north]
        
        return N_0, N_1, N_2, N_3, N_4, N_5, N_6
        
    def next_point(lon, lat, br, d):
        """
        Known using Degree point, bearing and distance to calculate another point
            lat = Latitude (Decimal Degree)
            Lon = Longitude (Decimal Degree)
            br  = Bearing (Angle degree between two points)
            d   = Distance in km
        """
        R = 6378.1 #Radius of the Earth by IERS(2003)
        lat1, lon1, brng = map(radians, [lat, lon, br]) #Current lat,lon,br converted to radians
    
        lat2 = math.asin( math.sin(lat1) * math.cos(d/R) + 
                         math.cos(lat1) * math.sin(d/R) * math.cos(brng))
        lon2 = lon1 + math.atan2(math.sin(brng) * math.sin(d/R) * math.cos(lat1), 
                                 math.cos(d/R) - math.sin(lat1) * math.sin(lat2))
    
        lat2, lon2 = map(degrees, [lat2, lon2]) #converted to degrees
    
        return lat2, lon2
    
    def distance(lat1, lon1, lat2, lon2):
        """
        Parameters
        ----------
        lat1 : First point latitude
        lon1 : First point Longitude
        lat2 : Second point Latitude
        lon2 : Second point Longtude
        All Coordinates types are Decimal Degreee (ex. 20.123, 30.123)
        
        Returns
        -------
        Distance between points in km
        """
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
     
        c = 2 * asin(sqrt(a))
        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371

        return(c * r)

    def haversine(lat1, lon1, lat2, lon2):
     
        # distance between latitudes and longitudes
        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0
        # convert to radians
        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0
        # apply formulae
        a = (pow(math.sin(dLat / 2), 2) +
             pow(math.sin(dLon / 2), 2) *
                 math.cos(lat1) * math.cos(lat2));
        r = 6371
        c = 2 * math.asin(math.sqrt(a))
    
        return r * c

    def rotated_grid_transform(grid_in, option, SP_coor):
        """https://gis.stackexchange.com/questions/10808/manually-transforming-rotated-lat-lon-to-regular-lat-lon?rq=1"""
        lon = grid_in[0]
        lat = grid_in[1];
    
        lon = (lon*pi)/180; # Convert degrees to radians
        lat = (lat*pi)/180;
    
        SP_lon = SP_coor[0];
        SP_lat = SP_coor[1];
    
        theta = 90+SP_lat; # Rotation around y-axis
        phi = SP_lon; # Rotation around z-axis
    
        theta = (theta*pi)/180;
        phi = (phi*pi)/180; # Convert degrees to radians
    
        x = cos(lon)*cos(lat); # Convert from spherical to cartesian coordinates
        y = sin(lon)*cos(lat);
        z = sin(lat);
    
        if option == 1: # Regular -> Rotated
    
            x_new = cos(theta)*cos(phi)*x + cos(theta)*sin(phi)*y + sin(theta)*z;
            y_new = -sin(phi)*x + cos(phi)*y;
            z_new = -sin(theta)*cos(phi)*x - sin(theta)*sin(phi)*y + cos(theta)*z;
    
        else:  # Rotated -> Regular
    
            phi = -phi;
            theta = -theta;
    
            x_new = cos(theta)*cos(phi)*x + sin(phi)*y + sin(theta)*cos(phi)*z;
            y_new = -cos(theta)*sin(phi)*x + cos(phi)*y - sin(theta)*sin(phi)*z;
            z_new = -sin(theta)*x + cos(theta)*z;
    
    
    
        lon_new = atan2(y_new,x_new); # Convert cartesian back to spherical coordinates
        lat_new = asin(z_new);
    
        lon_new = (lon_new*180)/pi; # Convert radians back to degrees
        lat_new = (lat_new*180)/pi;
    
        print (lon_new,lat_new)       

class convert:
    
    def dokml():
        
        return 
    
    def deg2utm(lat, lon):
        ##Compute UTM zone
        #"int": Extract only integer value
        #31: Offset for UTM zone definition
        #6: Angle in a UTM zone for the longitude direction
        e2u_zone=int(divmod(lon, 6)[0])+31
        
        #Define EQA2UTM converter
        e2u_conv=Proj(proj='utm', zone=e2u_zone, ellps='WGS84')
        #Apply the converter
        utmx, utmy=e2u_conv(lon, lat)
        #Add offset if the point in the southern hemisphere
        if lat<0:
            utmy=utmy+10000000
            
        print(" UTM zone is ", e2u_zone, " \n", \
              "UTM Easting is", utmx, "[m]\n",\
              "UTM Northing is ", utmy, "[m]") 
        return utmx, utmy
    
    def utm2deg(e2u_zone, hemi, utmx, utmy):   
        #Add offset if the point in the southern hemisphere
        if hemi=='S':
            utmy=utmy-10000000
            
        #Define coordinate converter
        e2u_conv=Proj(proj='utm', zone=e2u_zone, ellps='WGS84')
        #Convert UTM2EQA
        lon, lat=e2u_conv(utmx, utmy, inverse=True)
            
        print("Longitude is ",lon," [deg.] \n",\
              "Latitude is ", lat, "[deg.]")
        return lat, lon
    
    
            
# =============================================================================
#     def deneme(lat1, lon1, distKm):
#
#         c=print(lat1, lon1)                                                                      #center
#         n=print(geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())  #north
#         e=print(geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal()) #east
#         s=print(geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())#south
#         w=print(geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal())#west
#  
#         return n,e,s,w
#     
# points1=[]
# z= deneme(c_lat, c_lon, d)
# points1.append(z)
# =============================================================================

# =============================================================================
# class array:
#     R = 6378.1
# 
#     def __init__(self, lat, lon, azi, r):
#         self.lat = lat
#         self.lon = lon
#         self.azi = azi
#         self.r   = r
#     
#     def show(self):
#         brng_deg = math.radians(self.azi) 
#         brng = brng_deg #Bearing is 90 degrees converted to radians.
#         
#         # lat1 = math.radians(lat) #Current lat point converted to radians
#         # lon1 = math.radians(lon) #Current long point converted to radians
#         lat1, lon1 = map(radians, [self.lat, self.lon]) #Current lat,lon converted to radians
#         lat2 = math.asin( math.sin(lat1)*math.cos(self.r/array.R) +
#                math.cos(lat1)*math.sin(self.r/array.R)*math.cos(brng))
#         lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(self.r/array.R)*math.cos(lat1),
#                math.cos(self.r/array.R)-math.sin(lat1)*math.sin(lat2))
#         # lat2 = math.degrees(lat2)
#         # lon2 = math.degrees(lon2)
#         lat2, lon2 = map(degrees, [lat2, lon2]) #converted to degrees
#         return lat2, lon2
# 
# s1= array(-34.047190, 18.390146, 62.29, 0.16)
# s1 = array.show()
# 
# =============================================================================