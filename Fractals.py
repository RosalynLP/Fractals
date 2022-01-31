#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:50:46 2021

@author: rosalyn
"""
import matplotlib.pyplot as plt
import numpy as np

class Fractal:
    def __init__(self, grid_lims, plot_shape, const_param, N_upper=255, z_thresh = 2):
        self.grid_lims=grid_lims
        self.plot_shape=plot_shape
        self.const_param = const_param
        self.N_upper=N_upper
        self.z_thresh=z_thresh
        self.grid_Ns = np.zeros(plot_shape)
        
        x_lower,x_upper = grid_lims[0]
        y_lower,y_upper = grid_lims[1]        
        x_points,y_points = plot_shape
        
        self.grid_vars = np.array([[np.complex(x,y) for y in np.linspace(y_lower,y_upper,y_points)] for x in np.linspace(x_lower,x_upper,x_points)])
            
    def plot(self):
        fig, axes = plt.subplots()
        plt.axis('off')
        axes.imshow(self.grid_Ns.T, interpolation="bicubic", cmap="Spectral")
        return None
        
class Mandelbrot(Fractal):
    def __init__(self, grid_lims, plot_shape, z0=0,  N_upper=255, z_thresh = 2):
        super().__init__(grid_lims, plot_shape, z0, N_upper=255, z_thresh = 2)
        self.Cs = self.grid_vars
        self.z0 = self.const_param
    
    def find_all_Ns(self):
        for ind, C in np.ndenumerate(self.Cs):
            z=self.z0
            N=0
            while (np.abs(z)<=self.z_thresh and N < self.N_upper):
                z = z**2 + C
                N+=1
            self.grid_Ns[ind] = N
        return None
    
class Julia(Fractal):    
    def __init__(self, grid_lims, plot_shape, C,  N_upper=255, z_thresh = 2):
        super().__init__(grid_lims, plot_shape, C, N_upper=255, z_thresh = 2)
        self.z0s = self.grid_vars
        self.C = self.const_param        
    
    def find_all_Ns(self):
        for ind, z0 in np.ndenumerate(self.z0s):
            z=z0
            N=0
            while (np.abs(z)<=self.z_thresh and N < self.N_upper):
                z = z**2 + self.C
                N+=1
            self.grid_Ns[ind] = N
        return None
    
      
def main():
    #grid_lims = ((-2.025,0.6),(-1.125,1.125))
    grid_lims = ((-1.5,1.5),(-1,1))
    plot_shape = (800,800)
    Julia_dict = {"A":np.complex(0,-1),
                  "B":np.complex(-0.1,0.8), 
                  "C":np.complex(0.36,0.1),
                  "D":np.complex(-1,0),
                  "E":np.complex(0.5,0),
                  "F":np.complex(*np.random.rand(2)),
                  "G":-0.30901699 + 0.95105652j,
                  "secret": (0.2703509102469164+0.4928516089439091j),
                  "bingo": (-0.512511498387847167+0.521295573094847167j)}
    
    frac = input(prompt = "Mandelbrot or Julia (M/J):")
    if frac == "M":
        man = Mandelbrot(grid_lims,plot_shape)
        man.find_all_Ns()
        man.plot()
    elif frac == "J":
        J_type = input(prompt = "Which Julia? Dendrite(A), Rabbit(B), Dragon(C), D, E or random(F):")
        Jul = Julia(grid_lims,plot_shape,Julia_dict[J_type])
        Jul.find_all_Ns()
        Jul.plot()
        if J_type == "F":
            print(Julia_dict[J_type])
    else:
        print("We did not recognise your query, goodbye")
        
    return Jul
    
main()
