import matplotlib.pyplot as plt
import xarray as xr

import fun_plots as fp

file_path = '/Users/danielhueholt/Data/ev228_data/gridded/'
fn = 'era5_10mwind_1980-1989.nc'
fig_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251109/'
fig_name = '1-era5.png'

ds_era5 = xr.open_dataset(file_path + fn)
da_t2m = ds_era5['si10']
# print(da_t2m)

#  By default, the .plot() will flatten and bin the data
# da_t2m.plot(); plt.show()

#  Calculate a descriptive statistic on the data
da_t2m_timestat = da_t2m.mean('valid_time')
print(da_t2m_timestat)

#  Slice an index out of the data
# da_t2m_index = da_t2m.isel(valid_time=0)

#  Plots
fp.map(da_t2m_timestat, fig_path, fig_name)
# da_t2m_index.plot()
# plt.show()