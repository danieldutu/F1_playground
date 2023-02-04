import fastf1 as ff1
import matplotlib.pyplot as plt
from tqdm import tqdm

from fastf1 import plotting
import matplotlib.animation as animation

plt.rcParams['animation.ffmpeg_path']= r'D:\ffmpeg-2022-05-12-git-30e2bb0f64-essentials_build\bin\ffmpeg.exe'
plotting.setup_mpl()

# get the data
cache = ff1.Cache.enable_cache(r'D:\F1_playground\f1_cache') # enable cache

# get the data
session = ff1.get_session(2022, 'Austria', 'Q')

session.load()

fast_ver = session.laps.pick_driver('VER').pick_fastest()
ver_car_data = fast_ver.get_car_data()


# Get additional data for the plot
throttle = ver_car_data['Throttle']
brake = ver_car_data['Brake']
gear = ver_car_data['nGear']
drs = ver_car_data['DRS']
rpm = ver_car_data['RPM']
vCar = ver_car_data['Speed']
t = ver_car_data['Time']



fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, figsize=(10,10), sharex=True)

# Speed plot
ax1.plot(t, vCar)
ax1.set_xlabel('Time')
ax1.set_ylabel('Speed [Km/h]')
ax1.set_title('Speed')

# Throttle plot
ax2.plot(t, throttle)
ax2.set_xlabel('Time')
ax2.set_ylabel('Throttle')
ax2.set_title('Throttle')

# Brake plot
ax3.plot(t, brake)
ax3.set_xlabel('Time')
ax3.set_ylabel('Brake')
ax3.set_title('Brake')

# Gear plot
ax4.plot(t, gear, color='red')
ax4.set_ylabel('Gear')

# DRS plot
ax5.plot(t, drs, color='green')
ax5.set_ylabel('DRS')

# RPM plot
ax6.plot(t, rpm, color='orange')
ax6.set_ylabel('RPM')



def animate(i):
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()
    ax6.clear()
    
    x = t[:i+1]
    y1 = vCar[:i+1]
    y2 = throttle[:i+1]
    y3 = brake[:i+1]
    y4 = gear[:i+1]
    y5 = drs[:i+1]
    y6 = rpm[:i+1]
    
    ax1.plot(x, y1)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Speed [Km/h]')
    ax1.set_xlim(0, t.max())  # Fix x axis range    
    
    ax2.plot(x, y2)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Throttle')
    ax2.set_xlim(0, t.max())  # Fix x axis range    

    
    
    ax3.plot(x, y3)
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Brake')
    ax3.set_xlim(0, t.max())  # Fix x axis range    

    
    ax4.plot(x, y4, color='red')
    ax4.set_ylabel('Gear')
    ax4.set_xlim(0, t.max()) # Fix x axis range    

    
    ax5.plot(x, y5, color='green')
    ax5.set_ylabel('DRS')
    ax5.set_xlim(0, t.max())  # Fix x axis range    

    
    ax6.plot(x, y6, color='orange')
    ax6.set_ylabel('RPM')
    ax6.set_xlim(0, t.max())  # Fix x axis range    



ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=270, blit=False)

for i in tqdm(range(len(t))):
    ani._start(i)

ani.save('telemetry.mp4', writer='ffmpeg')

