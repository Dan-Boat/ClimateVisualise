# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:35:07 2021

@author: Boateng(daniel.boateng@uni-tuebingen.de)
This script generates both annual and monthly long-term mean plot 
------------------------------------------------------------

"""
# importing packages 

import xarray as xr
import os
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
from cartopy.mpl.ticker import (LatitudeLocator, LongitudeLocator) 
from cartopy.util import add_cyclic_point
import calendar


#importing other in-built functions
from plot_options import *
from plot_utils import *


def plot_annual_mean(variable, data, title=None , vmin=None, vmax=None , levels=None, 
                     center=None, output_format=None, projection=None):
    """
    This function generates the plot for long-term annual mean of a certian variable
    Parameters
    ----------
    variable : TYPE = Str
        DESCRIPTION: Variable to be ploted (imported from options)
    data : TYPE = dataArray
        DESCRIPTION: data to be ploted (imported from plot utils)
    title : TYPE = Str, optional
        DESCRIPTION: Title of the figure imported from plot options if provided, optional 
    vmin : TYPE = float, optional
        DESCRIPTION. minimum value limit of the variable to be ploted 
    vmax : TYPE = float, optional
        DESCRIPTION. maximum value limit of the variable to be ploted
    levels : TYPE,  float, optional
        DESCRIPTION. the number of levels for colorbar scale 
    center : TYPE =  float, optional
        DESCRIPTION. center value if data contains positive and negative values 
    output_format : TYPE = Str, optional
        DESCRIPTION. format to save the plotting figure eg. pdf, png, svg, eps

    Returns
    -------
    Figure.

    """
    
    if projection is not None:                # setting projection for plot
        projection = projection
    elif projection is None:
        projection = ccrs.PlateCarree()
    else:
        print("ERROR: defines the right projection from cartopy")
    
    fig, ax = plt.subplots(1, 1, sharex=False, figsize= (15, 13), 
                           subplot_kw= {"projection":projection})
    
    if variable == "Temperature":
        if all(parameter is not None for parameter in [vmin, vmax, levels, center]):
            p = data.plot.imshow(ax =ax, cmap=plt.cm.RdBu_r, vmin=vmin, vmax=vmax, center=center, levels=levels, transform = ccrs.PlateCarree(), 
                                 cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "horizontal", "shrink": 0.75, "format": "%.0f"})
        else:
            p = dataset.plot.imshow(ax=ax, cmap=plt.cm.RdBu_r, vmin=vmin, vmax=vmax, center=0, levels=30, transform = ccrs.PlateCarree(),
                                 cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "horizontal", "shrink": 0.75,
                                               "format": "%.0f"})
            
            p.colorbar.set_label(label="Temperature" + " [" + colorbar_unit + "]", size = 15, 
                                 weight = "bold")  
            p.colorbar.ax.tick_params(labelsize = 20)
            plot_background(p)
            
    elif variable == "Precipitation":
        if all(parameter is not None for parameter in [vmin, vmax, levels, center]):
            p = data.plot.imshow(ax =ax, cmap=plt.cm.Blues, vmin=vmin, vmax=vmax, levels=levels, transform = ccrs.PlateCarree(), 
                                 cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "horizontal", "shrink": 0.75, "format": "%.0f"})
        else:
            p = dataset.plot.imshow(ax=ax, cmap=plt.cm.RdBu_r, vmin=0, vmax=vmax, levels=30, transform = ccrs.PlateCarree(),
                                 cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "horizontal", "shrink": 0.75,
                                               "format": "%.0f"})
            
            p.colorbar.set_label(label="Precipitation" + " [" + colorbar_unit + "]", size = 15, 
                                 weight = "bold")  
            p.colorbar.ax.tick_params(labelsize = 20)
            plot_background(p)
    else:
        print("ERROR: define variable properly or your variable has not yet been implemented")
    if title is not None:
        plt.title(title_annual_mean, fontsize= 20, weight = "bold")
    elif title is None: 
        plt.title("Long-term annual mean")
    else:
        print("ERROR: check the data type of the defined title")
    plt.savefig(os.path.join(plot_path, output_name_annual_mean + output_format))
    
        
         