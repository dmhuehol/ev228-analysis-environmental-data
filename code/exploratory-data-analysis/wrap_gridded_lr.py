import sys
import time

from icecream import ic
import numpy as np
from scipy import stats

import fun_calc_var as fcv
import fun_import as fi
import fun_plots as fp

tic = time.time()
path = '/Users/danielhueholt/Data/ev228_data/gridded/'
fn = 'era5_t2m_1997-2025.nc'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251111/'
out_fn = 'lr.png'

da = fi.import_era5(file_path=path + fn, var='t2m')
tic = time.time()
da_ll = da.isel(latitude=40, longitude=100)
x_arbitrary = np.arange(0, len(da_ll.valid_time.data))
slope, intercept, r_value, p_value, std_err = stats.linregress(
    np.squeeze(x_arbitrary), np.squeeze(da_ll))
ic(slope, intercept, r_value, p_value, std_err)
r2 = r_value ** 2
toc = time.time() - tic
ic(toc)

# arr_lr = np.full(
#     (len(da['longitude']), len(da['latitude'])), np.nan)
# for lat in np.arange(0, len(da['latitude'])):
#     ic(lat)
#     for lon in np.arange(0, len(da['longitude'])):
#         ic(lon)
#         da_active = da.isel(latitude=lat, longitude=lon)
#         slope_active, intercept_active, r_value_active, p_value_active, _ = stats.linregress(
#             np.squeeze(x_arbitrary), np.squeeze(da_active))
#         arr_lr[lon, lat] = slope_active
# print(arr_lr)

# ic(x_arbitrary, da)
# sys.exit('STOP')
x_arbitrary = np.arange(0, len(da_ll.valid_time.data))
x_arbitrary = np.expand_dims(x_arbitrary, axis=[1,2])
tic = time.time()
arr_lr_vec = fcv.calc_lin_reg_vec(x_arbitrary, np.squeeze(da))
toc = time.time() - tic
ic(toc)
print(arr_lr_vec['grad'])
in_title = 'ERA5 trend 1997-2025'
fp.map_cartopy(
    arr_lr_vec['grad'], out_path, out_fn, cmap='RdBu_r', in_title=in_title, 
    vmin=-0.005, vmax=0.005)


