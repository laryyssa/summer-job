import pandas as pd

eventos = pd.read_csv('dados/paradas/SAO_eventosparadas_230104.csv', sep=';', decimal=',')
eventos['avg_speed'] = eventos['avg_speed'].astype(float)

paradas = pd.read_csv('dados/paradas/stops.txt', sep=',')

qtd_onibus_por_ponto = pd.merge(eventos, paradas, on='stop_id').groupby('stop_id', as_index=False).count()
qtd_onibus_por_ponto = qtd_onibus_por_ponto[['stop_id', 'trip_id']]
qtd_onibus_por_ponto = qtd_onibus_por_ponto.rename(columns={'trip_id': 'qtd'})

qtd_avgVel_paradas = pd.merge(eventos, paradas, on='stop_id').groupby('stop_id', as_index=False).mean()
    # já está no padrão Inner => só inclui na tabela aqueles que estão nas 2 tabelas
qtd_avgVel_paradas = pd.merge(qtd_avgVel_paradas, qtd_onibus_por_ponto, on='stop_id')

dfs = [eventos, paradas, qtd_onibus_por_ponto, qtd_avgVel_paradas]

