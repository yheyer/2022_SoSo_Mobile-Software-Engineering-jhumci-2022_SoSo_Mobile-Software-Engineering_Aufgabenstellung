# %% Notwendige Pakte importieren
import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %% Angabe des Dateipfades
folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'input_data')
file_name =  os.path.join(folder_input_data, 'power_data_3.txt')

# Alternativ auf hard-gecodeded
file_name = "input_data/power_data_3.txt"


# %% Öffnen der Datei
power_data_watts = open(file_name).read().split("\n")

# Entfernen der letzten leeren Zeile (optional)
power_data_watts.pop(-1)

# %% Plotten wie in Programmierübung 1 

fig, ax = plt.subplots()  # Über subplots wird eine figure erstellt und ein Achsen Objekt
ax.plot(power_data_watts)

# %%
