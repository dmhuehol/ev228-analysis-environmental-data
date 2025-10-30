import matplotlib.pyplot as plt
import xarray as xr

file_path = '/Users/danielhueholt/Data/ev228_data/gridded/'
fn = 'era5_t2m_1997-2025.nc'

ds_era5 = xr.open_dataset(file_path + fn)
da_t2m = ds_era5['t2m']
# print(da_t2m)

#  By default, the .plot() will flatten and bin the data
# da_t2m.plot(); plt.show()

#  Calculate a descriptive statistic on the data
da_t2m_timestat = da_t2m.sum('valid_time')
# print(da_t2m_timestat)

#  Slice an index out of the data
da_t2m_index = da_t2m.isel(valid_time=0)

# da_t2m_index.plot()
# plt.show()