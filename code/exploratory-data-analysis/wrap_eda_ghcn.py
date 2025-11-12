from icecream import ic
import os
import sys

from matplotlib import font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
df_data, df_yr = fi.import_csv_station(file_path, var='metANN', time_var='YEAR')
ic(df_data, df_yr)

plt.rcParams.update({'font.family': 'Figtree'})
#  'font.weight': normal, bold, heavy, light, ultrabold, ultralight
plt.rcParams.update({'font.weight': 'normal'})
plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots()
plt.plot(df_yr, df_data, color='r', lw=2)
plt.xlabel('year')
plt.xlim(2005, 2015)
plt.ylabel('deg C')
plt.title('Raleigh-Durham Airport (KRDU) Annual Mean Temperature')
ax.spines[['right', 'top']].set_visible(False)
plt.show()
ic(np.max(df_data))