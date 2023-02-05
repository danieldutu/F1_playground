import pandas as pd
import math
import matplotlib.pyplot as plt
import fastf1 as ff1
from fastf1 import plotting

plotting.setup_mpl()



# Read the first line of the file into a string
# with open("F12022.csv") as f:
#     first_line = f.readline()

# # Split the first line by spaces and use it as the header row
# header = first_line.strip().split(" ")

# # Read the rest of the file, specifying the header row and the separator
df = pd.read_csv("F12022.csv", delim_whitespace=True)

df = df.reset_index()
df = df.loc[:4324]
# print(df.columns)

# df.to_csv("F12022_new.csv", index=False)

throttle = df['throttle']
brake = df['brake']
gear = df['gear']
drs = df['drs']
rpm = df['rpm']
t = df['lap_time']
df['my_velocity'] = df.apply(lambda row: math.sqrt(row['velocity_X']**2 + row['velocity_Y']**2 + row['velocity_Z']**2), axis=1)
vCar = df['my_velocity']*4



fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, figsize=(10,10), sharex=True)
ax1.plot(t, vCar)
ax1.set_ylabel('Speed [Km/h]')

# Throttle plot
ax2.plot(t, throttle)
ax2.set_ylabel('Throttle')

# Brake plot
ax3.plot(t, brake)
ax3.set_ylabel('Brake')

# Gear plot
ax4.plot(t, gear, color='red')
ax4.set_ylabel('Gear')

# DRS plot
ax5.plot(t, drs, color='green')
ax5.set_ylabel('DRS')

# RPM plot
ax6.plot(t, rpm, color='orange')
ax6.set_ylabel('RPM')

#save figure
plt.savefig('my_lap.png')

plt.show()
