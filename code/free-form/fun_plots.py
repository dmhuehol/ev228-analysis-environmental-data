'''fun_plots
Functions to make various plots relevant for course activities and assignments.
'''
import sys

import cartopy.crs as ccrs
from icecream import ic
import matplotlib.pyplot as plt

def timeseries(
        in_df, in_x=None, out_path='', out_name='', color='#dc6b2b', 
        linewidth=2, in_title='', x_label='', x_lim=[], y_label=''):
    ''' Plot timeseries from 1D dataframe '''
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(in_x, in_df, color=color, linewidth=linewidth)
    plt.xlabel(x_label)
    plt.xlim(x_lim[0], x_lim[1])
    plt.ylabel(y_label)
    plt.title(in_title)
    plt.savefig(out_path + out_name, dpi=400)

def map(
        in_da, out_path='', out_name='', x_label='', y_label='', cb_label='', 
        title='', cmap='turbo',):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da['longitude']
    lats = in_da['latitude']

    image = plt.pcolormesh(lons, lats, in_da, cmap=cmap)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label(cb_label)
    plt.savefig(out_path + out_name, dpi=400)

def map_cartopy(
        in_da, out_path='', out_name='', cmap='turbo', in_title='', vmin=-1, 
        vmax=1):
    ''' Plot map from 2D DataArray with cartopy for grid '''
    fig = plt.figure()
    # ax = fig.add_subplot(111)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    # ax.stock_img()
    # gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
    #               linewidth=2, color='gray', alpha=0.5, linestyle='--')
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(
        lons, lats, in_da, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title(in_title)
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('standard deviation')
    plt.savefig(out_path + out_name, dpi=400)
