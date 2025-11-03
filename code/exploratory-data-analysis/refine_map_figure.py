import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

import fun_import as fi
import fun_plots as fp

path = '/Users/danielhueholt/Data/ev228_data/gridded/'
fn = 'era5_t2m_1997-2025.nc'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251103/'
out_fn = '3_era5.png'

da = fi.import_era5(file_path=path + fn, var='t2m')
da_timemn = da.mean(dim='valid_time')
da_toplot = da_timemn - 273.15
fp.map(da_toplot, out_path=out_path, out_name=out_fn)
