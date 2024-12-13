# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:13:12 2024

@author: Lenovo
"""

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

with open("hasil_data.txt", "w") as file:
    file.write("Berikut Data Framenya:\n\n")
    file.write(data.to_string(index=False))
    file.write("\n\nBerikut Data Mean:\n\n")
    file.write(mean_data.to_string(header=True))
    file.write("\n\nBerikut Data Standard Deviation:\n\n")
    file.write(std_data.to_string(header=True))

mean_data.to_csv("NegaraMean.csv", index=True) 
std_data.to_csv("NegaraStandarDeviasi.csv", index=True)

print("\nFile Berhasil Dibuat")

