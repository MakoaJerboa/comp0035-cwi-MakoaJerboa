# Data preparation and understanding code

# Importing libraries
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

'''
This is a function to clean the data to ensure no missing values are present

Inputs:
    df: The dataframe to be cleaned
'''
def clean(df):
    # Drops code columns as I won't be using them
    df = df.drop(['local authority code', "LSOA code"], axis = 1)
    # Drops rows with missing values
    df = df.dropna()
    return(df)

'''
This is a function to create a histogram of the data to check for outliers

Inputs:
    df: The dataframe to be plotted
'''
def histogram(df):
    # Creates a bar chart
    plt.bar(x=0, height=10, width=0.8, bottom=None, align='center', data=df)
    plt.show

'''
This is a function to add up all values for each area so the totals can be compared

Inputs:
    df: The dataframe to be summed
'''
def sum(df):
    # Groups the data by area and sums the values
    df = df.groupby("local authority name").sum()

    # Labels the first column as Area
    df = df.rename_axis("Area").reset_index()

    return(df)

'''
This is a function to print information about the dataframes to summarise them

Inputs:
    df: The dataframe to be summarised
'''
def summary(df):
    print("The number of rows and columns in the data frame are: ", df.shape)
    print("The data types of the columns are: ", "\n", df.dtypes)
    print("The first 5 rows of the data are: ", "\n" , df.head())
    print("The last 5 rows of the data are: ", "\n" , df.tail())

# Reads XLSX file and converts relevant sheets to dataframes
xlsx_file = Path(__file__).parent.joinpath("data", "dataset.xlsx")
raw_data_2011 = pd.read_excel(xlsx_file, sheet_name= "2011")
raw_data_2021 = pd.read_excel(xlsx_file, sheet_name= "2021")
df_2011 = pd.DataFrame(raw_data_2011)
df_2021 = pd.DataFrame(raw_data_2021)

# Calls function to clean data
df_2011 = clean(df_2011)
df_2021 = clean(df_2021)

# Passes the dataframe for each year into the function to sum the values
sum_2011 = sum(df_2011)
sum_2021 = sum(df_2021)

# Plots histograms of the data to ensure it is valid
histogram(df_2011)
histogram(df_2021)

# Summarises the data for each year to see general information about each dataframe
print("2011 data summary:",summary(sum_2011))
print("2021 data summary:",summary(sum_2021))

# Saves the dataframes to csv files for future use
sum_2011.to_csv(Path(__file__).parent.joinpath("data", "dataset_prepared_2011.csv"))
sum_2021.to_csv(Path(__file__).parent.joinpath("data", "dataset_prepared_2021.csv"))