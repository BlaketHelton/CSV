import matplotlib.pyplot as plt
import pandas as p
import matplotlib.dates as mdates
from datetime import datetime

death_valley = open('death_valley_2018_simple.csv', 'r')
sitka = open('sitka_weather_2018_simple.csv', 'r')

death_valley_data = p.read_csv(death_valley)
sitka_data = p.read_csv(sitka)

# X-AXIS
death_valley_date = death_valley_data['DATE']
sitka_date = sitka_data['DATE']

# CONVERT DATES
death_valley_date = [datetime.strptime(d, '%Y-%m-%d') for d in death_valley_date]
sitka_date = [datetime.strptime(d, '%Y-%m-%d') for d in sitka_date]

# Y-AXIS
death_valley_tmax = death_valley_data['TMAX']
death_valley_tmin = death_valley_data['TMIN']
sitka_tmax = sitka_data['TMAX']
sitka_tmin = sitka_data['TMIN']

fig, axs = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle("Temperature comparison between SITKA AIPORT, AK US and DEATH VALLEY, CA US")

# DEATH VALLEY
axs[0].plot(death_valley_date, death_valley_tmax, color='red', label='TMAX')
axs[0].plot(death_valley_date, death_valley_tmin, color='blue', label='TMIN')
axs[0].fill_between(death_valley_date, death_valley_tmax, death_valley_tmin, color='lightblue')
#axs[0].set_xlabel('Date')
axs[0].set_ylabel('Temperature (F)')
axs[0].set_title('Death Valley, CA US')
axs[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axs[0].legend()

# SITKA
axs[1].plot(sitka_date, sitka_tmax, color='red', label='TMAX')
axs[1].plot(sitka_date, sitka_tmin, color='blue', label='TMIN')
axs[1].fill_between(sitka_date, sitka_tmax, sitka_tmin, color='lightblue')
axs[1].set_ylabel('Temperature (F)')
axs[1].set_title('Sitka Airport, AK, US')
axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axs[1].legend()

plt.show()