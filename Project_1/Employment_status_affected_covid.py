import csv
from dateutil.parser import parse

# data wrangling
Regc = []
Datec = []
Eurc = []
Elprc = []
Eerc = []

# loading data from local maxhine
with open('Unemployment_Rate_M_Total.txt') as file:
    next(file)
    for row in csv.DictReader(file):
        Regc.append(str(row['Region']))
        Datec.append(str(parse(row[' Date']).strftime('%Y-%m-%d')))
        Eurc.append(float(row[' Estimated Unemployment Rate (%)']))
        Elprc.append(float(row[' Estimated Labour Participation Rate (%)']))

for line in Eurc:
    Eerc.append(float("%.2f" % (100.00 - line)))

# creating mapped values for dictionary from original date
from operator import itemgetter
mapped = zip(Regc, Datec, Eurc, Eerc, Elprc)
# converting values to print as set
mapped = set(mapped)
mapped = [list(ele) for ele in mapped]
mapped = sorted(mapped, key=itemgetter(0, 1))

# creating keys for dictionary extracted from header of the file
Key_features = ['Region', ' Date', ' Estimated Unemployment Rate (%)', ' Estimated Employed Rate (%)',
                ' Estimated Labour Participation Rate (%)']
# print(Key_features)
# print(mapped)
# Creating Dictionary Dataframe
dicts_df = [dict(zip(Key_features, x)) for x in mapped]
dictionary = {i: d for i, d in enumerate(dicts_df)}
# print(dictionary)
# Code to save Dataframe of dictionary in Local machine
# out_file = open('dictionary.txt', 'wt')
# out_file.write(str(dictionary))
# out_file.close()

All_region = list(set(Regc))
All_region = sorted(All_region)
print(All_region) # User options

# state_in = input("Visualise which state from the above?: ") # defining input from user
# # Temp bucket for state given by user
# S_Buc = []
# for row in dictionary[:224]:
#     if row[0] == state_in:
#         sorted(S_Buc)
#         S_Buc.append(row)
#
# print(S_BUC)
# sorted_list = sorted(S_Buc, key=lambda x: x[1])
# arr2 = [item[3] for item in S_Buc]
# https://www.programiz.com/python-programming/nested-dictionary
mapped = []
# to fetch data from dictionary.
for i, j in dictionary.items():
    for key in j:
        #print(key + ':', j[key])
        # print(j[key])
        mapped.append(j[key])

new_items = [mapped[i:i+5] for i in range(0, len(mapped), 5)]
# print(len(new_items))
# print(new_items)
state_in = input("Visualise which state from the above?: ") # defining input from user
# Temp bucket for state given by user
S_Buc = []
for row in new_items[:224]:
    if row[0] == state_in:
        sorted(S_Buc)
        S_Buc.append(row)

sorted_list = sorted(S_Buc, key=lambda x: x[1])
arr2 = [item[3] for item in S_Buc]

# Ploting
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10})
#stackplot
# mng = plt.get_current_fig_manager()
# mng.resize(*mng.window.maxsize())
plt.plot([], [], color='r', label = 'Estimated Unemployment Rate (%)')
plt.plot([], [], color='g', label = 'Estimated Labour Participation Rate (%)')
plt.plot([], [], color='b', label = 'Estimated Employed Rate (%)')
datex = [item[1] for item in S_Buc]
arr1 = [item[2] for item in S_Buc]
arr2 = [item[3] for item in S_Buc]
arr3 = [item[4] for item in S_Buc]
plt.stackplot(datex, arr1, arr3, arr2, colors= ['r', 'g', 'b'])
plt.title(state_in)
plt.figlegend(loc='upper right')
plt.show()

#Pie
# mng = plt.get_current_fig_manager()
# mng.resize(*mng.window.maxsize())
labels = 'Estimated Unemployment Rate (%)', 'Estimated Labour Participation Rate (%)', 'Estimated Employed Rate (%)'
sections = [arr1[7], arr3[7], arr2[7]]
colors = ['r', 'b', 'g']
plt.pie(sections, labels=labels, colors=colors,startangle=90,explode = (0, 0.1, 0),autopct = '%1.2f%%')
plt.title(" State : " +state_in + ", Dated on :" + datex[7])
plt.figlegend(loc='upper right')
plt.show()

#Line
# mng = plt.get_current_fig_manager()
# mng.resize(*mng.window.maxsize())
plt.plot(datex, arr1, label='Estimated Unemployment Rate (%)', color='Red', linestyle='dashed', linewidth = 1,
         marker='^', markerfacecolor='Red', markersize=6)
for x,y in zip(datex,arr1):
    label = y
    plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,10),ha='center')
plt.plot(datex, arr3, label='Estimated Labour Participation Rate (%)',color='blue', linestyle='dashed', linewidth = 1,
         marker='o', markerfacecolor='blue', markersize=6)
for x,y in zip(datex,arr3):
    label = y
    plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,10),ha='center')
plt.plot(datex, arr2, label='Estimated Employed Rate (%)',color='green', linestyle='dashed', linewidth = 1,
         marker='s', markerfacecolor='green', markersize=6)
for x,y in zip(datex,arr2):
    label = y
    plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,10),ha='center')
plt.plot()

plt.xlabel("Date")
plt.ylabel("Rate(%)")
plt.title(state_in)
plt.figlegend(loc='upper right')

plt.show()

#Subplot
fig, (ax1, ax2, ax3) = plt.subplots(3)
# fig.suptitle('Vertically stacked subplots')
ax1.plot(datex, arr1, label='Estimated Unemployment Rate (%)', color='Red', linestyle='dashed', linewidth = 1,
         marker='^', markerfacecolor='Red', markersize=6)
for x,y in zip(datex,arr1):
    label = y
    plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,10),ha='center')
ax1.set_title('Estimated Unemployment Rate (%)',fontsize = 15)
ax2.plot(datex, arr3, label='Estimated Labour Participation Rate (%)',color='blue', linestyle='dashed', linewidth = 1,
         marker='o', markerfacecolor='blue', markersize=6)
for x,y in zip(datex,arr3):
    label = y
    plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,10),ha='center')
ax2.set_title('Estimated Labour Participation Rate (%)')
ax3.plot(datex, arr2,label='Estimated Employed Rate (%)',color='green', linestyle='dashed', linewidth = 1,
         marker='s', markerfacecolor='green', markersize=6)
for x,y in zip(datex,arr2):
    label = y
    plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,10),ha='center')
ax3.set_title('Estimated Employed Rate (%)')
plt.subplots_adjust(hspace=0.5)
# mng = plt.get_current_fig_manager()
# mng.resize(*mng.window.maxsize())
plt.figlegend(loc='upper right')
plt.show()
