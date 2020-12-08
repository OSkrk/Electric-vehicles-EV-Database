import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import csv
# import CSV file
with open('EVs_data_base.csv', 'r', newline='') as f:
    rows = list(csv.reader(f, delimiter=','))
    for row in rows[1:]:
        row[5]= int(row[5])# transform column from string to int values
# Vectors initialization  
years=[]
chargingType=[]

for row in rows[1:]:
    if row[5]!='':years.append(row[5])
    if row[2]!='None': chargingType.append(row[2])
    if row[6]!='None': chargingType.append(row[6])
chargingType=list(dict.fromkeys(chargingType)) # remove repeated items
chargingType.sort()
years=list(dict.fromkeys(years)) # remove repeated items
years.sort()
#print (chargingType)
## Gathering data for plotting
x=[]
y=[]
z=[]
d={}
i=0
for entry in years:
    for elements in chargingType:
        x.append(entry)
        y.append(elements)
        z.append(0)
        d[repr([entry,elements])]=i
        i=i+1
entry=0
for row in rows: # For all rows
    entry=d.get(repr([row[5],row[2]])) # DC supported protocol and year
    if entry is not None:
        z[entry]=z[entry]+20
    entry=d.get(repr([row[5],row[6]])) # AC supported protocol and year
    if entry is not None:
        z[entry]=z[entry]+20

fig = go.Figure(data=[go.Scatter(
    x=x, y=y,
    mode='markers',
    marker=dict(
        color='rgb(65,127,216)'
    ),
    marker_size=z)
])
fig.update_layout(
    title='Europe trends in EV Charging technology ',title_font_size=40,
    xaxis=dict(
        title='year',
        gridcolor='white',
    ),
    yaxis=dict(
        title='Charging type and power',
        gridcolor='white',
    ),
    font=dict(
        size=18
    ))
fig.show()
