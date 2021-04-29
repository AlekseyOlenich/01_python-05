import pandas as pd

football = pd.read_csv('./data/data_sf.csv')

# print(football.info(verbose=True))

print(football.describe())
