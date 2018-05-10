#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:57:18 2018

@author: root
"""
import numpy as np
from matplotlib import pyplot as plt

def load_band(file:str):
    band=np.loadtxt(file, skiprows=1,delimiter=",")
    return band
def open_figure(rows,cols):
    fig,ax=plt.subplots(rows,cols)
    return fig,ax
def test_plot(band,style,subplot):
    subplot.plot(band[...,0],band[...,1],style)
def fwhm(band):
    wavelength=band[...,0]
    watts=band[...,1]
    half=(np.max(watts))/2
    left=np.where(watts>=half)[0].min()-1
    b=np.where((watts<=half))[0]
    right=b[b>left].min()+1
    cut_watt=watts[left:right]
    cut_watt=np.resize(cut_watt,(len(cut_watt),1))
    cut_wl=wavelength[left:right]
    cut_wl=np.resize(cut_wl,(len(cut_wl),1))
    return np.hstack((cut_wl,cut_watt))
def convolve(bandRSR,spec_sign):
    """
    inputs 
        bandRSR (type: numpy.array(), dtype: float, shape(x,2))
            x is the bandwidth in nanometers (ie the number of bands provided in the official RSR of that multispectral band).
            the columns contain 
                0: the wavelengths, 
                1: the watts
        spec_sign (type: numpy.array(), dtype: float, shape(y,z))
            y is the resolution of the hyperspectral spectral signature (ie the number of bands recorded)
            the columns contain    
                0: the wavelengths 
                1,...,z : the recorded reflectance of the different spectral signature z
            
    """
    hyper_pos=np.empty((0),dtype=int)
    watt_pos=np.empty((0),dtype=int)
    index=spec_sign[...,[0]]
    cbi=spec_sign[:,1:]
    indB=bandRSR[:,[0]]
    valB=bandRSR[:,[1]]
    for i,element in enumerate(indB):
        for n,l in enumerate(index):
            if element==l:
                hyper_pos=np.append(hyper_pos,n)#print (i, element, n, l)
                watt_pos=np.append(watt_pos,i)
    selcbi=cbi[hyper_pos]
    selband=valB[watt_pos]
    bandvalue=(np.sum(np.multiply(selcbi,selband),axis=0))/np.sum(selband)
    return bandvalue