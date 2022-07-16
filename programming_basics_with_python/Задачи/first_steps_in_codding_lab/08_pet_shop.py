# 8.	Зоомагазин
# Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и котки.  Храната се пазарува
# от зоомагазин, като една опаковка храна за кучета е на цена 2.50 лв, а опаковка храна за котки струва 4 лв.
# Вход
# От конзолата се четат 2 реда:
# 1.	Броят на опаковките храна за кучета – цяло число в интервала [0… 100]
# 2.	Броят на опаковките храна за котки –  цяло число в интервала [0… 100]
# Изход
# На конзолата се отпечатва:
# "{крайната сума} lv."
# Примерен вход и изход
# вход	изход		 вход	изход
# 5
# 4	    28.5 lv.		 13
#                         9
# 	                       68.5 lv.

number_of_packs_for_dogs = int(input())
number_of_packs_for_cats = int(input())
price_for_dogs_food = number_of_packs_for_dogs * 2.50
price_for_cat_food = number_of_packs_for_cats * 4

final_price = price_for_dogs_food + price_for_cat_food
print(f'{final_price} lv.')
