import pandas as pd
import ipywidgets as widgets
from ipywidgets import interact
import plotly.graph_objects as go
import plotly.express as px
# Set ipython's max row display
pd.set_option('display.max_row', 1000)


#Bubble Map Code
@interact
def display_widget(dt=widgets.DatePicker(description='Date', disabled=False, value=pd.to_datetime('01/27/2020'))):
    data = df1
    #delete NANs
    data.dropna(inplace=True)
    
    #Date picker filters data
    data = data.query("ObservationDate==@dt")
    
    #Create a new column to display on the graph
    data['text'] = data['Province_State'] + ' Confirmed Cases: ' + data['Confirmed'].astype(str)
    
    
    limits = [(0,100000)]
    
    #set Bubble Color
    colors = ["crimson"]
    cities = []
    scale = 5000

    #Instantiate graph
    fig = go.Figure()

    #Add data points
    for i in range(len(limits)):
        lim = limits[i]
        df_sub = data[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = data['Longitude'],
            lat = data['Latitude'],
            text = data['text'],
            marker = dict(
                size = data['Confirmed'],
                color = colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))
    
    #Set title and land color
    fig.update_layout(
        title_text = 'Coronavirus Outbreak by the Day',
        showlegend = False,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(225, 225, 225)',
        )
    )
    
    #Display Figure
    fig.show()
