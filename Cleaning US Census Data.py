import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

us_census = glob.glob("state*.csv")

df_list = []
for fil in us_census:
  data = pd.read_csv(fil)
  df_list.append(data)

census_df = pd.concat(df_list)

print(census_df.columns)
print(census_df.dtypes)

# print(census_df.head())

gender_split = census_df.GenderPop.str.split('_')

census_df["Men"] = gender_split.str.get(0)
census_df["Women"] = gender_split.str.get(1)

census_df["Men"] = census_df.Men.str.replace(r'\D', '')
census_df["Women"] = census_df.Women.str.replace(r'\D', '')

census_df["Income"] = census_df.Income.str.replace("$", '', regex=True).astype(float)

census_df["Men"] = pd.to_numeric(census_df.Men)
census_df["Women"] = pd.to_numeric(census_df.Women)

print(census_df.head())

census_df = census_df.fillna(value={
"Women": census_df.TotalPop - census_df.Men
})

# print(census_df.duplicated())
census_df.drop_duplicates()

plt.scatter(census_df['Women'], census_df["Income"], color=["red","green"])
plt.xlabel("Women")
plt.ylabel("Income")
plt.show()
plt.cla()

