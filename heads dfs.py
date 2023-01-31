import pandas as pd

eventos = pd.read_csv('dados/SAO_eventosparadas_230104.csv', sep=';', decimal=',')
eventos['avg_speed'] = eventos['avg_speed'].astype(float)

paradas = pd.read_csv('dados/stops.txt', sep=',')

qtd_paradas = pd.merge(eventos, paradas, on='stop_id').groupby('stop_id', as_index=False).count()
qtd_paradas = qtd_paradas[['stop_id', 'trip_id']]
qtd_paradas = qtd_paradas.rename(columns={'trip_id': 'qtd'})

qtd_avgVel_paradas = pd.merge(eventos, paradas, on='stop_id').groupby('stop_id', as_index=False).mean()
    # já está no padrão Inner => só inclui na tabela aqueles que estão nas 2 tabelas
qtd_avgVel_paradas = pd.merge(qtd_avgVel_paradas, qtd_paradas, on='stop_id')

dfs = [eventos, paradas, qtd_paradas, qtd_avgVel_paradas]

for i in dfs:
    print(f'database: {i} ----------------------')
    print(i.head())
    print()
