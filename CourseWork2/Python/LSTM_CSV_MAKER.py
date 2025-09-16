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

from os import chdir

chdir("./Python")

# Opennig the File
data = pd.read_csv("../CSV/mars-weather.csv")
data.head()

# Data Reading
data = data[["sol","ls","month","max_temp","pressure"]]

# Removing NaN Lines
data = data.dropna()

# Data Shifting
data['sol_t-1'] = data['sol'].shift(-1)
data['ls_t-1'] = data['ls'].shift(-1)
data['max_temp_t-1'] = data['max_temp'].shift(-1)
data['pressure_t-1'] = data['pressure'].shift(-1)

# Columns Re-organization
data = data[['sol_t-1', 'ls_t-1', 'max_temp_t-1', 'pressure_t-1', 'sol', 'ls', 'max_temp', 'pressure']]

# Inverting Columns (First one becomes the last, second one the penultimate etc ...)
data = data.iloc[::-1].reset_index(drop=True)

# Removing first instance (doesn't have a previous data)
data = data.drop(index=0)

# Turning into CSV file
data.to_csv("../CSV/mars-weather_LSTM_adapted.csv", index=False)