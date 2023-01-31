import pandas as pd
import plotly.express as px


eventos = pd.read_csv('dados/SAO_eventosparadas_230104.csv', sep=';', decimal=',')
eventos['avg_speed'] = eventos['avg_speed'].astype(float)

paradas = pd.read_csv('dados/stops.txt', sep=',')

qtd_paradas = pd.merge(eventos, paradas, on='stop_id').groupby('stop_id', as_index=False).count()
qtd_paradas = qtd_paradas[['stop_id', 'trip_id']]
qtd_paradas = qtd_paradas.rename(columns={'trip_id': 'qtd'})

#print(qtd_paradas)

qtd_avgVel_paradas = pd.merge(eventos, paradas, on='stop_id').groupby('stop_id', as_index=False).mean()
    # já está no padrão Inner => só inclui na tabela aqueles que estão nas 2 tabelas
qtd_avgVel_paradas = pd.merge(qtd_avgVel_paradas, qtd_paradas, on='stop_id')
print(qtd_avgVel_paradas.head())

#print(qtd_avgVel_paradas.head())

fig = px.scatter_mapbox(qtd_avgVel_paradas,
                        lon= qtd_avgVel_paradas['stop_lon'],
                        lat= qtd_avgVel_paradas['stop_lat'],
                        zoom = 9.5,
                        color= qtd_avgVel_paradas['avg_speed'],
                        size= qtd_avgVel_paradas['qtd'], # posso fazer tamanho por número de rotas que passaram por aqui
                        width= 1200,
                        height= 900,
                        title= 'Média de Velocidade dos Pontos de ônibus')

""" fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
) """

fig.update_layout(mapbox_style='open-street-map')
#fig.update_layout(margin={'r':0, 't':50, 'l':0, 'b':10})

fig.update_layout(
    autosize=False,
    width=1000,
    height=1000,)

fig.show() 
