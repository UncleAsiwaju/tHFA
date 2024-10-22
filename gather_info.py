import os
import pandas as pd
import numpy as np

countries = {
    'GHA': 'ghana',
    'GMB': 'gambia',
    # 'IDN': 'indonesia',
    'LBR': 'liberia',
    'MDG': 'madagascar',
    'MWI': 'malawi',
    'NGA': 'nigeria',
    'UGA': 'uganda',
    'COG': 'congo',
    'MOZ': 'mozambique'
}

table = pd.DataFrame([])
version = "2.10"
indicator = 'lab'
target = ['test-capac','score with lab','score without lab']

for code, country in countries.items():
    pivot_file = pd.read_csv(f"./output/{code}/{country}_pivot_v{version}.csv",index_col=[0,1])
    lab = pivot_file.loc[[('COUNTRY','AVERAGE')]][target]
    for level in ['PRIMARY', 'SECONDARY', 'TERTIARY']:
        part = pivot_file.loc[[(f'{level}','General')]][target]
        lab = pd.concat([lab,part])

    flattened_values = lab.values.flatten()
    flattened_columns = [f'{idx[0]}_{col}' for idx in lab.index for col in lab.columns]

    # Create the flattened DataFrame
    flattened_df = pd.DataFrame([flattened_values], columns=flattened_columns, index=[country])
    table = pd.concat([table,flattened_df])

table.to_csv(f"./output/updated-{indicator}-figures.csv")
print(table)