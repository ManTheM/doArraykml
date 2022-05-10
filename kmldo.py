#%%
import pygmt
import simplekml
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

# %%
import pygmt
fig = pygmt.Figure()

# generate points every 10 degrees along a great circle from 10N,50W to 30N,5W
points1 = pygmt.project(center=[-50, 10], endpoint=[-5, 30], generate=10)
# generate points every 750 km along a great circle from 10N,50W to 57.5N,90W
points2 = pygmt.project(center=[-50, 10], endpoint=[-90, 57.5], generate=750, unit=True)
# generate points every 350 km along a great circle from 10N,50W to 68N,5W
points3 = pygmt.project(center=[-50, 10], endpoint=[-5, 68], generate=350, unit=True)

# create a plot with coast and Mercator projection (M)
fig.basemap(region=[-100, 0, 0, 70], projection="M12c", frame=True)
fig.coast(shorelines=True, area_thresh=5000)

# plot individual points of first great circle as seagreen line
fig.plot(x=points1.r, y=points1.s, pen="2p,seagreen")
# plot individual points as seagreen squares atop
fig.plot(x=points1.r, y=points1.s, style="s.45c", color="seagreen", pen="1p")

# plot individual points of second great circle as orange line
fig.plot(x=points2.r, y=points2.s, pen="2p,orange")
# plot individual points as orange inverted triangles atop
fig.plot(x=points2.r, y=points2.s, style="i.6c", color="orange", pen="1p")

# plot individual points of third great circle as red line
fig.plot(x=points3.r, y=points3.s, pen="2p,red3")
# plot individual points as red circles atop
fig.plot(x=points3.r, y=points3.s, style="c.3c", color="red3", pen="1p")

fig.show()
# %%
import pygmt
import simplekml
from math import acos, cos, sin, asin, sqrt, radians, degrees

kml = simplekml.Kml()
# kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])
# kml.save("botanicalgardennn.kml")
name    = 'Array'
c_lon   = 28.630357
c_lat   = 41.004467
hankei  = 0.1   # km
#hankei2 = hankei * math.atan()
#hankei3 = 0
azi     = 90

errey1 = pygmt.project(center=[c_lon, c_lat], azimuth=[azi], length=[0/hankei], unit=True, generate=1)
errey2 = pygmt.project(center=[c_lon, c_lat], azimuth=[azi+120], length=[0/hankei], unit=True, generate=1)
errey3 = pygmt.project(center=[c_lon, c_lat], azimuth=[azi+240], length=[0/hankei], unit=True, generate=1)

print(errey1,errey2,errey3)
"""
pol = kml.newpolygon(name=name)
pol.outerboundaryis = [(18.333868,-34.038274), (18.370618,-34.034421),
                       (18.350616,-34.051677),(18.333868,-34.038274)]
pol.innerboundaryis = [(18.347171,-34.040177), (18.355741,-34.039730),
                        (18.350467,-34.048388),(18.347171,-34.040177)]

pol.style.linestyle.color = simplekml.Color.green
pol.style.linestyle.width = 5
pol.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.green)
"""
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

# %%
