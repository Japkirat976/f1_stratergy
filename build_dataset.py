import fastf1
import pandas as pd
import os

# =========================
# CONFIG
# =========================
YEAR = 2023
CACHE_DIR = "cache"
OUTPUT_FILE = f"f1_strategy_{YEAR}.csv"

# =========================
# ENABLE CACHE
# =========================
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

fastf1.Cache.enable_cache(CACHE_DIR)

# =========================
# LOAD SEASON SCHEDULE
# =========================
schedule = fastf1.get_event_schedule(YEAR)

full_data = []

print(f"\nBuilding dataset for {YEAR} season...\n")

for _, event in schedule.iterrows():

    # Skip sprint weekends for now (simplify v1)
    if event['EventFormat'] != 'conventional':
        continue

    race_name = event['EventName']
    round_number = event['RoundNumber']

    print(f"Loading Round {round_number}: {race_name}")

    try:
        session = fastf1.get_session(YEAR, race_name, 'R')
        session.load()
    except Exception as e:
        print(f"Skipping {race_name} due to error: {e}")
        continue

    laps = session.laps
    # Count Safety Car laps (TrackStatus contains '4' during SC)
    sc_laps = laps[laps['TrackStatus'].astype(str).str.contains('4')]
    safety_car_count = len(sc_laps)

    # Get race-level features
    weather = session.weather_data
    avg_track_temp = weather['TrackTemp'].mean()
    avg_air_temp = weather['AirTemp'].mean()

    race_laps = session.total_laps
    results = session.results

    for driver in laps['Driver'].unique():

        driver_laps = laps[laps['Driver'] == driver]

        if driver_laps.empty:
            continue

        num_stints = driver_laps['Stint'].nunique()

        if num_stints <= 1:
            continue

        stint_data = driver_laps.groupby('Stint').agg({
            'Compound': 'first',
            'LapNumber': ['min']
        })

        compounds = stint_data['Compound']['first'].tolist()
        stint_starts = stint_data['LapNumber']['min'].tolist()
        pit_laps = stint_starts[1:]
        
        first_compound = compounds[0]
        num_stops = num_stints - 1
        first_pit_lap = pit_laps[0] if len(pit_laps) > 0 else None

        # Calculate degradation rate (first stint only)
        first_stint = driver_laps[driver_laps['Stint'] == 1]

        if len(first_stint) > 5:
            lap_times = first_stint['LapTime'].dt.total_seconds()
            degradation = lap_times.diff().mean()
        else:
            degradation = None

        # Get grid position
        try:
            grid_position = results[
                results['Abbreviation'] == driver
            ]['GridPosition'].values[0]
            grid_percentile = grid_position / 20
        except:
            grid_position = None
            grid_percentile = None

        full_data.append({
            "Year": YEAR,
            "Round": round_number,
            "GridPercentile": grid_percentile,
            "TrackTemp": avg_track_temp,
            "AirTemp": avg_air_temp,
            "TotalLaps": race_laps,
            "SafetyCarLaps": safety_car_count,
            "DegradationRate": degradation,
            "First_Compound": first_compound,
            "Num_Stops": num_stops,
            "First_Pit_Lap": first_pit_lap
        })

# =========================
# CREATE DATAFRAME
# =========================
season_df = pd.DataFrame(full_data)

print("\nDataset Preview:")
print(season_df.head())

print("\nTotal rows:", len(season_df))

# =========================
# SAVE TO CSV
# =========================
season_df.to_csv(OUTPUT_FILE, index=False)

print(f"\nDataset saved as {OUTPUT_FILE}")
