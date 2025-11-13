'''wrap_plot_anom
Demonstrate plotting z-score anomaly data (derived in wrap_calc_anom.py).
'''
import xarray as xr

import fun_plots as fp

path = '/Users/danielhueholt/Data/ev228_data/gridded/'
fn = 'era5_t2m-anom-relative-19972025_1997-2025.nc'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251112/'
out_fn = 'era5_anom.png'

da_anom = xr.open_dataarray(path + fn)
da_to_plot = da_anom.isel(year=-2)

in_title = 'ERA5 2024 temp anomaly relative to 1997-2024'
fp.map_cartopy(
    da_to_plot, out_path, out_fn, cmap='RdBu_r', in_title=in_title, vmin=-3, 
    vmax=3)