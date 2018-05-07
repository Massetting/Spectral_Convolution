import methods
import os
#from matplotlib import pyplot as plt
import numpy as np


fnb5="TM_5.csv"
pthb5=os.path.join("Band_RSR",fnb5)
smpl="CBI.csv"
pth_sample=os.path.join("Hyper_samples",smpl)

#get header
with open(pth_sample,"r") as dummy:
    ggg=dummy.read().split("\n")[0]
#get values
cbi=methods.load_band(pth_sample)
index=cbi[...,0]

##
B5=methods.load_band(pthb5)
b5_cut=methods.fwhm(B5)

#####


b5_cut[b5_cut[:,0]==index]
np.where(b5_cut[:,0]==index)


fig,ax=methods.open_figure(1,1)
methods.test_plot(B5,"k--",ax)
methods.test_plot(b5_cut,"r-",ax)