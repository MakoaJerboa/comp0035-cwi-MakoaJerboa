# Data preparation and understanding code

# Importing libraries
from pathlib import Path
import pandas as pd

def csv_sort(
        worker_categories, worker_categories_friendly, df_prepared, column_label, 
        custom_column_label, column_label_2
        ):
    for i, category in enumerate(worker_categories):
        # Sorts the data by worker category
        category_df = df_dropped[df_dropped[column_label_2] == category]
        
        # Counts the number of people in each worker caterory and sorts it by area
        category_count = category_df.groupby(column_label).size().reset_index(name=worker_categories_friendly[i])
        
        # Since the area labels are constant, this section is only run once
        if i == 0:
            # Takes the only first column and gives it a simpler label
            df_prepared = category_count.rename(columns={column_label: custom_column_label}).drop(category_count.columns[[1]], axis=1)
        
        else:
            # For each loop after the first, adds the worker category column to the dataframe
            next_column = category_count.drop(category_count.columns[[0]], axis=1)
            df_prepared = df_prepared.join(next_column)
    return(df_prepared)

# Reads csv file and converts it to dataframe to be used throughout the code
csvfile = Path(__file__).parent.joinpath("data", "dataset.csv")
raw_data = pd.read_csv(csvfile)
df = pd.DataFrame(raw_data)

# Drops first 3 columns as I won't be using them
df_dropped = df.drop(['lsoa21cd', "lsoa21nm", "lad22cd"], axis = 1)

# Drops rows with missing values
df_dropped = df_dropped.dropna()

# This next section prepares the data by sorting
# the number of people in each working time bracket per area

# Sets worker categories in order and simpler names for them
worker_categories = [
    "Full-time: 49 or more hours worked","Full-time: 31 to 48 hours worked",
    "Part-time: 16 to 30 hours worked", "Part-time: 15 hours or less worked"
    ]
worker_categories_friendly = [
    "Hours worked: 49+", "Hours worked: 31-48", 
    "Hours worked: 16-30", "Hours worked: 1-15"
    ]

# Creates an empty dataframe to be filled later
df_prepared = pd.DataFrame()

# For each category of worker, takes the number of them and sorts it by area and adds it to the dataframe
df_prepared = csv_sort(
    worker_categories, worker_categories_friendly, df_prepared,
    "lad22nm", "Area", "hours_worked"
    )

print(df_prepared)

# Saves the prepared data to a csv file with the appropriate path and name
df_prepared.to_csv(Path(__file__).parent.joinpath("data", "dataset_prepared.csv"), index=False)

# For each category of worker, take the number of them and sorts it by occupation and adds it to the dataframe
df_prepared = csv_sort(
    worker_categories, worker_categories_friendly, df_prepared,
    "occupation", "Occupation", "hours_worked"
    )

print(df_prepared)
# Saves the prepared data to a csv file with the appropriate path and name
df_prepared.to_csv(Path(__file__).parent.joinpath("data", "dataset_prepared_2.csv"), index=False)