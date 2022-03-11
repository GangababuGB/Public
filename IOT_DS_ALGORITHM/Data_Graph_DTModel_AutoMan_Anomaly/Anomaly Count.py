
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt 

data = pd.read_csv('sensor_IOT.csv')
AC = pd.DataFrame(data.label.value_counts())
AC = AC.reset_index()
AC.columns = ['sensor','count']
AC = AC.sort_values('sensor')
cell_text = [AC['count'].tolist()]
rows = AC['sensor'].tolist()
#columns = AC['sensor'].tolist()
plt.table(cellText=cell_text,colLabels=columns,loc='right')

plt.show()
