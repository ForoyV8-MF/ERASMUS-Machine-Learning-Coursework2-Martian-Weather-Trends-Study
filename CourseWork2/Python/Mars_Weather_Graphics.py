#****************************************************************************#
#*  ADAPTED BY : Vérin Clément                              ISIMA (ZZ2, F1) *#
#*  SUPERVISED BY : Paul Trundle                        Bradford University *#
#*  April / May 2025                                                        *#
#*                                                                          *#
#*             CourseWork #2 Study of Weather Trends on Mars                *#
#*                                                                          *#
#* Mars_Weather_Graphics.py                                                 *#
#* LSTM_CSV_MAKER.py                                                        *#
#*                                                                          *#
#* VS CODE                                                   Python 3.11.2  *#
#****************************************************************************#

# // CSV FILE EXPLAINATION \\

# id : Unique number representing the sample
# terrestrial_date : Earthian date of sample collection.
# sol : Number of Martian days elapsed since the Curiosity Rover landed. One "day" on Mars last 24h39, wich is called a "sol".
# ls : "Solar Longitude". Position of mars on its orbit around the sun. That's why it moves between 0 and 360 degrees.
# month : Earthian month of sample collection.
# min_temp : Minimal temperature noted on this sol.
# max_temp : Maximal temperature noted on this sol.
# pressure : Pressure noted on this sol.
# wind_speed : Speed of the wind noted on this sol.
# atmo_opacity : General weather of this sol.

import pandas as pd
import matplotlib.pyplot as plt

from os import chdir

chdir("./Python")

# Opennig the File
data = pd.read_csv("../CSV/mars-weather.csv")
data.head()

# Data Selection
data = data[["id","terrestrial_date","sol","ls","month","min_temp","max_temp","pressure","wind_speed","atmo_opacity"]]

# Data Grouping
ls_Mean_Min_Temp = data.groupby('ls')['min_temp'].mean()
ls_Mean_Max_Temp = data.groupby('ls')['max_temp'].mean()
ls_Mean_Press = data.groupby('ls')['pressure'].mean()

sol_Min_Temp = data.groupby('sol')['min_temp'].mean()
sol_Max_Temp = data.groupby('sol')['max_temp'].mean()
sol_Press = data.groupby('sol')['pressure'].mean()

# Statistics Displaying
plt.figure(figsize=(15, 10), facecolor="black")
plt.style.use("dark_background")

plt.subplot(321)
plt.plot(ls_Mean_Min_Temp.index, ls_Mean_Min_Temp.values, marker='o', linestyle='none', color="skyblue", markersize=3, label="temperature")
plt.title('Mean of Minimum Temperature value grouped by Solar Longitude')
plt.xlabel('Solar Longitude (degrees)')
plt.ylabel('Minimum Temperature (degrees Celsius)')
plt.legend()

plt.subplot(322)
plt.plot(ls_Mean_Max_Temp.index, ls_Mean_Max_Temp.values, marker='o', linestyle='none', color="red", markersize=3, label="temperature")
plt.title('Mean of Maximum Temperature value grouped by Solar Longitude')
plt.xlabel('Solar Longitude (degrees)')
plt.ylabel('Maximum Temperature (degrees Celsius)')
plt.legend()

plt.subplot(323)
plt.plot(ls_Mean_Press.index, ls_Mean_Press.values, marker='o', linestyle='none', color='green', markersize=3, label="pressure")
plt.title('Pressure value grouped by Solar Longitude')
plt.xlabel('Solar Longitude (degrees)')
plt.ylabel('Pressure (pascals)')
plt.legend()

plt.subplot(324)
plt.plot(sol_Min_Temp.index, sol_Min_Temp.values, marker='o', linestyle='none', color='skyblue', markersize=3, label="temperature")
plt.title('Minimum Temperature value changes over the sols')
plt.xlabel('Current Sol (since landing)')
plt.ylabel('Minimum Temperature (degrees Celsius)\n')
plt.legend()

plt.subplot(325)
plt.plot(sol_Max_Temp.index, sol_Max_Temp.values, marker='o', linestyle='none', color='red', markersize=3, label="temperature")
plt.title('Maximum Temperature value changes over the sols')
plt.xlabel('Current Sol (since landing)')
plt.ylabel('Maximum Temperature (degrees Celsius)\n')
plt.legend()

plt.subplot(326)
plt.plot(sol_Press.index, sol_Press.values, marker='o', linestyle='none', color='green', markersize=3, label="pressure")
plt.title('Pressure value changes over the sols')
plt.xlabel('Current Sol (since landing)')
plt.ylabel('Pressure (pascals)')
plt.legend()

plt.tight_layout()
plt.show()
