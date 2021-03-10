# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:54:05 2021

@author: Boateng
This script contains all the functions for computing the long-term annual means and monthly differences

1. loading data
2. extracting variables
3. converting units 
4. averaging for annual mean
5. annual and monthly difference
6. Function for generating the backgroud of plotting - projection, add boarderlines, coords formatter etc
"""
# importing packages 
import xarray as xr
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.colors as colors
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
from cartopy.mpl.ticker import (LatitudeLocator, LongitudeLocator) 
from cartopy.util import add_cyclic_point

#importing other in-built functions
from plot_options import *


#loading data from path 
data = xr.open_dataset(os.path.join(output_processed_path, data1_name))
data_ref = xr.open_dataset(os.path.join(output_processed_path_ref, data2_name))

if data3_name is not None:  # if annual long-term dataset is available instead of calculation 
    data_annual = xr.open_dataset(os.path.join(output_processed_path, data3_name))
    data_annual_ref = xr.open_dataset(os.path.join(output_processed_path_ref, data3_name))

#extracting variables from datasets 

# Temperature
if variable == "Temperature":
    data_temp = data["temp2"]
    
    # checking units and conversion 
    if data_temp.units != "deg C":
        data_temp = data_temp - 273.15
        data_temp.attrs["units"] = "deg C"   # changing units to deg C
    else:
        print(data_temp.units)
        
    data_ref_temp = data_ref["temp2"]
    
    # checking units and conversion 
    if data_ref_temp.units != "deg C":
        data_ref_temp = data_ref_temp - 273.15
        data_ref_temp.attrs["units"] = "deg C"  #changing the units to deg C
    else:
        print(data_ref_temp.units)
        
# Precipitation (Convective + large scale precipitation)     
   
elif variable == "Precipitation":
    data_aprl = data["aprl"] 
    data_prec = data_aprl + data["aprc"]    # total precipitation 
    data_ref_prec = data_ref["aprl"] + data_ref["aprc"]
    
    # checking units and convertion 
    if data_aprl.units != "mm/month":       #kg/ms²-->mm/month
        data_prec = data_prec *60*60*24*30     
        data_ref_prec = data_ref_prec *60*60*24*30
    else:
        print(data_aprl.units)
    
else:
    print ("source error : Define the variable for plotting")
    

#computation of annual means and monthly difference 

if variable == "Temperature":
    
    # calculating long-term average (annual mean)
    
    if data3_name is not None:  # if annual data is loaded...used that instead
        data_temp_ltmean = data_annual
        data_ref_temp_ltmean = data_annual_ref
        
    else:
        data_temp_ltmean = data_temp.mean(dim = "time")
        data_ref_temp_ltmean = data_ref_temp.mean(dim = "time")
    
   # calculating annual difference [data_ref - data] 
    data_temp_ltdiff = data_ref_temp_ltmean - data_temp_ltmean    # annual diff
    
    # calculating long-term monthly difference (monthly difference)
    data_temp["time"] = data_ref_temp.time                #passing the time from ref data to data 
    data_temp_mltdiff = data_ref_temp - data_temp
    
elif variable == "Precipitation":
    
    # calculating long-term average (annual mean)
    
    if data3_name is not None:  # if annual data is loaded...used that instead
        data_temp_ltmean = data_annual
        data_ref_temp_ltmean = data_annual_ref
        
    else:
        data_prec_ltmean = data_prec.mean(dim = "time")
        data_ref_prec_ltmean = data_ref_prec.mean(dim = "time")
    
   # calculating annual difference [data_ref - data] 
    data_prec_ltdiff = data_ref_prec_ltmean - data_prec_ltmean    # annual diff
    
    # calculating long-term monthly difference (monthly difference)
    data_prec["time"] = data_ref_prec.time                #passing the time from ref data to data 
    data_prec_mltdiff = data_ref_prec - data_prec
    
# Generating function for the plotting background and domain size

def plot_background(p, domain=None):
    """
    This funtion defines the plotting domain and also specifies the background. It requires 
    the plot handle from xarray.plot.imshow and other optional arguments 
    Parameters
    -------------

    p: TYPE: plot handle 
    DESCRIPTION: the plot handle after plotting with xarray.plot.imshow
    
    domian = TYPE:str 
    DESCRIPTION: defines the domain size, eg. "Europe", "Asia", "Africa"
                  "South America", "Alaska", "Tibet Plateau" or "Himalaya", "Eurosia",
                  "New Zealand", default: global
    """
    p.axes.set_global()                    # setting global axis 
    p.axes.coastlines(resolution = "50m")  # add coastlines outlines to the current axis
    p.axes.add_feature(cfeature.BORDERS, color="black", linewidth = 0.5) #adding country boarder lines
    
    #setting domain size
    if domain is not None: 
        if domain == "Europe":   # Europe
            minLon = -15
            maxLon = 40
            minLat = 35
            maxLat = 65
        elif domain == "South America":   # South America
            minLon = -85
            maxLon = -30
            minLat = -60
            maxLat = 15
        elif domain == "Tibetan Plateau" or domain == "Himalayas":  #Tibet Plateau/Himalayas
            minLon = 40
            maxLon = 120
            minLat = 0
            maxLat = 60
        elif domain == "Eurasia":        # Eurasia
            minLon = -18
            maxLon = 164
            minLat = 20
            maxLat = 77
        elif domain == "Cascades":  # Cascades
            minLon = -129
            maxLon = -120
            minLat = 45
            maxLat = 52
        elif domain == "Alaska":  # Alaska
            minLon = -165
            maxLon = -125
            minLat = 52
            maxLat = 68
        elif domain == "Africa":  # Africa
            minLon = -30
            maxLon = 55
            minLat = -35
            maxLat = 40
        elif domain == "New Zealand":  # New Zealand 
            minLon = 165
            maxLon = 180
            minLat = -47
            maxLat = -34
        elif domain == "Olympic Mnts":  # Olympic Mnt's
            minLon = -126
            maxLon = -118
            minLat = 43
            maxLat = 52
        else:
            print("ERROR: invalid geographical domain passed in options")
        p.axes.set_extent([minLon, maxLon, minLat, maxLat], ccrs.PlateCarree())
    if domain is None: 
        p.axes.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
        
    # adding gridlines    
    gl= p.axes.gridlines(crs = ccrs.PlateCarree(), draw_labels = True, linewidth = 1,
                     color = "gray", linestyle = "--")
    
    gl.xlabels_top = False                  # labesl at top
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER     # axis formatter
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {"size": 15, "color": "black", "weight": "bold"}   #axis style 
    gl.ylabel_style = {"color": "black", "size": 15, "weight": "bold"}
    
    #return p
    
class MidpointNormalize(colors.Normalize):
    """
    At the moment its a bug to use divergence colormap and set the colorbar range midpoint 
    to zero if both vmax and vmin has different magnitude. This might be possible in 
    future development in matplotlib through colors.offsetNorm(). This class was original developed 
    by Joe Kingto and modified by Daniel Boateng. It sets the divergence color bar to a scale of 0-1 by dividing the midpoint to 0.5
    Use this class at your own risk since its non-standard practice for quantitative data.
    """
    
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))      
            
    
norm = MidpointNormalize(midpoint = center)   # must be imported to plotting functions
    
    







   

