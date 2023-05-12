import pandas as pd

# read excel file nad put it into dataframe
df = pd.read_excel('supermarket_sales.xlsx')

# double square brackets to select multiple columne
df = df[['Gender', 'Product line', 'Total']]

# create pivot table of how much each gender spend in each product line
# so the:
# index must be Gender
# column is Product line
# values are Total
# use aggregate aggfunc function to sum
# round them to one decimal number
pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(1)

# now export it to excel file named pivot_table, first sheet called Report, starting in row 4
pivot_table.to_excel('pivot_table.xlsx','Report', startrow=4)