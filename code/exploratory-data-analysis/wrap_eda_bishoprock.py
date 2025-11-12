from icecream import ic
import os
import sys
import time

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

tic = time.time()
file_path = '/Users/danielhueholt/Data/ev228_data/station/Bishop-Rock.csv'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251106/'
out_filename = 'bishoprock.png'
df_data, df_yr = fi.import_csv_station(file_path, var='T_HMP', time_var='TIMESTAMP')
# df_data2, df_yr = fi.import_csv_station(file_path, var='T_HMP_2', time_var='TIMESTAMP')
# ic(df_data.corr(df_data2))
# sys.exit('STOP')

ic(
    df_data.mean(), df_data.std(), 
    df_data.max(), df_data.min())

plt.rcParams.update({'font.family': 'Figtree'})
#  'font.weight': normal, bold, heavy, light, ultrabold, ultralight
plt.rcParams.update({'font.weight': 'normal'})
plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots()
plt.plot(df_yr[0:60], df_data[0:60], color='r', lw=2)
plt.xlabel('time')
ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.tick_params(axis='x', labelrotation=45)
plt.xticks(fontsize=3)
# plt.xlim(2005, 2015)
plt.ylabel('deg C')
plt.title('Bishop Rock')
ax.spines[['right', 'top']].set_visible(False)
plt.savefig(out_path + out_filename, dpi=400) 
toc = time.time() - tic
print(toc)