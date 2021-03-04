# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:33:57 2021
@author: Boateng(daniel.boateng@uni-tuebingen.de)
This script contains all the required specifications required for visualizing 
global simulation output or reanalysis dataset.Please contact the author for more information if necessary
--------------------------------------------------------------
1. directories to input datasets and for output figure -(str)
2. setting projection, variable(eg. Temperature) and limit of dataset(must be the same for 
   positive and negative values) for the background plot: Projection must be 
   available from cartopy package (default is PlateCarre())
3. Defining titles of plots and output file names


"""
#importing packages 

import cartopy.crs as ccrs


#setting paths to data and figure directory 

main_path = "C:/Users/Boateng/Desktop/education/AEG stuff/Master_Thesis/Modules/GCM-echam"          # model output path 
output_processed_path = "C:/Users/Boateng/Desktop/education/AEG stuff/Master_Thesis/Modules/GCM-echam/e007_2_hpc-bw_e5w2.3_PI_t159l31.1d/output_processed"                    # path to processed data
output_processed_path_ref = "C:/Users/Boateng/Desktop/education/AEG stuff/Master_Thesis/Modules/GCM-echam/e009_hpc-bw_e5w2.3_LGM_t159l31.1d/output_processed"                 # path to processed output for referenced data
data1_name = "1003_1017_mlterm.nc"                                    # file of monthly means 
data2_name = "1004_1017_mlterm.nc"                                    # file of monthly means referenced data
data3_name = None                                                     # file of annual means if needed
data4_name = None                                                     # file of annual means if needed for referenced data

plot_path = "C:/Users/Boateng/Desktop/education/AEG stuff/Master_Thesis/Modules/GCM-echam/e007_2_hpc-bw_e5w2.3_PI_t159l31.1d/plots" # path for plots 


#setting projection and limit of values (if not defined, the default in the plot functions will be used)

projection = ccrs.PlateCarree()                                                       # name of projection from cartopy
vmax = 10                                                             # maximu plotted
vmin = -10                                                            # minimum plotted
center = 0                                                            #center value on the color map
levels = 30                                                           # number of levels for colorbar scale 
variable = "Temperature"                                              # variabe eg. "Precipitation" 

#seting plot title and output file

if variable== "Temperature": 
    title_month_diff = "Temperature Difference [e009_(LGM)- e007_2(PI)] monthly mean" 
    title_annual_diff = "Temperature Difference [e009_(LGM)- e007_2(PI)] annual mean"                                                # Title of plot for mothly mean and difference 
    title_month_mean = "Temperature [e007_2(PI)] monthly mean"
    title_annual_mean = "Temperature [e007_2(PI)] annual mean"
    output_name_month_diff = "mont_diff"+ data1_name + "_" +data2_name + "_" + variable                                          # output name monthly difference 
    output_name_month_mean = "mont_mean"+ data1_name + "_" + variable                                            # output name monthly mean
    output_name_annual_mean = "annual_diff"+ data1_name + "_" +data2_name + "_" + variable                                           # output name annual mean
    output_name_annual_diff = "annual_mean"+ data1_name + "_" + variable 
    colorbar_unit = "deg C"                                        # output name annual difference
    output_format = ".pdf" 

                                                   # format of figure eg. tiff, svg, eps,pdf
elif variable == "Precipitation":
    title_month_diff = "Precipitation Difference [e009_(LGM)- e007_2(PI)] monthly mean" 
    title_annual_diff = "Precipitation Difference [e009_(LGM)- e007_2(PI)] annual mean"                                                # Title of plot for mothly mean and difference 
    title_month_mean = "Precipitation [e007_2(PI)] monthly mean"
    title_annual_mean = "Precipitation [e007_2(PI)] annual mean"
    output_name_month_diff = "mont_diff"+ data1_name + "_" +data2_name + "_" + variable                                          # output name monthly difference 
    output_name_month_mean = "mont_mean"+ data1_name + "_" + variable                                            # output name monthly mean
    output_name_annual_mean = "annual_diff"+ data1_name + "_" +data2_name + "_" + variable                                           # output name annual mean
    output_name_annual_diff = "annual_mean"+ data1_name + "_" + variable 
    colorbar_unit = "mm/month"                                      # output name annual difference
    output_format = ".pdf"

else:
    print("ERROR: Define variable to be plotted well")


