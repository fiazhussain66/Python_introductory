a = 3
b = 4
c = 5

abc_string = str(a)+str(b)+str(c)


print(abc_string)
print(type(str(abc_string)))

# to check the path


import pandas as pd


path = r"C:\Users\Fiaz Hussain\Desktop\python_tutorials\data"
file_name = r"\german_credit_data.csv"
data_set = pd.read_csv(path + file_name, index_col = 0)

print(data_set.head(3))

print(data_set.columns)