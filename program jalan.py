import pandas as pd

file_path = "Negara.csv" 
data = pd.read_csv(file_path)


print("Berikut Data Frame:")
print(data)


mean_data = data.groupby('Benua')[['Luas', 'Populasi']].mean()
std_data = data.groupby('Benua')[['Luas', 'Populasi']].std()


print("\nBerikut Data Mean:")
print(mean_data)


print("\nBerikut Data Standard Deviation:")
print(std_data)
