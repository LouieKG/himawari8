#!/usr/bin/env python3

import matplotlib.pyplot as plt
import netCDF4
import numpy as np

######################################
# its all a fit fucked - lots of the common libraries for ploting netCDF data arent supported anymore and this was supposed to be a quick muck around.
# Never to be touched again :/

url = 'OR_HFD-020-B14-M1C07-T071_GH8_s2020021120000_c2020022204655.nc'
nc = netCDF4.Dataset(url)


# print(nc.variables.keys())
# print(nc.variables['x'])

# #print all variables


for i in nc.variables.keys():
    print(nc.variables[i])


topo = nc.variables['x'][::10]
print(topo)

x_var = nc.variables['x'][::10]
y_var = nc.variables['y'][::10]

#########################################
#new try

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap

first_file = 'OR_HFD-020-B14-M1C07-T071_GH8_s2020021120000_c2020022204655.nc'
fh = Dataset(first_file, mode='r')

lons = fh.variables['y'][::20]
lats = fh.variables['x'][::20]
tmax = fh.variables['Sectorized_CMI'][::20]

tmax_units = fh.variables['Sectorized_CMI'].units

fh.close()

# Get some parameters for the Stereographic Projection
lon_0 = lons.mean()
lat_0 = lats.mean()

# m = Basemap(width=5000000,height=3500000,
#             resolution='l',projection='stere',\
#             lat_ts=40,lat_0=lat_0,lon_0=lon_0)

# Because our lon and lat variables are 1D,
# use meshgrid to create 2D arrays
# Not necessary if coordinates are already in 2D arrays.

lon, lat = np.meshgrid(lons, lats)

plt.scatter(lon, lat)




xi, yi =m(lon, lat)

# Plot Data
cs = plt(xi,yi,np.squeeze(tmax))

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(tmax_units)

# Add Title
plt.title('DJF Maximum Temperature')

plt.show()

