from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import pandas as pd
from datetime import datetime

dt = datetime.now()
dt = dt.strftime("%m.%d.%Y")


plt.style.use('fivethirtyeight')
#plt.style.use('dark_background')

def animate(i):
    RT = pd.read_csv('sensor_IOT.csv')
    RT['TS'] = pd.to_datetime(RT['TS'])
    TSF = RT['TS'].iloc[:1]
    TSL = RT['TS'].iloc[-1:]
    TT = str(pd.to_timedelta(TSL.values[0]-TSF.values[0]))
    data = pd.read_csv('sensor_IOT.csv')
    data = data.iloc[-60:]
    TS = data['TS'].str[-11:]
    xs1 = data['xs1']
    xs2 = data['xs2']
    xs3 = data['xs3']
    xs4 = data['xs4']
    xs5 = data['xs5']
    xs6 = data['xs6']
    xs7 = data['xs7']
    xs8 = data['xs8']
    plt.cla()
    
    plt.plot(TS, xs1, linewidth=2, label = 'Sensor_1')
    plt.plot(TS, xs2, linewidth=2, label = 'Sensor_2')
    plt.plot(TS, xs3, linewidth=2, label = 'Sensor_3')
    plt.plot(TS, xs4, linewidth=2, label = 'Sensor_4')
    plt.plot(TS, xs5, linewidth=2, label = 'Sensor_5')
    plt.plot(TS, xs6, linewidth=2, label = 'Sensor_6')
    plt.plot(TS, xs7, linewidth=2, label = 'Sensor_7')
    plt.plot(TS, xs8, linewidth=2, label = 'Sensor_8')
    
    plt.suptitle('IOT Live Synthetic Data : '+dt+' RunTime : '+TT, fontsize=14, fontweight='bold')
    plt.legend(loc = 'upper left', fontsize = 6)
    plt.xlabel('Time Stamp', fontsize = 8)
    plt.ylabel('Machine A', fontsize = 8)
    plt.legend(loc = 'upper left', fontsize = 6)
    plt.xticks(rotation=90, fontsize = 6)
    plt.yticks(rotation=90, fontsize = 7)
    plt.style.use('fivethirtyeight')

    AC = pd.DataFrame(RT.label.value_counts())
    AC = AC.reset_index()
    AC.columns = ['sensor','count']
    AC = AC.sort_values('sensor')
    cell_text = [AC['count'].tolist()]
    columns = AC['sensor'].tolist()
    table = plt.table(cellText=cell_text,colLabels=columns,loc='top')
    table.set_fontsize(6)
    table.scale(1,1)

    '''
    plt.axhline(23, linestyle= '--', color='grey', lw=1, alpha=0.7)
    plt.annotate('S2 Threshold', xy=(len(data), 63),fontsize = 7)
    plt.axhline(63, linestyle= '--', color='grey', lw=1, alpha=0.7)
    plt.annotate('S3 Threshold', xy=(len(data), 621),fontsize = 7)
    plt.axhline(621, linestyle= '--', color='grey', lw=1, alpha=0.7)
    plt.annotate('S4 Threshold', xy=(len(data), 94),fontsize = 7)
    plt.axhline(94, linestyle= '--', color='grey', lw=1, alpha=0.7)
    plt.annotate('S1 Threshold', xy=(len(data), 112),fontsize = 7)
    plt.axhline(111, linestyle= '--', color='grey', lw=1, alpha=0.7)
    plt.annotate('S2 Threshold', xy=(len(data), 351),fontsize = 7)
    plt.axhline(351, linestyle= '--', color='grey', lw=1, alpha=0.7)
    plt.annotate('S3 Threshold', xy=(len(data), 621),fontsize = 7)
    plt.axhline(621, linestyle= '--', color='grey', lw=1, alpha=0.7)
    plt.annotate('S4 Threshold', xy=(len(data), 94),fontsize = 7)
    plt.axhline(94, linestyle= '--', color='grey', lw=1, alpha=0.7)
    '''
    plt.tight_layout()
    plt.show()
    
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()
plt.show()
