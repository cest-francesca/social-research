import pdb # this means python debugger

from ucimlrepo import fetch_ucirepo

print("Hello Fran and George. Dont worry, stuff is happening")

# fetch dataset
contraceptive_method_choice = fetch_ucirepo(id=30)

# data (as pandas dataframes)
X = contraceptive_method_choice.data.features
y = contraceptive_method_choice.data.targets




# metadata
print(contraceptive_method_choice.metadata)

# variable information
print(contraceptive_method_choice.variables)

# To write a pandas dataframe back to disk as a CSV
X.to_csv('features.csv')

# To write to excel
X.to_excel('contraceptive_method_choice_variables.xlsx')
