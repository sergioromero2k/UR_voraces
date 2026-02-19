"""
Enunciado
Dado un valor V y un conjunto de monedas coins ordenadas de mayor a menor, 
    encuentra cuántas monedas de cada tipo necesitas para dar exactamente V.

Idea voraz
    Siempre tomar la moneda más grande posible.
    Restar su valor del total y repetir hasta llegar a 0.
"""

"""
def money_exchange(value, coins):
    exchange = [0]*len(coins)
    for i, coin in enumerate(coins):
        exchange[i] = value // coin;
        value = value % coin;
    return exchange
"""

"""
def money_exchange(value, coins):
    exchange = [0] * len(coins)
    i = len(coins) - 1
    while i >= 0 and value > 0:
        exchange[i] = value // coins[i]
        value = value % coins[i]
        i -= 1
    return exchange
"""
    
def money_exchange(value, coins):
    exchange = [0] * len(coins)
    i = 0
    while i < len(coins) and value >= 0:
        exchange[i] = value // coins[i]
        value = value % coins[i]
        i += 1
    return exchange


coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
value = 786
print(money_exchange(value, coins))