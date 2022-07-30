print('Amount Due: 50')
amount_due = 50
coin_inserted = 0
while True:
    insert_coin = int(input('Insert Coin: '))
    if insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
        amount_due -= insert_coin
        coin_inserted += insert_coin
    else:
        print('Amount Due:',amount_due)
        continue
    if coin_inserted >= 50:
        change_owed = coin_inserted - 50
        print('Change Owed:',change_owed)
        break
    else:
        print('Amount Due:',amount_due)