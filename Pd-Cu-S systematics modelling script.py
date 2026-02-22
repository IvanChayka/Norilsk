#calculate bulk content of Pd

import numpy as np
import matplotlib.pyplot as plt

# Define X range
F_values = np.linspace(0, 0.6, 100)

# Define A and B ranges
A_values = np.arange(10, 210, 10) # Dpd fl/sil
B_values = {10000, 15000, 20000, 30000, 50000, 100000, 500000, 1000000} #DPd sul/sil
I_values = {0.008, 0.011, 0.03} #initial sulfur conc 

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 70,
    "axes.edgecolor": "black",
    "xtick.color": "black",
    "ytick.color": "black"
})
plt.figure(figsize=(40, 30))
colors = ['grey', 'red', 'grey']

# Generate and plot the curves
for i, I in enumerate(I_values, start = 0):
        for A in A_values:
            for B in B_values:
                S_values = (I - 0.05 * F_values) #sulfur vs fluid evolved
                mask = S_values > 0.0005 #sulfur content at sulfide exhaustion
                if np.any(mask):  # proceed only if at least one value is valid
                     S_filtered = S_values[mask]
                     F_filtered = F_values[mask]
                     Sulf = S_filtered / 0.35 #sulfide vs fluid evolved
                     DPd = ((0.25 - F_filtered) / A) + Sulf * (B / A) #calculate D as in Boudreau1992
                     CoPd = 2.8 * (I * 100) - 0.27 #initial concnetration as in taxitic gabbros (empirical regression)
                     CPd = np.where(
                    F_filtered < 0.07,
                    CoPd * (1 - F_filtered) ** ((1 / DPd) - 1),
                    CoPd * (1 - 0.07) ** ((1 / DPd) - 1)
                    )#calculate C(Pd) as in Boudreau1992, Shaw1970
                     plt.plot(S_filtered * 100,  CPd, color=colors[i], linewidth=1, alpha=0.4)
plt.yscale('log')
plt.xlim(0, 3)
plt.ylim(0.5, 30)
plt.xlabel('S, wt. %')
plt.ylabel('Pd, ppm')
ax = plt.gca()
ax.tick_params(
    axis='both',      
    colors='black',    
    width=5,        
    length=40           
)
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(5)  

# %%
#calculate Pd tenor

import numpy as np
import matplotlib.pyplot as plt


F_values = np.linspace(0, 0.6, 100)
A_values = np.arange(10, 210, 10) 
B_values = {10000, 15000, 20000, 30000, 50000, 100000, 500000, 1000000} 
I_values = {0.008, 0.018, 0.03} 

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 70,
    "axes.edgecolor": "black",
    "xtick.color": "black",
    "ytick.color": "black"
})
plt.figure(figsize=(40, 30))
colors = ['grey', 'red', 'grey']

TPd_matches = []
for i, I in enumerate(I_values, start = 0):
        for A in A_values:
            for B in B_values:
                S_values = (I - 0.05 * F_values) 
                mask = S_values > 0.0005
                if np.any(mask):  
                     S_filtered = S_values[mask]
                     F_filtered = F_values[mask]
                     Sulf = S_filtered / 0.35 
                     DPd = ((0.25 - F_filtered) / A) + Sulf * (B / A) 
                     CoPd = 2.8 * (I * 100) - 0.27
                     CPd = np.where(
                    F_filtered < 0.07,
                    CoPd * (1 - F_filtered) ** ((1 / DPd) - 1),
                    CoPd * (1 - 0.07) ** ((1 / DPd) - 1)
                    )
                     TPd = CPd / S_filtered * 0.35
                     plt.plot(S_filtered * 100,  TPd, color=colors[i], linewidth=1, alpha=0.4)
plt.yscale('log')
plt.xlim(0, 3)
plt.ylim(10, 5000)
plt.xlabel('S, wt. %')
plt.ylabel('Pd, ppm')
ax = plt.gca()
ax.tick_params(
    axis='both',       
    colors='black',    
    width=5,        
    length=40          
)
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(5)  
# %%

#calculate bulk content of Cu
import numpy as np
import matplotlib.pyplot as plt

# Define X range
F_values = np.linspace(0, 0.6, 100)

# Define A and B ranges
M_values = np.arange(5, 300, 30)
N_values = np.arange(250, 1450, 100)
I_values = {0.008, 0.011, 0.03} #initial sulfur conc 

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 70,
    "axes.edgecolor": "black",
    "xtick.color": "black",
    "ytick.color": "black"
})
plt.figure(figsize=(40, 30))
colors = ['grey', 'red', 'grey']

# Generate and plot the curves
for i, I in enumerate(I_values, start = 0):
        for M in M_values:
            for N in N_values:
                S_values = (I - 0.05 * F_values) #sulfur vs fluid evolved
                mask = S_values > 0. #sulfur content at sulfide exhaustion
                if np.any(mask):  # proceed only if at least one value is valid
                     S_filtered = S_values[mask]
                     F_filtered = F_values[mask]
                     Sulf = S_filtered / 0.35 #sulfide vs fluid evolved
                     DCu = ((0.25 - F_filtered) / M) + Sulf * (N / M) #calculate D as in Boudreau1992
                     CoCu = 2775 * (I * 100) + 1215 #initial concnetration as in taxitic gabbros (empirical regression)
                     CCu = np.where(
                    F_filtered < 0.07,
                    CoCu * (1 - F_filtered) ** ((1 / DCu) - 1),
                    CoCu * (1 - 0.07) ** ((1 / DCu) - 1)
                    )#calculate C(Cu) as in Boudreau1992, Shaw1970
                     plt.plot(S_filtered * 100,  CCu, color=colors[i], linewidth=1, alpha=0.4)
plt.yscale('log')
plt.xlim(0, 3)
plt.ylim(200, 20000)
plt.xlabel('S, wt. %')
plt.ylabel('Cu, ppm')
ax = plt.gca()
ax.tick_params(
    axis='both',       
    colors='black',    
    width=5,       
    length=40           
)
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(5) 

# %%
#calculate Cu tenor
import numpy as np
import matplotlib.pyplot as plt

# Define X range
F_values = np.linspace(0, 0.6, 100)

# Define A and B ranges
M_values = np.arange(5, 300, 30)
N_values = np.arange(250, 1450, 100)
I_values = {0.008, 0.011, 0.03} #initial sulfur conc 

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 70,
    "axes.edgecolor": "black",
    "xtick.color": "black",
    "ytick.color": "black"
})
plt.figure(figsize=(40, 30))
colors = ['grey', 'red', 'grey']

# Generate and plot the curves
for i, I in enumerate(I_values, start = 0):
        for M in M_values:
            for N in N_values:
                S_values = (I - 0.05 * F_values) #sulfur vs fluid evolved
                mask = S_values > 0.0005
                if np.any(mask):  # proceed only if at least one value is valid
                     S_filtered = S_values[mask]
                     F_filtered = F_values[mask]
                     Sulf = S_filtered / 0.35 
                     DCu = ((0.25 - F_filtered) / M) + Sulf * (N / M) 
                     CoCu = 2775 * (I * 100) + 1215 
                     CCu = np.where(
                    F_filtered < 0.07,
                    CoCu * (1 - F_filtered) ** ((1 / DCu) - 1),
                    CoCu * (1 - 0.07) ** ((1 / DCu) - 1)
                    )
                     TCu = CCu / S_filtered * 0.35 / 10000
                     plt.plot(S_filtered * 100,  TCu, color=colors[i], linewidth=1, alpha=0.4)

#plt.xscale('log')
#plt.yscale('log')
plt.xlim(0, 3)
plt.ylim(0, 25)
plt.xlabel('S, wt. %')
plt.ylabel('Cu, ppm')
ax = plt.gca()
ax.tick_params(
    axis='both',       
    colors='black', 
    width=5,        
    length=40         
)
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(5)  
# %%
#calculate Cu/Pd

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import math

F_values = np.linspace(0, 0.6, 100)

A_values = np.arange(10, 210, 50)
B_values = {10000, 15000, 20000, 30000, 50000, 100000, 500000, 1000000}
M_values = np.arange(5, 300, 30)
N_values = np.arange(250, 1450, 100)
I_values = {0.008, 0.011, 0.03} 

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 70,
    "axes.edgecolor": "black",
    "xtick.color": "black",
    "ytick.color": "black"
})
plt.figure(figsize=(40, 30))
colors = ['grey', 'red', 'grey']

for i, I in enumerate(I_values, start=0):
    for A in A_values:
        for B in B_values:
            for M in M_values:
                for N in N_values:
                    S_values = (I - 0.05 * F_values)
                    mask = S_values > 0.0005
                    if np.any(mask):
                        S_filtered = S_values[mask]
                        F_filtered = F_values[mask]
                        Sulf = S_filtered / 0.35
                        
                        DPd = ((0.25 - F_filtered) / A) + Sulf * (B / A)
                        CoPd = 2.8 * (I * 100) - 0.27
                        CPd = np.where(
                            F_filtered < 0.07,
                            CoPd * (1 - F_filtered) ** ((1 / DPd) - 1),
                            CoPd * (1 - 0.07) ** ((1 / DPd) - 1)
                        )

                        DCu = ((0.25 - F_filtered) / M) + Sulf * (N / M)
                        CoCu = 2775 * (I * 100) + 1215
                        CCu = np.where(
                            F_filtered < 0.07,
                            CoCu * (1 - F_filtered) ** ((1 / DCu) - 1),
                            CoCu * (1 - 0.07) ** ((1 / DCu) - 1)
                        )

                        CuPd = CCu / CPd
                        plt.plot(S_filtered * 100, CuPd, color=colors[i], linewidth=0.5, alpha=0.05)

plt.xlim(0, 3)
plt.ylim(0, 1800)
plt.xlabel('S, wt. %')
plt.ylabel('Cu/Pd')
ax = plt.gca()
ax.tick_params(
    axis='both',       
    colors='black',   
    width=5,         
    length=40           
)
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(5) 
plt.show()
# %%

#plot Cu tenor vs Pd tenor
import numpy as np
import matplotlib.pyplot as plt

F_values = np.linspace(0, 0.6, 100)

A_values = np.arange(10, 210, 50)
B_values = {10000, 15000, 20000, 30000, 50000, 100000, 500000, 1000000}
M_values = np.arange(5, 300, 30)
N_values = np.arange(250, 1450, 100)
I_values = {0.008, 0.011, 0.03} 

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 70,
    "axes.edgecolor": "black",
    "xtick.color": "black",
    "ytick.color": "black"
})

plt.figure(figsize=(40, 30))
colors = ['grey', 'red', 'grey']

for i, I in enumerate(I_values, start=0):
    for A in A_values:
        for B in B_values:
            for M in M_values:
                for N in N_values:
                    S_values = (I - 0.05 * F_values)
                    mask = S_values > 0.0005
                    if np.any(mask):
                        S_filtered = S_values[mask]
                        F_filtered = F_values[mask]
                        Sulf = S_filtered / 0.35
                        
                        DPd = ((0.25 - F_filtered) / A) + Sulf * (B / A)
                        CoPd = 2.8 * (I * 100) - 0.27
                        CPd = np.where(
                            F_filtered < 0.07,
                            CoPd * (1 - F_filtered) ** ((1 / DPd) - 1),
                            CoPd * (1 - 0.07) ** ((1 / DPd) - 1)
                        )

                        DCu = ((0.25 - F_filtered) / M) + Sulf * (N / M)
                        CoCu = 2775 * (I * 100) + 1215
                        CCu = np.where(
                            F_filtered < 0.07,
                            CoCu * (1 - F_filtered) ** ((1 / DCu) - 1),
                            CoCu * (1 - 0.07) ** ((1 / DCu) - 1)
                        )
                        TCu = CCu / Sulf / 10000
                        TPd = CPd / Sulf
                    
                        plt.plot(TPd,  TCu, color=colors[i], linewidth=1, alpha=0.02)

# Labels and title
plt.xscale("log")
#plt.yscale("log")
plt.xlim(20, 3000)
plt.ylim(0, 25)
plt.xlabel('Pd in 100% sulfide, ppm')
plt.ylabel('Cu in 100% sulfide, wt. %')
ax = plt.gca()
ax.tick_params(
    axis='both',      
    colors='black',   
    width=5,         
    length=40           
)
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(5)  
# %% 
# upgrading of Pd

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 70,
    "axes.edgecolor": "black",
    "xtick.color": "black",
    "ytick.color": "black"
})

S_values = np.linspace(0.05, 3, 1000)
A_values = np.arange(400, 4400, 100) #range of provisional tenors of Pd in the "last sulfide droplet"

plt.figure(figsize=(40, 30))

for A in A_values:
    CPd = S_values / 100 * A
    plt.plot(S_values,  CPd, linewidth=1)

plt.yscale("log")
ax = plt.gca()
ax.tick_params(
    axis='both',     
    colors='black',   
    width=5,         
    length=40           
)
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(5)  

# %% 
# Upgrading of Cu

import numpy as np
import matplotlib.pyplot as plt

S_values = np.linspace(0.05, 3, 1000)
A_values = np.arange(100, 50000, 100) #range of provisional tenors of Cu in the "last sulfide droplet"

plt.figure(figsize=(40, 30))

for A in A_values:
    CCu = S_values / 100 * A
    plt.plot(S_values,  CCu, linewidth=1)

plt.yscale("log")