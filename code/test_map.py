'''test_map
Test map plots for in-class activity in EV228 at Colorado College.
'''

from icecream import ic
import os
import sys

from matplotlib import font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd

import fun_import as fi
import fun_plots as fp

font_path_local = '/Users/danielhueholt/Library/Fonts/'
font_path_coe_hpc = '/home/danielhueholt/fonts/'
if os.path.exists(font_path_local):
    for font in fm.findSystemFonts(font_path_local):
        fm.fontManager.addfont(font)
elif os.path.exists(font_path_coe_hpc):
    for font in fm.findSystemFonts(font_path_coe_hpc):
        fm.fontManager.addfont(font)

#  Inputs
file_path = '/Users/danielhueholt/Data/ev228_data/gridded/era5_t2m_1997-2025.nc'
fig_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251031/'
fig_name = 'era5_timemn.png'
data_var = 't2m'

da_t2m = fi.import_era5(file_path, var=data_var)
da_t2m_timemn = da_t2m.mean(dim='valid_time')

fp.map(da_t2m_timemn, fig_path, fig_name)