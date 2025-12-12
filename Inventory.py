import pandas as pd
file = pd.read_excel("stock.xlsx")
total_low = 0
total_price = 0

stock = file['stock']
parts = file['part']
price = file['price']

stock_low_idx = file.index[stock < 15]

for e in stock_low_idx:
    total_low += 1
    file.loc[file['stock'] < 15, 'stock'] = 20
    total_price += file.loc[file['stock'] < 15, 'price'].iloc[0]
    print(file.loc[e])

print("\n" + total_price)