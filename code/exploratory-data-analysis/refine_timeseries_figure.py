import numpy as np
import matplotlib.pyplot as plt

import fun_import as fi
import fun_plots as fp

path = '/Users/danielhueholt/Data/ev228_data/station/'
fn = 'ASM00094998_temp_194804-202508.csv'
out_path = '/Users/danielhueholt/Documents/Figures/ev228_fig/20251105/'
out_fn = 'eda_timeseries.png'

df_data, df_yr = fi.import_ghcn(file_path=path + fn, var='metANN')

print(df_data)
fp.timeseries(df_data, in_x=df_yr, out_path=out_path, out_name=out_fn)
