amount_money = 5
coin_denominations = [1,2,3,4]
temp_coins_seen = []
result = []

for coin in coin_denominations:
    if amount_money%coin == 0:
        result.append([[coin] * (amount_money/coin)])
    elif coin>amount_money:
        continue
    elif coin == amount_money:
        result.append(coin)
    temp_coins_seen.append(coin)
    for temp_coin in temp_coins_seen:
        if coin == temp_coin:
            continue
        if amount_money - coin == temp_coin:
            result.append([coin,temp_coin])

    print(result)

