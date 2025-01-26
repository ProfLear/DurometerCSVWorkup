# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:13:58 2025

@author: benle
"""

results={}

with open (r"C:/Users/benle/Documents/GitHub/DurometerCSVWorkup/pynometry.csv", "r") as s:
    for line in s:
        l = line.split(",")
        #print(l)
        if "sample" not in line:
        
            sample = l[0][:3]
            print(l[0][4:])
            if "center" in l[0][4:]:
                position = "floor"
            elif "inner" in l[0][4:]:
                position = "wall"
            elif l[0][4:] == "top-lip":
                position = "rim"
            elif l[0][4:] == "bulk":
                position = "bulk"
            if sample not in results:
                results[sample]={}
            if position not in results[sample]:
                results[sample][position] = {}
                results[sample][position]["density"] = round(float(l[3]), 4)
                results[sample][position]["density error"] = round(float(l[4]), 4)
                
#%%
# write cross link table
with open(r"C:/Users/benle/Documents/GitHub/DurometerCSVWorkup/densityTable.txt", "w") as t:
    t.write(r'''
\begin{table}
\begin{tabular}{ccccc}
\caption{Table of mass densities (g/cm$^3$) obtained pycnometry measurements. }
    \label{tab:ShoreValues}
condition & floor & wall & rim & bulk \\ \hline
''')
    for condition in results:
        t.write(f"{condition}")
        for position in results[condition]:
            t.write(f" & {results[condition][position]['density']:.4f} $\pm$ {results[condition][position]['density error']:.4f} " )
        t.write(r"\\" + "\n")
    t.write(r'''\hline
\end{tabular}
\end{table}

''') 