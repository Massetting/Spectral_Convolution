# =============================================================================
# =============================================================================
#                          SPECTRAL CONVOLUTION


# # author: Andrea Massetti
# # email: andrea.massetti@gmail.com
# # Version: 0.1
# # tested: python 3.6
# # Contact if you need help.



#Hyperspectral to multi-spectral filter.
#
# Loads the spectral signatures and the bands' RSR and convolves. 
# 
# The convolution cuts at fwhm the bands' RSR.
# 
# Commented out there is some plotting.
# 
# Note. Due to relative paths, the script should be ran from the git main folder.
# Note. The script does not export the results as this was a one timer and only meant to give the resuts that I wanted. 
# =============================================================================

import methods
import os

paths={
"TM5": os.path.join("Band_RSR","TM_5.csv"),
"TM7": os.path.join("Band_RSR","TM_7.csv"),

"ETM5":os.path.join("Band_RSR","ETM_5.csv"),
"ETM7":os.path.join("Band_RSR","ETM_7.csv"),

"OLI1":os.path.join("Band_RSR","OLI_swir1.csv"),
"OLI2":os.path.join("Band_RSR","OLI_swir2.csv"),

"MSI1":os.path.join("Band_RSR","MSI_B11.csv"),
"MSI2":os.path.join("Band_RSR","MSI_B12.csv")}

bands = {}
for i,k in paths.items():
    bands[i] = methods.load_band(k)
bands_fwhm={}
for i, k in bands.items():
    bands_fwhm[i]=methods.fwhm(k)
spec_signs = [f for f in os.listdir(r"Hyper_samples{}".format(os.path.sep)) if f.endswith(".csv")]
spec_signn = {}
labels = {}
for gn in spec_signs:
    name = gn.split(".")[0]
    pth_sample = os.path.join("Hyper_samples",gn)
    if gn.split("_")[0] != "Canopy" and gn.split("_")[0]!="Grass" and gn.split("_")[0]!="Litter":
        spec_signn[name] = methods.load_band(pth_sample)
    else:
        band=methods.load_band(pth_sample)
        band[:,1:] = band[:,1:]/100
        spec_signn[name] = band
        
    with open(pth_sample,"r") as dummy:
        
        label_line = dummy.read().split("\n")[0]
        labels[name] = [f for f in label_line.split(",")]

final = {}
for name, spec in spec_signn.items():
    convs = {}
    for i, band in bands_fwhm.items():
        convs[i] = methods.convolve(band,spec)
    final[name] = convs    



# =============================================================================
# PLOT the PINE
#    
#    
# fig2,ay=methods.open_figure(1,1)
# ay.scatter([final["CBI"]["ETM5"][0],final["CBI"]["ETM5"][2],final["CBI"]["ETM5"][4],final["CBI"]["ETM5"][6],final["CBI"]["ETM5"][8],final["CBI"]["ETM5"][10],final["CBI"]["ETM5"][12],final["CBI"]["ETM5"][14]], [final["CBI"]["ETM7"][0],final["CBI"]["ETM7"][2],final["CBI"]["ETM7"][4],final["CBI"]["ETM7"][6],final["CBI"]["ETM7"][8],final["CBI"]["ETM7"][10],final["CBI"]["ETM7"][12],final["CBI"]["ETM7"][14]], marker="s",label="Enhanced Thematic Mapper" )
# ay.scatter([final["CBI"]["TM5"][0],final["CBI"]["TM5"][2],final["CBI"]["TM5"][4],final["CBI"]["TM5"][6],final["CBI"]["TM5"][8],final["CBI"]["TM5"][10],final["CBI"]["TM5"][12],final["CBI"]["TM5"][14]], [final["CBI"]["TM7"][0],final["CBI"]["TM7"][2],final["CBI"]["TM7"][4],final["CBI"]["TM7"][6],final["CBI"]["TM7"][8],final["CBI"]["TM7"][10],final["CBI"]["TM7"][12],final["CBI"]["TM7"][14]], marker="^",label ="Thematic Mapper")
# ay.scatter([final["CBI"]["MSI1"][0],final["CBI"]["MSI1"][2],final["CBI"]["MSI1"][4],final["CBI"]["MSI1"][6],final["CBI"]["MSI1"][8],final["CBI"]["MSI1"][10],final["CBI"]["MSI1"][12],final["CBI"]["MSI1"][14]], [final["CBI"]["MSI2"][0],final["CBI"]["MSI2"][2],final["CBI"]["MSI2"][4],final["CBI"]["MSI2"][6],final["CBI"]["MSI2"][8],final["CBI"]["MSI2"][10],final["CBI"]["MSI2"][12],final["CBI"]["MSI2"][14]], marker=">",label ="MultiSpectral Instrument")
# ay.scatter([final["CBI"]["OLI1"][0],final["CBI"]["OLI1"][2],final["CBI"]["OLI1"][4],final["CBI"]["OLI1"][6],final["CBI"]["OLI1"][8],final["CBI"]["OLI1"][10],final["CBI"]["OLI1"][12],final["CBI"]["OLI1"][14]], [final["CBI"]["OLI2"][0],final["CBI"]["OLI2"][2],final["CBI"]["OLI2"][4],final["CBI"]["OLI2"][6],final["CBI"]["OLI2"][8],final["CBI"]["OLI2"][10],final["CBI"]["OLI2"][12],final["CBI"]["OLI2"][14]], marker="<",label ="Operational Land Imager")
# x=np.arange(8,15)/100
# y=x*0.78-0.0280
# ay.plot(x,y,"g-",label="Dummy Vege line \n y=0.78x+0.028")
# 
# ay.text(final["CBI"]["ETM5"][0],final["CBI"]["ETM7"][0],"CBI_3")
# ay.text(final["CBI"]["ETM5"][2],final["CBI"]["ETM7"][2],"CBI_2.95")
# ay.text(final["CBI"]["ETM5"][4],final["CBI"]["ETM7"][4],"CBI_2.9")
# ay.text(final["CBI"]["ETM5"][6],final["CBI"]["ETM7"][6],"CBI_2.85")
# ay.text(final["CBI"]["ETM5"][8],final["CBI"]["ETM7"][8],"CBI_2.8")
# ay.text(final["CBI"]["ETM5"][10],final["CBI"]["ETM7"][10],"CBI_2.75")
# ay.text(final["CBI"]["ETM5"][12],final["CBI"]["ETM7"][12],"CBI_2.7")
# ay.text(final["CBI"]["ETM5"][14],final["CBI"]["ETM7"][14],"CBI_2.65")
# 
# 
# ay.legend()
# 
# =============================================================================



# =============================================================================
# PLOT VICTORIA
    
    
# fig,ax=methods.open_figure(1,1)
# #ax.scatter(final["Canopy_cont"]["TM5"],final["Canopy_cont"]["TM7"],color="g",marker="^",label="Canopy control")
# 
# for a,f in enumerate(final["Grass_cont"]["TM5"]):
#     ax.text(final["Grass_cont"]["TM5"][a],final["Grass_cont"]["TM7"][a],labels["Grass_cont"][a+1])
#     
# ax.scatter(final["Grass_cont"]["TM5"],final["Grass_cont"]["TM7"],color="g",marker=".",label="Grass control")
# #ax.scatter(final["Litter_cont"]["TM5"],final["Litter_cont"]["TM7"],color="g",marker="s",label="Litter control")
# 
# #ax.scatter(final["Canopy_low"]["TM5"],final["Canopy_low"]["TM7"],color="y",marker="^",label="Canopy low")
# for a,f in enumerate(final["Grass_low"]["TM5"]):
#     ax.text(final["Grass_low"]["TM5"][a],final["Grass_low"]["TM7"][a],labels["Grass_low"][a+1])
# 
# ax.scatter(final["Grass_low"]["TM5"],final["Grass_low"]["TM7"],color="y",marker=".",label="Grass low")
# #ax.scatter(final["Litter_low"]["TM5"],final["Litter_low"]["TM7"],color="y",marker="s",label="Litter low")
# 
# #ax.scatter(final["Canopy_mid"]["TM5"],final["Canopy_mid"]["TM7"],color="#ff5733",marker="^",label="Canopy mid")
# for a,f in enumerate(final["Grass_mid"]["TM5"]):
#     ax.text(final["Grass_mid"]["TM5"][a],final["Grass_mid"]["TM7"][a],labels["Grass_mid"][a+1])           
#            
# ax.scatter(final["Grass_mid"]["TM5"],final["Grass_mid"]["TM7"],color="#ff5733",marker=".",label="Grass mid")
# #ax.scatter(final["Litter_mid"]["TM5"],final["Litter_mid"]["TM7"],color="#ff5733",marker="s",label="Litter mid")
# 
# #ax.scatter(final["Canopy_high"]["TM5"],final["Canopy_high"]["TM7"],color="r",marker="^",label="Canopy high")
# for a,f in enumerate(final["Grass_high"]["TM5"]):
#     ax.text(final["Grass_high"]["TM5"][a],final["Grass_high"]["TM7"][a],labels["Grass_high"][a+1])
# 
# 
# ax.scatter(final["Grass_high"]["TM5"],final["Grass_high"]["TM7"],color="r",marker=".",label="Grass high")
# #ax.scatter(final["Litter_high"]["TM5"],final["Litter_high"]["TM7"],color="r",marker="s",label="Litter high")
# 
# ax.legend()
# =============================================================================
