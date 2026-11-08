import kagglehub
import csv
from pathlib import Path

# Download latest version
path = kagglehub.dataset_download("davidcariboo/player-scores")

print("Path to dataset files:", path)

# Read the player information from the downloaded dataset folder.
source_file = Path(path) / 'players.csv'
output_file = Path(__file__).parent / 'player_scores.csv'

with open(source_file, 'r', newline='', encoding='utf-8') as datafile:
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(datafile)
        writer = csv.writer(csvfile)
        writer.writerows(reader)  # Copy the header and every data row.

print(f"CSV file created successfully: {output_file}")
