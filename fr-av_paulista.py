import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

# FILTRO DE PONTOS DE ÔNIBUS QUE POSSUEM UMA FREQUÊNCIA 
# MAIOR QUE 5 ÔNIBUS POR HORA EM HORÁRIOS DE PICO (7H-10H) E (17H-20H) 


# convert string to datatime (df: stop_times)
stop_times = pd.read_csv('dados\paradas\stop_times.txt', sep=',')
stop_times['arrival_time'] = pd.to_datetime(stop_times['arrival_time'])
stop_times['hour'] = stop_times['arrival_time'].dt.hour
print(stop_times.count())
# df stops
stops = pd.read_csv('dados\paradas\stops.txt', sep=',')

# merge stop_times & stops
events = pd.merge(stop_times, stops, on='stop_id')
print(events.count())
#events.to_csv('eventos.txt')

av_paulista1 = events[events['stop_name'].str.contains("Av. Paulista", case=False, na=False)]
print(av_paulista1.describe())
av_paulista2 = events[events['stop_desc'].str.contains("Av. Paulista", case=False, na=False)]
print(av_paulista2.describe())

av_paulista = pd.concat([av_paulista1,av_paulista2],ignore_index=True)

filter_es_morning = av_paulista.loc[(events['hour'] >= 7) & (av_paulista['hour'] < 9)].groupby('stop_id', as_index=False).count()
filter_es_morning = filter_es_morning[['stop_id', 'trip_id']]
filter_es_morning = filter_es_morning.rename(columns={'trip_id': 'qtd'})


print(av_paulista.describe())
print(filter_es_morning.describe())