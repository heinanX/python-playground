from math import *

shopper = 'June'
product = 'bar of soap'
product_price = 10
cash = 25
sum = product_price - cash


print(shopper + ' paid ' + str(cash) + ' dollars for a ' + product + '.')
print('Because the ' + product + ' only cost ' + str(product_price) + ', ' + shopper + ' was handed ' + str(abs(sum)) + ' in change' )

print(max(product_price, cash))
print(min(product_price, cash))

print(round(3.7))
print(floor(3.7))