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
# enumerate- allows us to iterate through a sequence but it keeps track of both the index and the element
# print(dictionary)
# Code to save Dataframe of dictionary in Local machine
# out_file = open('dictionary.txt', 'wt')
# out_file.write(str(dictionary))
# out_file.close()

All_region = list(set(Regc))
All_region = sorted(All_region)
# User options
print(All_region)

mapped = []
# To fetch data from dictionary.
for i, j in dictionary.items():
    for key in j:
        # print(key+':',j[key])
        # print(j[key])
        mapped.append(j[key])

new_items = [mapped[i:i+5] for i in range(0, len(mapped), 5)]
# defining input from user
state_in = input("Visualise which state from the above?: ")
# Temp bucket for state given by user
S_Buc = []
for row in new_items[:]:
    if row[0] == state_in:
        sorted(S_Buc)
        S_Buc.append(row)

# Plotting.
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10})
date_x = [item[1] for item in S_Buc]
arr1 = [item[2] for item in S_Buc]
arr2 = [item[3] for item in S_Buc]
arr3 = [item[4] for item in S_Buc]
# stack-plot
plt.plot([], [], color='r', label='Estimated Unemployment Rate (%)')
plt.plot([], [], color='g', label='Estimated Labour Participation Rate (%)')
plt.plot([], [], color='b', label='Estimated Employed Rate (%)')
plt.stackplot(date_x, arr1, arr3, arr2, colors=['r', 'g', 'b'])
plt.title(state_in)
plt.figlegend(loc='upper right')

plt.show()

# Pie
labels = 'Estimated Unemployment Rate (%)', 'Estimated Labour Participation Rate (%)', 'Estimated Employed Rate (%)'
sections = [arr1[7], arr3[7], arr2[7]]
colors = ['r', 'b', 'g']
plt.pie(sections, labels=labels, colors=colors, startangle=90, explode=(0, 0.1, 0), autopct='%1.2f%%')
plt.title(" State : " + state_in + ", Dated on :" + date_x[7])
plt.figlegend(loc='upper right')
plt.show()

# Line
plt.plot(date_x, arr1, label='Estimated Unemployment Rate (%)', color='Red', linestyle='dashed', linewidth=1,
         marker='^', markerfacecolor='Red', markersize=6)
for x, y in zip(date_x, arr1):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
plt.plot(date_x, arr3, label='Estimated Labour Participation Rate (%)', color='blue', linestyle='dashed', linewidth=1,
         marker='o', markerfacecolor='blue', markersize=6)
for x, y in zip(date_x, arr3):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
plt.plot(date_x, arr2, label='Estimated Employed Rate (%)', color='green', linestyle='dashed', linewidth=1,
         marker='s', markerfacecolor='green', markersize=6)
for x, y in zip(date_x, arr2):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
plt.plot()
plt.xlabel("Date")
plt.ylabel("Rate(%)")
plt.title(state_in)
plt.figlegend(loc='upper right')
plt.show()

# Subplot
fig, (ax1, ax2, ax3) = plt.subplots(3)
ax1.plot(date_x, arr1, label='Estimated Unemployment Rate (%)', color='Red', linestyle='dashed', linewidth=1,
         marker='^', markerfacecolor='Red', markersize=6)
for x, y in zip(date_x, arr1):
    label = y
    ax1.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
ax1.set_title('Estimated Unemployment Rate (%)', loc='left')
ax2.plot(date_x, arr3, label='Estimated Labour Participation Rate (%)', color='blue', linestyle='dashed', linewidth=1,
         marker='o', markerfacecolor='blue', markersize=6)
for x, y in zip(date_x, arr3):
    label = y
    ax2.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
ax2.set_title('Estimated Labour Participation Rate (%)', loc='left')
ax3.plot(date_x, arr2, label='Estimated Employed Rate (%)', color='green', linestyle='dashed', linewidth=1,
         marker='s', markerfacecolor='green', markersize=6)
for x, y in zip(date_x, arr2):
    label = y
    ax3.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
ax3.set_title('Estimated Employed Rate (%)', loc='left')
plt.subplots_adjust(hspace=0.5)
plt.figlegend(loc='upper right')
plt.show()

top_list = new_items[7::8]
# print(len(top_list))
for row in top_list:
    if row[0] == 'India':top_list.remove(row)
# print(len(top_list))
# print(top_list)

eol_state = new_items[7::8]
for row in eol_state:
    if row[0] == 'India':
        eol_state.remove(row)

# Get Top N elements from Records
res = sorted(eol_state, key=lambda x: x[2], reverse=True)[:10]
res1 = sorted(eol_state, key=lambda x: x[3], reverse=True)[:10]
res2 = sorted(eol_state, key=lambda x: x[4], reverse=True)[:10]
res_d1 = {sub[0]: sub[2] for sub in res}
res_d2 = {sub[0]: sub[3] for sub in res1}
res_d3 = {sub[0]: sub[4] for sub in res2}

#  Bar plot Estimated Unemployment Rate (%)
courses = list(res_d1.keys())
values = list(res_d1.values())
fig = plt.figure(figsize=(5, 2.5))
plt.bar(courses, values, color='red', width=0.5)
plt.xlabel("State")
plt.ylabel("Rate (%)")
plt.title("Top 10 Estimated Unemployment Rate (%)")
for x,y in zip(courses,values):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()

#  Bar plot Estimated Employed Rate (%)
courses = list(res_d2.keys())
values = list(res_d2.values())
fig = plt.figure(figsize=(5, 2.5))
plt.bar(courses, values, color='green', width=0.5)
plt.xlabel("State")
plt.ylabel("Rate (%)")
plt.title("Top 10 Estimated Employed Rate (%)")
for x,y in zip(courses,values):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()

#  Bar plot Estimated Labour Participation Rate (%)
courses = list(res_d3.keys())
values = list(res_d3.values())
fig = plt.figure(figsize=(5, 2.5))
plt.bar(courses, values, color='blue', width=0.5)
plt.xlabel("State")
plt.ylabel("Rate (%)")
plt.title("Top 10 Estimated Labour Participation Rate (%)")
for x,y in zip(courses,values):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()

# Histogram
res11 = sorted(new_items, key=lambda x: x[2], reverse=True)
res12 = sorted(new_items, key=lambda x: x[3], reverse=True)
res13 = sorted(new_items, key=lambda x: x[4], reverse=True)
res_d11 = {sub[0]: sub[2] for sub in res11}
res_d12 = {sub[0]: sub[3] for sub in res12}
res_d13 = {sub[0]: sub[4] for sub in res13}
EUR = list(res_d11.values())
EER = list(res_d12.values())
ELR = list(res_d13.values())
plt.hist(EUR, label='Estimated Unemployment Rate (%)', alpha=.7,color='red', edgecolor='red', density=True, histtype='stepfilled', stacked=True)
plt.hist(EER, label='Estimated Employed Rate (%)', alpha=0.7, color='green', edgecolor='green',density=True, histtype='stepfilled', stacked=True)
plt.hist(ELR, label='Estimated Labour Participation Rate (%)', alpha=.7, color='blue', edgecolor='blue', density=True, histtype='stepfilled', stacked=True)
plt.figlegend(loc='upper right')
plt.title("Histogram of Employment Status affected by Covid19")
plt.xlabel("Rate (%)")
plt.show()
