import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df1 = pd.read_excel(xlsx, header=0)
print(df1)
df2 = df1.groupby(['Rok'])['Liczba'].sum()
print(df2)
df2.plot()
plt.show()
df3 = df1[(df1.Plec == 'M')]['Liczba'].sum()
df4 = df1[(df1.Plec == 'K')]['Liczba'].sum()
etykiety = ['Urodzone kobiety', 'Urodzeni mezczyzni']
wartosci = [df4, df3]
plt.bar(etykiety, wartosci)
plt.ylabel('Ilosc narodzin w mln')
plt.show()
