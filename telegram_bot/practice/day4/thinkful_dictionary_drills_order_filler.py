def fillable(stock, merch, n):
    if stock.get(merch) is not None:
        return stock.get(merch) >= n
    else:
        return False

#  tests
stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 }
print(fillable(stock, 'football', 3))
print(fillable(stock, 'leggos', 2))
print(fillable(stock, 'action figure', 1))