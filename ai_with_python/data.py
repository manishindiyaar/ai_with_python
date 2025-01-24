import pandas as pd

# Reading the CSV file
data = pd.read_csv("my.csv")

# print(data)

print(data[data['Price']>=10000])
# Show all the cars from the 2015 
print(data[data["Year"]>=2015])


filtered_data = data[data["Year"]>=2015]
print(filtered_data["Price"].median())


