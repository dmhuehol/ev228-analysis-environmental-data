from icecream import ic
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

file_path = '/Users/danielhueholt/Data/ev228_data/gridded/'
fn = 'era5_vegcover.nc'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251107/'
out_fn = 'testlisted.png'

ds = xr.open_dataset(file_path + fn)
da = np.squeeze(ds['cvh'])
l_colors = ['darkorange', 'gray', 'gray', 'mistyrose']
cmap = colors.ListedColormap(l_colors, name='from_list', N=4)

fig, ax = plt.subplots()
image = plt.pcolormesh(
    da.longitude, da.latitude, da.data, cmap=cmap)
cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
plt.savefig(out_path + out_fn, dpi=400)
