import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df1 = pd.read_excel(xlsx, header=0)
print(df1)
df2 = df1.groupby(['Rok'])['Liczba'].sum()
print(df2)
df2.plot(color='y', linestyle='--')
plt.show()
df3 = df1[(df1.Plec == 'M')]['Liczba'].sum()
df4 = df1[(df1.Plec == 'K')]['Liczba'].sum()
etykiety = ['Urodzone kobiety', 'Urodzeni mezczyzni']
wartosci = [df4, df3]
plt.bar(etykiety, wartosci,  color='black')
plt.ylabel('Ilosc narodzin w mln')
plt.show()

df2 = df1[(df1['Rok'] >= 2012)].groupby(['Plec']).agg({'Liczba': {'sum'}})
etykiety = ['Dziewczynki', 'Chłopcy']
wykres = df2.plot.pie(figsize=(5, 5),
                      subplots=True,
                      labels=etykiety,
                      startangle=90,
                      shadow=True,
                      wedgeprops={'edgecolor': 'white'},
                      colors=['g', 'r'])
plt.title('Urodzenia w ostatnich 5 latach')
plt.show()
df3 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
df4 = df3.groupby(['Sprzedawca'])[['idZamowienia']].count().plot(kind='bar',
                                                                 color='purple',
                                                                 legend=None,
                                                                 title='Ilosc zamowien zlozonych'
                                                                       ' przez poszczegolnych sprzedawcow')
plt.ylabel('Ilosc zlozonych zamowien')
plt.show()
