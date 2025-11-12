from icecream import ic
import os
import sys

from matplotlib import font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats, odr

import fun_import as fi

font_path_local = '/Users/danielhueholt/Library/Fonts/'
font_path_coe_hpc = '/home/danielhueholt/fonts/'
if os.path.exists(font_path_local):
    for font in fm.findSystemFonts(font_path_local):
        fm.fontManager.addfont(font)
elif os.path.exists(font_path_coe_hpc):
    for font in fm.findSystemFonts(font_path_coe_hpc):
        fm.fontManager.addfont(font)

file_path = '/Users/danielhueholt/Data/ev228_data/station/KRDU_temp_188708-202508.csv'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251106/'
out_fn = 'rdu-linreg.png'
df_data, df_yr = fi.import_csv_station(file_path, var='metANN', time_var='YEAR')
ic(df_data, df_yr)
slope, intercept, r_value, p_value, std_err = stats.linregress(
    np.squeeze(df_yr), np.squeeze(df_data)
)
ic(slope, intercept, r_value, p_value, std_err)
r2 = r_value ** 2
ic(r2)


plt.rcParams.update({'font.family': 'Figtree'})
#  'font.weight': normal, bold, heavy, light, ultrabold, ultralight
plt.rcParams.update({'font.weight': 'normal'})
plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots()
plt.scatter(df_yr, df_data, color='r', lw=2)
plt.plot(
    df_yr, intercept + df_yr * slope, "--", color="darkblue", 
    label="linear regression", linewidth=)
plt.xlabel('year')
# plt.xlim(2005, 2015)
plt.ylabel('deg C')
plt.title('Raleigh-Durham Airport (KRDU) Annual Mean Temperature')
ax.spines[['right', 'top']].set_visible(False)
plt.savefig(out_path + out_fn, dpi=400)
ic(np.max(df_data))