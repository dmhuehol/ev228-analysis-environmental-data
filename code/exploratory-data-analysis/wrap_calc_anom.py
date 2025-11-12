import sys
import time

from icecream import ic

import fun_import as fi

tic = time.time()
path = '/Users/danielhueholt/Data/ev228_data/gridded/'
fn = 'era5_t2m_1997-2025.nc'
out_fn = 'era5_t2m-anom-relative-19972025_1997-2025.nc'

da = fi.import_era5(file_path=path + fn, var='t2m')
#  Technically, we need to weight by day; omitting this step now for simplicity
da_ann = da[:-1].groupby("valid_time.year").mean()

da_mean_time = da_ann.mean(dim=['year'])
da_stdev_time = da_ann.std(dim=['year'])
da_anom = (da_ann - da_mean_time) / da_stdev_time
da_anom.to_netcdf(path + out_fn)
toc = time.time() - tic
ic(toc)
