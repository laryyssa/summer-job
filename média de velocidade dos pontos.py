import pandas as pd
import plotly.express as px

eventos = pd.read_csv('SAO_eventosparadas_230104.csv', sep=';', decimal=',')
eventos['avg_speed'] = eventos['avg_speed'].astype(float)

paradas = pd.read_csv('stops.txt', sep=',')

result = pd.merge(eventos, paradas, on='stop_id').groupby('stop_id').mean()
    # já está no padrão Inner => só inclui na tabela aqueles que estão nas 2 tabelas

print(result.head())

fig = px.scatter(result, x='stop_lon', y='stop_lat',
                 color='avg_speed')

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)

fig.show() 
