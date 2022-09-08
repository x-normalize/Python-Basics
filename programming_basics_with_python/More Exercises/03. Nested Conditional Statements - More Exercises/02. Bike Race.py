# Предстои Вело състезание за благотворителност в което участниците са разпределени в младша("juniors")
# и старша("seniors") група. Парите се набавят от таксата за участие на велосипедистите.
# Според възрастовата група и вида на трасето на което ще се провежда състезанието, таксата е различна.
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши),
# таксата  намалява с 25%. Организаторите отделят 5% процента от събраната сума за разходи.
# Вход
# От конзолата се четат 2 числа и един стринг, всяко на отделен ред:
# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.
juniors = int(input())
seniors = int(input())
trace = input()
all_money = float()
if trace == "trail":
    all_money = juniors * 5.50 + seniors * 7
elif trace == "cross-country":
    all_money = juniors * 8 + seniors * 9.5
    if seniors + juniors >= 50:
        all_money *= 0.75
elif trace == "downhill":
    all_money = juniors * 12.25 + seniors * 13.75
elif trace == "road":
    all_money = juniors * 20 + seniors * 21.50
all_money *= 0.95
print(f'{all_money:.2f}')