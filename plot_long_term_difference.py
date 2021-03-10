# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:34:24 2021

@author: Boateng(daniel.boateng@uni-tuebingen.de)
This script generates both annual and monthly long-term difference plot between two geologic age simulations or specific time range.
-----------------------------------------------------

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


def plot_annual_diff(variable, data, title=None , vmin=None, vmax=None , levels=None, 
                     center=None, output_format=None, projection=None, domain = None, norm=None ):
    """
    This function generates the plot for long-term annual difference of annual means between ref data[eg. LGM] and data [eg. PI] of a certian variable
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
    domain : str, optional eg. Africa, Asia, Europe
    norm : Normalize function for divergence colormap, optional

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
    
    # plotting using imshow from xarray and other specifications
    
    if variable == "Temperature":
        if all(parameter is not None for parameter in [vmin, vmax, levels, center, norm]):    # if all these params are not None 
            p = data.plot.imshow(ax =ax, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax, center=center, levels=levels, transform = ccrs.PlateCarree(), 
                                 norm=norm, cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "horizontal", "shrink": 0.6, "format": "%.0f"},
                                 extend= "neither")
        else:
            p = data.plot.imshow(ax=ax, cmap=plt.cm.seismic, vmin=-30, vmax=30, center=0, levels=30, transform = ccrs.PlateCarree(),
                                 cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "horizontal", "shrink": 0.6,
                                               "format": "%.0f"})
            
        p.colorbar.set_label(label="Temperature" + " [" + colorbar_unit + "]", size = 20)  
        p.colorbar.ax.tick_params(labelsize = 20)
            
        if domain is not None:
            plot_background(p,domain=domain)
        elif domain is None:
            plot_background(p, domain)
        else:
            print("ERROR: define the domian area properly or check the plot utils for the right names")
            
    elif variable == "Precipitation":
        if all(parameter is not None for parameter in [vmin, vmax, levels, center, norm]):
            p = data.plot.imshow(ax =ax, cmap=plt.cm.seismic_r, vmin=vmin, vmax=vmax, levels=levels, center= center, transform = ccrs.PlateCarree(), 
                                 cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "horizontal", "shrink": 0.6, "format": "%.0f"},
                                 extend= "neither", norm= norm)
        else:
            p = data.plot.imshow(ax=ax, cmap=plt.cm.seismic_r, vmin=-1000, vmax=1000, levels=30, center = 0, transform = ccrs.PlateCarree(),
                                 cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "horizontal", "shrink": 0.6,
                                               "format": "%.0f"}, extend= "neither", norm = norm)
            
        p.colorbar.set_label(label="Precipitation" + " [" + colorbar_unit + "]", size = 20)  
        p.colorbar.ax.tick_params(labelsize = 20)
            
        if domain is not None:
            plot_background(p,domain=domain)
        elif domain is None:
            plot_background(p, domain)
        else:
            print("ERROR: define the domian area properly or check the plot utils for the right names")
            
    else:
        print("ERROR: define variable properly or your variable has not yet been implemented")
    if title is not None:
        plt.title(title_annual_diff, fontsize= 20, weight = "bold")
    elif title is None: 
        plt.title("Long-term annual mean")
    else:
        print("ERROR: check the data type of the defined title")
        
    if output_format is not None:
        plt.savefig(os.path.join(plot_path, output_name_annual_diff + output_format), bbox_inches="tight")
    elif output_format is None:
        plt.savefig(os.path.join(plot_path, output_name_annual_diff), format="pdf", bbox_inches="tight")
        



def plot_monthly_diff(variable, data, months, title=None , vmin=None, vmax=None , levels=None, 
                     center=None, output_format=None, projection=None, domain = None, norm=None):
    """
    This function generates the plot for long-term monthly difference of a certian variable between two datasets
    The differences are calculated in the plot_utils functions
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
    domain : str, optional eg. Africa, Asia, Europe
    norm : Normalize function for divergence colormap, optional
    months: TYPE = Str
            DESCRIPTION. Define the months to be plotted eg. January-June or July-December
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
    
    # creating subplots for six months
    
    fig, ((ax1,ax2),(ax3,ax4), (ax5,ax6)) = plt.subplots(3, 2, sharex = True, sharey = True,figsize =(10,15),  
                                                         subplot_kw={"projection": projection})    
    #plt.subplots_adjust(left=0.05, right=0.85, top=0.94, bottom=0.06, wspace=0.02)
    
    axes = [ax1,ax2,ax3,ax4,ax5,ax6]   # axes for all subplots 
    
    if months == "January-June":
        months_num = [0, 1, 2, 3, 4, 5]
        mnames = ["January", "February", "March", "April", "May", "June"]
    elif months == "July-December":
        months_num = [6, 7, 8, 9, 10, 11]
        mnames = ["July", "August", "September", "October","November", "December"]
    else:
        print("EEROR: define months for subplots")
    
    for i in range(len(months_num)):
        cbar_ax = fig.add_axes([0.85, 0.30, 0.02, 0.5])   # axis for subplot colorbar # left, bottom, width, height
        
        if variable == "Temperature":
            if axes[i]==ax5:
                
                if all(parameter is not None for parameter in [vmin, vmax, levels, center, norm]):    # if all these params are not None 
                    p = data[months_num[i]].plot.imshow(ax =axes[i], cmap=plt.cm.seismic, vmin=vmin, vmax=vmax, center=center, levels=levels, transform = ccrs.PlateCarree(), 
                                         norm=norm, cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "vertical", "shrink": 0.3, "format": "%.0f"},
                                         extend= "neither", add_colorbar = True, cbar_ax = cbar_ax)
                else:
                    p = data[months_num[i]].plot.imshow(ax=axes[i], cmap=plt.cm.seismic, vmin=vmin, vmax=vmax, center=0, levels=30, transform = ccrs.PlateCarree(),
                                         cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "vertical", "shrink": 0.3,
                                                       "format": "%.0f"}, add_colorbar = True, cbar_ax = cbar_ax, extend = "neither")
                p.colorbar.set_label(label="Temperature" + " [" + colorbar_unit + "]", size = 20)  
                p.colorbar.ax.tick_params(labelsize = 20)
                    
                if domain is not None:
                    plot_background(p,domain=domain)
                elif domain is None:
                    plot_background(p, domain)
                else:
                    print("ERROR: define the domian area properly or check the plot utils for the right names")
                    
                axes[i].set_title(mnames[i], fontdict= {"fontsize": 20, "fontweight":"bold"})     #seting subplot title 
                    
            # for other plots without color bar (limits are same so similar colorbar for all months)        
            else:
                if all(parameter is not None for parameter in [vmin, vmax, levels, center, norm]):    # if all these params are not None 
                    p = data[months_num[i]].plot.imshow(ax =axes[i], cmap=plt.cm.seismic, vmin=vmin, vmax=vmax, center=center, levels=levels, transform = ccrs.PlateCarree(), 
                                         norm=norm, extend= "neither", add_colorbar= False)
                
                else:
                    p = data[months_num[i]].plot.imshow(ax=axes[i], cmap=plt.cm.seismics, vmin=-30, vmax=30, center=0, levels=30, transform = ccrs.PlateCarree(),
                                         norm=norm, extend = "neither", add_colorbar = False)
                
                
                if domain is not None:
                    plot_background(p,domain=domain)
                elif domain is None:
                    plot_background(p, domain)
                else:
                    print("ERROR: define the domian area properly or check the plot utils for the right names")
                    
                axes[i].set_title(mnames[i], fontdict= {"fontsize": 20, "fontweight":"bold"})   # setting subplot title
                
        elif variable == "Precipitation":
            if axes[i]==ax5:
                
                if all(parameter is not None for parameter in [vmin, vmax, levels, center, norm]):    # if all these params are not None 
                    p = data[months_num[i]].plot.imshow(ax =axes[i], cmap=plt.cm.seismic_r, vmin=vmin, vmax=vmax, levels=levels, center = center, transform = ccrs.PlateCarree(), 
                                         cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "vertical", "shrink": 0.3, "format": "%.0f"},
                                         extend= "neither", add_colorbar = True, cbar_ax = cbar_ax, norm = norm)
                else:
                    p = data[months_num[i]].plot.imshow(ax=axes[i], cmap=plt.cm.seismic_r, vmin=-1000, vmax=1000, levels=30, center = 0, transform = ccrs.PlateCarree(),
                                         cbar_kwargs= {"pad":0.1, "drawedges": True, "orientation": "vertical", "shrink": 0.3,
                                                       "format": "%.0f"}, add_colorbar = True, cbar_ax = cbar_ax, extend = "neither", norm = norm)
                p.colorbar.set_label(label="Precipitation" + " [" + colorbar_unit + "]", size = 20)  
                p.colorbar.ax.tick_params(labelsize = 20)
                    
                if domain is not None:
                    plot_background(p,domain=domain)
                elif domain is None:
                    plot_background(p, domain)
                else:
                    print("ERROR: define the domian area properly or check the plot utils for the right names")
                    
                axes[i].set_title(mnames[i], fontdict= {"fontsize": 20, "fontweight":"bold"})     #seting subplot title 
                    
            # for other plots without color bar (limits are same so similar colorbar for all months)        
            else:
                if all(parameter is not None for parameter in [vmin, vmax, levels, center,norm]):    # if all these params are not None 
                    p = data[months_num[i]].plot.imshow(ax =axes[i], cmap=plt.cm.seismic_r, vmin=vmin, vmax=vmax, levels=levels, center= center, transform = ccrs.PlateCarree(), 
                                         extend= "neither", add_colorbar= False, norm = norm)
                
                else:
                    p = data[months_num[i]].plot.imshow(ax=axes[i], cmap=plt.cm.seismic_r, vmin=0, vmax=1000, levels=30, center = 0, transform = ccrs.PlateCarree(),
                                         extend = "neither", add_colorbar = False, norm = norm)
                
                
                if domain is not None:
                    plot_background(p,domain=domain)
                elif domain is None:
                    plot_background(p, domain)
                else:
                    print("ERROR: define the domian area properly or check the plot utils for the right names")
                    
                axes[i].set_title(mnames[i], fontdict= {"fontsize": 20, "fontweight":"bold"})   # setting subplot title
                
        else:
            print("ERROR: define variable properly or your variable has not yet been implemneted")
            
        
        
    if title is not None:
        fig.suptitle(title_month_diff, fontsize= 20, weight = "bold")
    elif title is None: 
        fig.suptitle("Long-term monthy mean")
    else:
        print("ERROR: check the data type of the defined title")
        
        
    fig.canvas.draw()   # the only way to apply tight_layout to matplotlib and cartopy is to apply canvas firt 
    fig.tight_layout() 
    plt.subplots_adjust(left=0.05, right=0.85, top=0.94, bottom=0.06, wspace=0.02)   # subplots_adjust has effect on the figure after tight layout 
    
    if output_format is not None:
        plt.savefig(os.path.join(plot_path, output_name_month_diff + "_" + months + output_format), bbox_inches="tight")
    elif output_format is None:
        plt.savefig(os.path.join(plot_path, output_name_month_diff + "_" + months), format="pdf", bbox_inches="tight")
        
        
        
#**********************************************************************************************************       

# define a customize argument_paser for calling the function with command lines options

# You have to pass the right data (this will be fixed with argparser in future)
if variable == "Temperature":
    plot_annual_diff(variable, data=data_temp_ltdiff, title=title_annual_diff , vmin=vmin, vmax=vmax , levels=levels, 
                         center=center, output_format=output_format, projection=projection, domain=domain, norm= norm) 
    plot_monthly_diff(variable, data=data_temp_mltdiff, months= months, title=title_month_diff , vmin=vmin, vmax=vmax , levels=levels, 
                         center=center, output_format=output_format, projection=projection, domain=domain, norm= norm)
elif variable == "Precipitation": 
    plot_annual_diff(variable, data=data_prec_ltdiff, title=title_annual_diff , vmin=vmin, vmax=vmax , levels=levels, 
                        center=center, output_format=output_format, projection=projection, domain=domain, norm= norm)
    plot_monthly_diff(variable, data=data_prec_mltdiff, months= months, title=title_month_diff , vmin=vmin, vmax=vmax , levels=levels, 
                         center=center, output_format=output_format, projection=projection, domain=domain, norm= norm)
       
         