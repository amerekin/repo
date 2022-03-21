#Вывести на экран эти цены через запятую в одну строк
prices = [57.8, 46.51, 97, 55.06, 6.8, 33.21, 67.3, 55.62, 4.5, 6.7]

prices1 = []
for price in prices:
    prices1.append(f'"{int(price)} рублей, {round(((price - int(price))*100))} копеек"')
message = ', '.join(prices1)
print('цены через запятую в одну строку')
print(message)

# B. Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
prices.sort()
prices1 = []
for price in prices:
    prices1.append(f'"{int(price)} рублей, {round(((price - int(price))*100))} копеек"')
message = ', '.join(prices1)
print('цены, отсортированные по возрастанию')
print(message)

# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
prices = [57.8, 46.51, 97, 55.06, 6.8, 33.21, 67.3, 55.62, 4.5, 6.7]
prices.sort(reverse=True)
prices2 = []
for price in prices:
    prices2.append(f'"{int(price)} рублей, {round(((price - int(price))*100))} копеек"')
message = ', '.join(prices2)
print('цены отсортированные по убыванию')
print(message)

#D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по
# возрастанию, написав минимум кода?
prices = [57.8, 46.51, 97, 55.06, 6.8, 33.21, 67.3, 55.62, 4.5, 6.7]
prices.sort(reverse=True)
prices_max5 = prices[0:5]
prices3 = []
for price in prices_max5:
    prices3.append(f'"{int(price)} рублей, {round(((price - int(price))*100))} копеек"')
message = ', '.join(prices3)
print('цены пяти самых дорогих товаров')
print(message)