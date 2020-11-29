import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import csv
with open('EVs_data_base.csv', 'r', newline='') as f:
    rows = list(csv.reader(f, delimiter=';'))
    for row in rows[1:]:
        row[5]= int(row[5])
    
years=[]
chargingType=[]
for row in rows[1:]:
    if row[5]!='':years.append(row[5])
    if row[2]!='None': chargingType.append(row[2])
    if row[6]!='None': chargingType.append(row[6])
chargingType=list(dict.fromkeys(chargingType))
chargingType.sort()
years=list(dict.fromkeys(years))
years.sort()
print (chargingType)
x=[]
y=[]
z=[]
for entry in years:
    for elements in chargingType:
        x.append(entry)
        y.append(elements)
        z.append(1)
index=0
for year in years:
    for chtype in chargingType:
        for row in rows:
            if row[5]==year and row [2]==chtype:
                z[index]=z[index]+20
            if row[5]==year and row [6]==chtype:
                z[index]=z[index]+20
        index=index+1

print(len(x),len(y))
#z=# Count of cars
fig = go.Figure(data=[go.Scatter(
    x=x, y=y,
    mode='markers',
    marker_size=z)
])
fig.update_layout(
    title='Europe trends in EV Charging technology ',
    xaxis=dict(
        title='year',
        gridcolor='white',
    ),
    yaxis=dict(
        title='Charging type and power',
        gridcolor='white',
    ))
fig.show()
