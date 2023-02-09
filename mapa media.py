import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


eventos = pd.read_csv('dados/SAO_eventosparadas_230104.csv', sep=';', decimal=',')
eventos['avg_speed'] = eventos['avg_speed'].astype(float)

paradas = pd.read_csv('dados/stops.txt', sep=',')

qtd_paradas = pd.merge(eventos, paradas, on='stop_id').groupby('stop_id', as_index=False).count()
qtd_paradas = qtd_paradas[['stop_id', 'trip_id']]
qtd_paradas = qtd_paradas.rename(columns={'trip_id': 'qtd'})

qtd_avgVel_paradas = pd.merge(eventos, paradas, on='stop_id').groupby('stop_id', as_index=False).mean()
    # já está no padrão Inner => só inclui na tabela aqueles que estão nas 2 tabelas
qtd_avgVel_paradas = pd.merge(qtd_avgVel_paradas, qtd_paradas, on='stop_id')
print(qtd_avgVel_paradas.head())


fig = go.Figure(go.Scattermapbox(
    mode = "markers+text",
    lon = plane_df['lon'], lat = plane_df['lat'],
    marker = {'size': 20, 'symbol': "airport", 'allowoverlap': False,},
    hoverinfo='none',
    text = plane_df['Name'],
    textposition = "bottom right",
    textfont={'size':20, 'color':'blue'}
))

fig.add_trace(go.Scattermapbox(
    mode = "markers",
    lon = plane_df['lon'], lat = plane_df['lat'],
    marker = {'size': plane_df['Range']*50, 'sizemode':'area', 'symbol': "circle", 'opacity':0.3, 'allowoverlap': True,},
    hoverinfo='skip',
    text = plane_df['Name'],textposition = "bottom right"))

fig.update_layout(
    mapbox = {
        'accesstoken': token,
        'style': "streets",
        'bearing': 0,
        'pitch': 0,
        'center':{'lat':51, 'lon':8},
        'zoom': 4.6
    },
    showlegend = False)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()



