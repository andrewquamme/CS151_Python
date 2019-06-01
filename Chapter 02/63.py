price = float(input("Item price: "))
discountPercent = 30
markdown = (discountPercent / 100) * price
price -= markdown
print(round(price,2))
