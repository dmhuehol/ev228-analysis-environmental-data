'''wrap_lr_station
Demonstrate linear regression model and trendline plotting on station data from
Global Historical Climatology Network.
'''
import os
import sys

from icecream import ic
from matplotlib import font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import fun_import as fi

font_path_local = '/Users/danielhueholt/Library/Fonts/'
if os.path.exists(font_path_local):
    for font in fm.findSystemFonts(font_path_local):
        fm.fontManager.addfont(font)

file_path = '/Users/danielhueholt/Data/ev228_data/station/KRDU_temp_188708-202508.csv'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251113/'
out_fn = 'rdu-linreg.png'

df_data, df_yr = fi.import_csv_station(
    file_path, var='metANN', time_var='YEAR')
slope, intercept, r_value, p_value, std_err = stats.linregress(
    np.squeeze(df_yr), np.squeeze(df_data))
ic(slope, intercept, r_value, p_value, std_err)
r2 = r_value ** 2
ic(r2)
trendline = intercept + df_yr * slope

plt.rcParams.update({'font.family': 'Figtree'})
#  'font.weight': normal, bold, heavy, light, ultrabold, ultralight
plt.rcParams.update({'font.weight': 'normal'})
plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots()
plt.scatter(df_yr, df_data, color='r', lw=2)
plt.plot(
    df_yr, trendline, "--", color="darkblue", label="linear regression", 
    linewidth=2)
plt.xlabel('year')
plt.ylabel('deg C')
plt.title('Raleigh-Durham Airport (KRDU) Annual Mean Temperature')
ax.spines[['right', 'top']].set_visible(False)
plt.savefig(out_path + out_fn, dpi=400)