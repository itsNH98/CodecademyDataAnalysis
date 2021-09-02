import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

print(census.head())
print(census.dtypes)


census['birth_year'] = census.birth_year.replace('missing', '1967')
print(census.birth_year.unique())

census['birth_year'] = pd.to_numeric(census.birth_year)
print(census.dtypes)

print(census.birth_year.mean())

census.higher_tax = pd.Categorical(census['birth_year'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)

print(census.higher_tax.unique())
census['higher_tax'] = census['higher_tax'].cat.codes
print(census['higher_tax'].median())

census = pd.get_dummies(census, columns=['marital_status'])
print(census.head())



