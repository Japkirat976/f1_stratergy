import fastf1
import pandas as pd

fastf1.Cache.enable_cache('cache')

session = fastf1.get_session(2023,'Silverstone','R')
session.load()

print("Session loaded")

laps = session.laps

print(laps.head())
print(laps.columns)

nor_laps = laps[laps['Driver'] == 'NOR']
print(nor_laps[['LapNumber','Stint','Compound','TyreLife']].head())

print("Number of stints: ", nor_laps['Stint'].nunique())

driver = 'NOR'
driver_laps = laps[laps['Driver'] == driver]

stint_summary = driver_laps.groupby('Stint').agg({
    'Compound': 'first',
    'LapNumber': ['min', 'max']
})

print(stint_summary)
print("Number of stints: ", driver_laps['Stint'].nunique())

all_strategies = []

for driver in laps['Driver'].unique():
    driver_laps = laps[laps['Driver'] == driver]
    
    stint_data = driver_laps.groupby('Stint').agg({
        'Compound': 'first',
        'LapNumber': ['min', 'max']
    })
    
    num_stints = driver_laps['Stint'].nunique()
    
    compounds = stint_data['Compound']['first'].tolist()
    
    pit_laps = stint_data['LapNumber']['min'].tolist()[1:]  # ignore first stint
    
    all_strategies.append({
        'Year': 2023,
        'Race': 'British GP',
        'Driver': driver,
        'Num_Stints': num_stints,
        'Compounds': compounds,
        'Pit_Laps': pit_laps
    })

strategy_df = pd.DataFrame(all_strategies)
strategy_df = strategy_df[strategy_df['Num_Stints'] > 1]

print(strategy_df)
