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