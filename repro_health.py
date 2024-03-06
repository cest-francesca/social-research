from rich import print

import pandas as pd

file_path = "/Users/francescahearing/Desktop/WORK/2022 work/2023 work/2024 work/Coding/rep_rmnch/data.xlsx"

number_of_rows = 3000
df = pd.read_excel(file_path, nrows=number_of_rows)

print(f"All of the countries in the top {number_of_rows} rows are:")
print(df['setting'].unique())

print(df)

#accessing something which already exists,

print("The columns in the dataframe are: ")
print(df.columns)

print("The start of the file is:")
print(df.head(5))

print("The end of the file is:")
print(df.tail(5))

# the use of () normally denotes that it's a method, or a verb
print("The dataframe printed as a dictionary is: ")
# print(df.to_dict())

print(df['setting'])


# squiggly brackets for dictionaries
french_to_english_dictionary = {'ours': 'bear'}

print(french_to_english_dictionary["ours"])

print("The subcategories are: ")

print(df["dimension"].unique())

print("The variables are: ")

print(df["indicator_name"].unique())

# how many mothers who received postnatal care within two days of giving birth (%)

indicator_mask = df["indicator_name"] == "Newborns who received postnatal care within two days of delivery (%)"
print(indicator_mask)

print(indicator_mask.sum())

print(df[indicator_mask])

