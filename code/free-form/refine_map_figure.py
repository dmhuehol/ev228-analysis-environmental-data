'''refine_map_figure
Make map plot with gridded ERA5 data. This file is used for in-class 
demonstrations of various refinements and statistics (e.g., changing colorbar, 
latitude weighting, tic/toc profiling, unit conversions, etc.)
'''
import time

from icecream import ic
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

import fun_import as fi
import fun_plots as fp

path = '/Users/danielhueholt/Data/ev228_data/gridded/'
fn = 'era5_t2m_1997-2025.nc'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251112/'
out_fn = '1_era5_t2m.png'

#  Open data
tic = time.time()
da = fi.import_era5(file_path=path + fn, var='t2m')
toc = time.time() - tic
ic(toc)

#  Plot data
da_timemn = da.mean(dim='valid_time') #  Dimension reduction
da_toplot = da_timemn - 273.15 #  Convert Kelvin to degrees C
fp.map(
    da_toplot, out_path=out_path, out_name=out_fn, x_label='longitude', 
    y_label='latitude', cb_label='deg C', title='ERA5 2m temp 1997-2025 mean',
    cmap='turbo')

#  Statistics
weights = np.cos(np.deg2rad(da_toplot['latitude']))
da_wghtd = da_toplot.weighted(weights)
da_timemn_wghtd = da_wghtd.mean(dim=['latitude', 'longitude'])
da_timemn_nowghtd = da_toplot.mean(dim=['latitude', 'longitude'])
ic(da_timemn_wghtd.data, da_timemn_nowghtd.data)

