import methods
import os
from matplotlib import pyplot as plt
import numpy as np


fnb5="TM_5.csv"
fnb7="TM_7.csv"
pthb5=os.path.join("Band_RSR",fnb5)
pthb7=os.path.join("Band_RSR",fnb7)


smpl="CBI.csv"
pth_sample=os.path.join("Hyper_samples",smpl)

#get header
with open(pth_sample,"r") as dummy:
    labels=dummy.read().split("\n")[0]
#get values
labbs=[f for f in labels.split(",")]    
cbitot=methods.load_band(pth_sample)

##b5
B5=methods.load_band(pthb5)
b5_cut=methods.fwhm(B5)
#bandtot=b5_cut
##b7
B7=methods.load_band(pthb7)
b7_cut=methods.fwhm(B7)
#bandtot=b5_cut


#np.all(b5_cut[:,0]==index)
#gg=np.where(b5_cut[:,0]==index,b5_cut[:,0],index)
def select_wavelength(bandtot,cbitot):
    """given 1 wavelegths selected of a band and all the wavelengths available, returns an index"""
    hyper_pos=np.empty((0),dtype=int)
    watt_pos=np.empty((0),dtype=int)
    index=cbitot[...,[0]]
    cbi=cbitot[:,1:30]
    indB=bandtot[:,[0]]
    valB=bandtot[:,[1]]
    for i,element in enumerate(indB):
        for n,l in enumerate(index):
            if element==l:
                hyper_pos=np.append(hyper_pos,n)#print (i, element, n, l)
                watt_pos=np.append(watt_pos,i)
    selcbi=cbi[hyper_pos]
    selband=valB[watt_pos]
    bandvalue=(np.sum(np.multiply(selcbi,selband),axis=0))/np.sum(selband)
    return bandvalue
b5s=select_wavelength(b5_cut,cbitot)
b7s=select_wavelength(b7_cut,cbitot)

fig,ax=methods.open_figure(1,1)
ax.scatter(b5s,b7s)
lab=labbs[1:30]
for i, txt in enumerate(lab):
    ax.annotate(txt, (b5s[i],b7s[i]))
    

methods.test_plot(B7,"k--",ax)
methods.test_plot(b7_cut,"r-",ax)