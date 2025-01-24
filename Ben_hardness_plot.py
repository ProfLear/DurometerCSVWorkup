# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:34:50 2025

@author: benle
"""

from pathlib import Path
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import codechembook

shore_files = list(Path("C:/Users/benle/Documents/GitHub/DurometerCSVWorkup/LOR_exclusion").glob("*.txt"))


results = {}# empty dictionary to hold the results
for file in shore_files:
    print(file)
    results[f"{file.stem}"]={}
    with open(file, "r") as f:
        old_s = 0
        for i, line in enumerate(f):
            if i>0: #we are where the data is
                l = line.strip("\n").split("\t")
                if old_s != int(l[0]):
                    old_s = int(l[0])
                    results[f"{file.stem}"][f"{old_s}"] = {}

                results[f"{file.stem}"][f"{old_s}"][f"{l[1]}"] = np.array(l[2:])[np.array(l[2:]) !=""].astype(np.float64)



#%%
def average_measurements(condition):
    sample_ys = []
    sample_std = []
    for i in range(1,4):
        replicate_ys = [] 
        for j in range(1,4):
            replicate_ys.append(condition[f"{i}"][f"{j}"])
        sample_ys.append(np.mean(np.array(replicate_ys), axis=0))
        sample_std.append(np.std(np.array(replicate_ys), axis=0)/(len(replicate_ys)**0.5))
        
    means = np.mean(np.array(sample_ys), axis = 0)
    stds = np.sum(np.array(sample_std)**2, axis = 0)**0.5 / (len(sample_std)**0.5)
        
    return  means, stds

def get_plot_formatting(condition):
    alpha = 0.2
    symbol = "circle"
    color = f"rgba(29, 87, 0, 1)"
    fill = f"rgba(29, 87, 0, 1)"
    dash = "solid"
    error = f"rgba(29, 87, 0, {alpha})"
    
    for i, letter in enumerate(condition):
        
        if letter == "L":
            if i == 0:
                color = f"rgba(211, 96, 39, 1)"
                fill = f"rgba(211, 96, 39, 1)"
                error = f"rgba(211, 96, 39, {alpha})"
            if i == 1:
                color = f"rgba(162, 55, 104, 1)"
                fill = f"rgba(162, 55, 104, 1)"
                error = f"rgba(162, 55, 104, {alpha})"

            if i == 2:
                color = f"rgba(7, 115, 177, 1)"
                fill = f"rgba(7, 115, 177, 1)"
                error = f"rgba(7, 115, 177, {alpha})"

        
        if letter == "O":
            if i == 0:
                symbol = "circle"
            if i == 1:
                symbol = "diamond"
            if i == 2:
                symbol = "square"
        
        if letter == "R":
            if i == 0:
                dash = "dash"
            if i == 1:
                dash = "dashdot"
            if i == 2:
                dash = "dot"
        
        if "O" not in condition:
            fill = "white"
    
    return color, fill, symbol, dash, error
       
#%% Generate plots
x = [0, 0.5, 1, 1.5, 2]
tick_labels = ["center", "floor", "wall", "rim", "bulk"]
shorePlot = make_subplots(cols = 2, rows = 1)
shorePlot.update_xaxes(title = "measurement position", 
                       tickvals=x, ticktext=tick_labels, 
                       range = [-0.27, 2.1])
shorePlot.update_yaxes(title = "Shore hardness", range = [18, 57])
# construct the left plot 
col = 1

# draw all the grey lines...
for condition in ["LRO","LOR","RLO","ROL","OLR","ORL"]:
    y, std = average_measurements(results[f"{condition}"])
    #print(f"{condition}: {y}")

    # grey lines
    shorePlot.add_scatter(
        x = x, 
        y = y,
        showlegend = False,
        mode = "lines+markers",
        marker = dict(color = "lightgrey", symbol = "circle", size = 8, line = dict(width = 4, color = "lightgrey")),
        line = dict(color = "lightgrey", dash = "solid"),
        row = 1, col = 1)

for condition in ["L","LO","LR","O","OL","OR","R","RL","RO",]:
    y, std = average_measurements(results[f"{condition}"])
    # grey lines
    shorePlot.add_scatter(
        x = x, 
        y = y,
        showlegend = False,
        mode = "lines+markers",
        marker = dict(color = "lightgrey", symbol = "circle", size = 8, line = dict(width = 4, color = "lightgrey")),
        line = dict(color = "lightgrey", dash = "solid"),
        row = 1, col = 2)


    
for condition in ["L","LO","LR","O","OL","OR","R","RL","RO",]:
    
    color, fill, symbol, dash, error = get_plot_formatting(condition)

    y, std = average_measurements(results[f"{condition}"])
    
    #coded lines
    shorePlot.add_scatter(
        x = x, 
        y = y,
        showlegend = False,
        mode = "lines+markers",
        marker = dict(color = fill, symbol = symbol, size = 8, line = dict(width = 4, color = color)),
        line = dict(color = color, dash = dash),
        row = 1, col = 1)
    
    shorePlot.add_scatter(
        x = x, 
        y = y-std,
        showlegend = False,
        mode = "lines",
        marker = dict(color = fill, symbol = symbol, size = 8, line = dict(width = 4, color = color)),
        line = dict(color = color, dash = dash, width = 0),
        row = 1, col = 1)
    shorePlot.add_scatter(
        x = x, 
        y = y+std,
        showlegend = False,
        fill='tonexty',  # Fill between the bounds
        fillcolor= error,  # Transparent blue color
        mode = "lines",
        marker = dict(color = fill, symbol = symbol, size = 8, line = dict(width = 4, color = color)),
        line = dict(color = color, dash = dash, width = 0),
        row = 1, col = 1)
    
    
    shorePlot.add_annotation(text = f"{condition}", x = x[0], y = y[0], showarrow = False, xanchor = "left", xshift = -8*4.5, font = dict(color = color, ))

for condition in ["LRO","LOR","RLO","ROL","OLR","ORL"]:
    
    color, fill, symbol, dash, error = get_plot_formatting(condition)
        
    y, std = average_measurements(results[f"{condition}"])
    
    #coded lines
    shorePlot.add_scatter(
        x = x, 
        y = y,
        showlegend = False,
        mode = "lines+markers",
        marker = dict(color = fill, symbol = symbol, size = 8, line = dict(width = 4, color = color)),
        line = dict(color = color, dash = dash),
        row = 1, col = 2)
    
    shorePlot.add_scatter(
        x = x, 
        y = y-std,
        showlegend = False,
        mode = "lines",
        marker = dict(color = fill, symbol = symbol, size = 8, line = dict(width = 4, color = color)),
        line = dict(color = color, dash = dash, width = 0),
        row = 1, col = 2)
    shorePlot.add_scatter(
        x = x, 
        y = y+std,
        showlegend = False,
        fill='tonexty',  # Fill between the bounds
        fillcolor= error,  # Transparent blue color
        mode = "lines",
        marker = dict(color = fill, symbol = symbol, size = 8, line = dict(width = 4, color = color)),
        line = dict(color = color, dash = dash, width = 0),
        row = 1, col = 2)
    
    shorePlot.add_annotation(text = f"{condition}", x = x[0]-0.03, y = y[0], showarrow = False, xanchor = "left", xshift = -8*4.5, font = dict(color = color, ), row = 1, col = 2)



shorePlot.update_layout(#template = codechembook.plotlyTemplates.chemplate.JACS, 
                        template = "simple_white",
                        width = 3.3*300, height = 2.5*300,
                        font = dict(size = 15))
shorePlot.show("png")
            
            
                