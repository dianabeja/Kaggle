import pandas as pd

dataframe = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

dataframe2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

dataframe3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print(dataframe)
print(dataframe2)