# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 13:12:41 2025

converting data to latex tables for the physical properties paper

@author: benle
"""

from pathlib import Path
import numpy as np
import pandas as pd

shore_files = list(Path("C:/Users/benle/Documents/GitHub/DurometerCSVWorkup/LOR_exclusion").glob("*.txt"))


results = {}# empty dictionary to hold the results
for file in shore_files:
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
with open(r"C:/Users/benle/Documents/GitHub/DurometerCSVWorkup/hardnessTable.txt", "w") as t:
    t.write(r'''
\begin{longtable}{lllllll}
\caption{Table of all Shore hardness measurements.}
    \label{tab:ShoreValues}
condition & sample \# & center & floor & wall & rim & bulk \\ \hline
''')
    for condition in results:
        for sample in results[condition]:
            for replicant in results[condition][sample]:
                #if sample=="2" and replicant == "2": # only add this on the second entry...
                t.write(f"{condition} & {sample} ")
                for measurement in results[condition][sample][replicant]:
                    t.write(f"& {measurement} ")
                t.write(r"\\")
                if sample =="3" and replicant=="3":
                    t.write(r" \hline")
                t.write(" \n")
    t.write(r'''
\end{longtable}
''')