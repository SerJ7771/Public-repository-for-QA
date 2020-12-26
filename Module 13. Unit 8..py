Price = 0
tickets = int(input("Сколько билетов хотите приобрести?\n"))
for i in range(tickets):
    age = int(input("Человеку какого возраста приобретается данный билет?\n"))
    if age < 18:
        Price += 0
    if 18 <= age < 25:
        Price += 990
    if age >= 25:
        Price += 1390
print('----------')
if tickets >= 3:
    discount_price = Price - ((Price / 100) * 10)
    print("Ваша сумма к оплате с учетом скидки в 10% составляет:", int(discount_price), 'руб')
else:
    print("Ваша сумма к оплате составляет:", Price, 'руб')