import pandas as pd
import numpy as np

## creating a dataframe for the data and reading the data

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK2/data/healthcare_data_cleaning.csv')

## understanding the data

column_names = df.columns.tolist()
print(column_names)

df_list = [df]

for idx, df in enumerate(df_list, start=1):
  print(f"Dataframe {idx}:")
  print("First 5 rows: ")
  print(df.head(5))
  print("\n" + "="*40 + "\n")
  print("Random sample: ")
  print(df.sample(5))

## cleaning data/ removing rows -> removing columns -> saving cleaned data

df.replace('missing', np.nan)
df_cleaned = df.dropna(inplace=True)
df_cleaned = df.dropna(axis = 1)
df_cleaned.to_csv('cleaned_healthcare_data_cleaning.csv', index=False)

print(df_cleaned.head(5))

## identifying and cleaning duplicates

duplicate_mask = df.duplicated()
duplicate_rows = df[duplicate_mask]
print(duplicate_rows)
duplicate_rows_counted = len(duplicate_rows)
print(duplicate_rows_counted)

## removing duplicate rows

df_cleaned_dupes = df_cleaned.drop_duplicates()
print(df_cleaned_dupes.head(5))
df_cleaned_dupes.to_csv('cleaned_healthcare_data_cleaning.csv', index=False)

duplicate_mask = df.duplicated()
duplicate_rows = df[duplicate_mask]
print(duplicate_rows)
duplicate_rows_counted = len(duplicate_rows)
print(duplicate_rows_counted)

## renaming column names, I should've used re

data = {'A': ['Patient Age', 'Gender', 'City of Residence', 'State of Residence', 'Has Insurance', 'Visited Last Month', 'Payment Method', 'Preferred Doctor', 'Disease Diagnosed', 'Medication Prescribed', 'Type of Appointment', 'Average Heart Rate', 'Average BP', 'Height (in cm)', 'Weight (in kg)', 'Payment Due ($)', 'Last Visit (days ago)', 'Visit Duration (mins)', 'Number of Tests', 'Prescription Cost ($)']}
df = pd.DataFrame(data)

new_column_names = {'B': ['Patient_Age', 'Gender', 'City', 'State', 'Insurnace_Boolean', 'Visted_Last_Month', 'Payment_Method', 'Preferred_Doctor', 'Diagnosis', 'Medication', 'Type_of_Appointment', 'Average_Heart_Rate', 'Average_Blood_Pressure', 'Height(CM)', 'Weight(KG)', 'Payment_Due($)', 'Last_Visit', 'Visit_Duration(MIN)', 'Tests_Used', 'Prescription_Cost']}

column_names = df.columns.tolist()
print(column_names)

threshold_high_heartrate = 100

df['Heart_Rate_Rating'] = df['Average_Heart_Rate'].apply(lambda x: 'Average' if x >= threshold_high_heartrate else 'High')

print(df[['Patient_Age', 'Average_Heart_Rate', 'Heart_Rate_Rating']].head(10))

## Random Groupby Usage

df.groupby('Average_Rate_Rating').function_to_apply(sum)

## Random Pivot Table Usage

df.pivot_table(index=False, columns='City', values='Average_Heart_Rate', aggfunc='mean')