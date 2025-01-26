# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:23:44 2025

@author: benle
"""
results={}

with open (r"C:/Users/benle/Documents/GitHub/DurometerCSVWorkup/LRO-RLO_n-output.csv", "r") as s:
    for line in s:
        l = line.split(",")
        #print(l)
        if "sample" not in line:
        
            sample = l[0][:3]
            print(l[0][4:-2])
            if l[0][4:-2] == "center":
                position = "floor"
            elif "inner" in l[0][4:-2]:
                position = "wall"
            elif l[0][4:-2] == "lip":
                position = "rim"
            elif l[0][4:-2] == "bulk":
                position = "bulk"
            if sample not in results:
                results[sample]={}
            if position not in results[sample]:
                results[sample][position] = {}
                results[sample][position]["cross link density"] = []
                results[sample][position]["gel fraction"] = []
                
            results[sample][position]["cross link density"].append(round(float(l[1]), 3))
            results[sample][position]["gel fraction"].append(round(float(l[3]), 4))

# write cross link table
with open(r"C:/Users/benle/Documents/GitHub/DurometerCSVWorkup/sohxletTable.txt", "w") as t:
    t.write(r'''
\begin{table}
\begin{tabular}{lllll}
\caption{Table of cross link densities (mmol/cm$^3$) obtained by solvent swelling experiments. }
    \label{tab:ShoreValues}
condition & floor & wall & rim & bulk \\ \hline
''')
    for condition in results:
        for i, measurement in enumerate(results[condition]["floor"]["cross link density"]):
            t.write(f"{condition} & {results[condition]['floor']['cross link density'][i]:.3f} & {results[condition]['wall']['cross link density'][i]} & {results[condition]['rim']['cross link density'][i]} & {results[condition]['bulk']['cross link density'][i]} " + r"\\ " + "\n")
        t.write(r"\hline" + "\n")
    t.write(r'''
\end{tabular}
\end{table}

''')   

# write gel fraction table
    t.write(r'''
\begin{table}
\begin{tabular}{lllll}
\caption{Table of gel fraction obtained by solvent swelling experiments. }
    \label{tab:ShoreValues}
condition & floor & wall & rim & bulk \\ \hline
''')
    for condition in results:
        for i, measurement in enumerate(results[condition]["floor"]["gel fraction"]):
            t.write(f"{condition} & {results[condition]['floor']['gel fraction'][i]:.4f} & {results[condition]['wall']['gel fraction'][i]:.4f} & {results[condition]['rim']['gel fraction'][i]:.4f} & {results[condition]['bulk']['gel fraction'][i]:.4f} " + r"\\ " + "\n")
        t.write(r"\hline" + "\n")
    t.write(r'''
\end{tabular}
\end{table}
''')             