'''wrap_map_cartopy
Demonstrate plotting a gridded dataset as a true map using Cartopy to interpret
geospatial features.
'''
from icecream import ic

import fun_import as fi
import fun_plots as fp

path = '/Users/danielhueholt/Data/ev228_data/gridded/'
fn = 'era5_t2m_1997-2025.nc'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251112/'
out_fn = '2_era5-cartopy.png'

#  Import data and prepare for plotting
da = fi.import_era5(file_path=path + fn, var='t2m')
da_timemn = da.mean(dim='valid_time') #  dimension reduction
da_toplot = da_timemn - 273.15 #  convert Kelvin to degrees Celsius

fp.map_cartopy(
    da_toplot, out_path=out_path, out_name=out_fn, vmin=-20, vmax=30,
    cmap='twilight')
