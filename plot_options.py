# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:33:57 2021
@author: Boateng(daniel.boateng@uni-tuebingen.de)
This script contains all the required specifications required for visualizing 
global simulation output or reanalysis dataset.Please contact the author for more information if necessary!
--------------------------------------------------------------
1. directories to input datasets and for output figure -(str)
2. setting projection, variable(eg. Temperature) and limit of dataset(must be the same for 
   positive and negative values) for the background plot: Projection must be 
   available from cartopy package (default is PlateCarre())
3. Defining titles of plots and output file names


"""
#importing packages 

import cartopy.crs as ccrs
import numpy as np



#setting paths to data and figure directory 

main_path = "C:/Users/Boateng/Desktop/education/AEG stuff/Master_Thesis/Modules/GCM-echam"          # model output path 
output_processed_path_ref = "C:/Users/Boateng/Desktop/education/AEG stuff/Master_Thesis/Modules/GCM-echam/e007_2_hpc-bw_e5w2.3_PI_t159l31.1d/output_processed"         # path to processed output for referenced data          
output_processed_path = "C:/Users/Boateng/Desktop/education/AEG stuff/Master_Thesis/Modules/GCM-echam/e009_hpc-bw_e5w2.3_LGM_t159l31.1d/output_processed"              # path to processed data    
data1_name = "1004_1017_mlterm.nc"                                    # file of monthly means 
data2_name = "1003_1017_mlterm.nc"                                    # file of monthly means referenced data
data3_name = None                                                     # file of annual means if needed
data4_name = None                                                     # file of annual means if needed for referenced data

plot_path = "C:/Users/Boateng/Desktop/education/AEG stuff/Master_Thesis/Modules/GCM-echam/e007_2_hpc-bw_e5w2.3_PI_t159l31.1d/plots"       # path for plots 


#setting projection, variable, plotting type and domain area for plotting 

projection = ccrs.PlateCarree()                                           # name of projection from cartopy                                                         # number of levels for colorbar scale 
variable = "Precipitation"                                            # variabe eg. "Precipitation" 
domain = "South America"                                                        # domin name (from plot utils) 
plotting_type = "Difference"                                                 # ["Average" or "Difference"] Specify the type of plot (whether long-term average or difference)                                      

#seting plot title and output file

if variable== "Temperature": 
    # limit of values (if not defined, the default in the plot functions will be used)
    if plotting_type == "Average":
        vmax = 30                                                             # maximu plotted
        vmin = -30                                                            # minimum plotted
        center = 0                                                            #center value on the color map
        levels = 30
        months = "January-June"        # Months to plot eg. "January-June" or "July-December"
        title_month_mean = "Temperature [e007_2(PI)] monthly mean"
        title_annual_mean = "Temperature [e007_2(PI)] annual mean"
        output_name_month_mean = "mont_mean_" + "_" + data1_name + "_" + domain+ "_" + variable                                                            # output name monthly mean
        output_name_annual_mean = "annual_mean_" + "_" + data1_name + "_" +data2_name + "_" + domain+ "_" + variable                                       # output name annual mean
   
    elif plotting_type == "Difference":
        vmax = 30                                                             # maximu plotted
        vmin = -30                                                           # minimum plotted
        center = 0                                                            #center value on the color map
        levels = 30
        months = "January-June"       # Months to plot eg. "January-June" or "July-December"
        title_month_diff = "Temperature Difference [e007_2(PI) - e009_(LGM)] monthly mean" 
        title_annual_diff = "Temperature Difference [e007_2(PI) - e009_(LGM)] annual mean"                                            # Title of plot for mothly mean and difference 
        output_name_month_diff = "mont_diff_"+ data1_name + "_" +data2_name + "_" + domain+ "_" + variable                                           # output name monthly difference 
        output_name_annual_diff = "annual_diff_" + data1_name + "_" + domain+ "_" + variable                    # output name annual difference
    else: 
        print("ERROR: define plotting type eg. Average or Difference")

    colorbar_unit = "deg C"                                                                                                      
    output_format = ".pdf"                                                                                                       # format of figure eg. tiff, svg, eps,pdf

                                                   
elif variable == "Precipitation":
    if plotting_type == "Average":
        vmax = 200                                                             # maximu plotted
        vmin = 0                                                            # minimum plotted
        spacing = 10
        ticks = np.arange(vmin, vmax+(2*spacing), spacing)                # colorbar tick values
        levels = len(ticks)
        months = "January-June"        # Months to plot eg. "January-June" or "July-December"
        title_month_mean = "Precipitation [e007_2(PI)] monthly mean"
        title_annual_mean = "Precipitation [e007_2(PI)] annual mean"
        output_name_month_mean = "mont_mean_"+ data1_name + "_" + domain+ "_" + variable                                            # output name monthly mean
        output_name_annual_mean = "annual_mean_"+ data1_name + "_" +data2_name + "_" + domain+ "_" + variable                                            # output name annual mean
    elif plotting_type == "Difference":
        vmax = 500                                                             # maximu plotted
        vmin = -500                                                            # minimum plotted
        center = 0                                                            #center value on the color map
        levels = 30  
        months = "January-June" 
        title_month_diff = "Precipitation Difference [e007_2(PI) - e009_(LGM)] monthly mean" 
        title_annual_diff = "Precipitation Difference [e007_2(PI) - e009_(LGM)] annual mean"                                                # Title of plot for mothly mean and difference 
        output_name_month_diff = "mont_diff_"+ data1_name + "_" +data2_name + "_" + domain+ "_" + variable                                           # output name monthly difference 
        output_name_annual_diff = "annual_diff_"+ data1_name + "_" + domain+ "_" + variable                      # output name annual difference
    else:
        print("ERROR: define plotting type eg. Average or Difference")

    colorbar_unit = "mm/month"                                      
    output_format = ".pdf"

else:
    print("ERROR: Define variable to be plotted well")


