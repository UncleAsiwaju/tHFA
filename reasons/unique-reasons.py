import pandas as pd
import numpy as np


countries = [
    # 'GHA',
    # 'GMB',
    'IDN',
    # 'LBR',
    'MDG',
    # 'MWI',
    # 'NGA',
    # 'UGA',
]

for country in countries:
    file_path = f"./Updated tHFA data/tHFA_{country}.xlsx"


    # Load and treat file
    df = pd.read_excel(file_path, header=None)
    df.columns = df.iloc[0]
    df = df[1:]
    df.set_index('Q100', inplace=True)

    # Select reasons column and transform to text file

    q = [f'tHFA_D011_1_{i}' for i in range(1,6)]
    reasons = np.concatenate([df[q[j]].unique() for j in range(5)])
    reasons = reasons.astype(str)
    reasons = np.char.lower(reasons)
    unique_reasons = np.unique(reasons)
    unique_reasons

    np.savetxt(f'reasons_{country}.txt', unique_reasons, fmt='%s')
    print(f'Done for {country}')

# file_name = ''

# with open(file_name, 'w') as file:
#     # Write each string to the file, each on a new line
#     for string in unique_reasons:
#         file.write(string + '\n')