'''fun_import
Functions to import various datasets relevant for EV228 course at Colorado 
College.
'''
import sys

from icecream import ic
import pandas as pd
import xarray as xr


def import_ghcn(file_path='', var=''):
    ''' Import GHCN weather station data '''
    df = pd.read_csv(file_path)
    df_data = df[var]
    df_yr = df['YEAR']

    return df_data, df_yr

def import_era5(file_path='', var=''):
    ''' Import ERA5 gridded data '''
    ds = xr.open_dataset(file_path)
    da = ds[var]

    return da