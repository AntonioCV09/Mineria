import pandas as pd

df = pd.read_csv("uanl_02_2024.csv")

df['fecha'] = pd.to_datetime({'year': df['anio'], 'month': df['mes'], 'day': 1})
