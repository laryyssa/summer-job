import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

# FILTRO DE PONTOS DE ÔNIBUS QUE POSSUEM UMA FREQUÊNCIA 
# MAIOR QUE 5 ÔNIBUS POR HORA EM HORÁRIOS DE PICO (7H-10H) E (17H-20H) 

# convert string to datatime (df: stop_times)
stop_times = pd.read_csv('dados\carioca\stop_times.txt', sep=',')
stop_times['arrival_time'] = pd.to_datetime(stop_times['arrival_time'])
stop_times['hour'] = stop_times['arrival_time'].dt.hour
print(stop_times.head())

# df stops
stops = pd.read_csv('dados\carioca\stops.txt', sep=',')
print(stops.head())

# merge stop_times & stops
events = pd.merge(stop_times, stops, on='stop_id')
print(events.head())


# filter events by time: 7h-10h & 17h-20h
filter_es_morning = events.loc[(events['hour'] >= 7) & (events['hour'] < 9)].groupby('stop_id', as_index=False).count()
filter_es_morning = filter_es_morning[['stop_id', 'trip_id']]
filter_es_morning = filter_es_morning.rename(columns={'trip_id': 'qtd'})

merge = pd.merge(stops,filter_es_morning, on='stop_id')
print(merge.describe())

merge_qtd = merge.loc[(merge['qtd'] >= 10)]
print(merge_qtd.describe())
""" 
fig = px.scatter(merge, x='stop_lon', y='stop_lat',
                 color='qtd')

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)

fig.show() """

fig = go.Figure(go.Scattermapbox(
    mode='markers',
    lon= merge['stop_lon'],
    lat= merge['stop_lat'],
    marker=dict(
        color= np.where(np.logical_and(merge['qtd'].values < 10, merge['qtd'] <= 10), 'blue', 'yellow')
    )
))

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(
    hovermode='closest',
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
#fig.show()



filter_es_afternoon = events.loc[(events['hour'] >= 17) & (events['hour'] < 20)]

# filter stops by frequency (5 buses by hour; 15 buses by 3 hours) 
#qtd_morning = filter_es_morning

filters = [filter_es_morning, filter_es_afternoon] 

filter_es = pd.concat(filters, ignore_index=True)