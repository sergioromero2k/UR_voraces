#!/usr/bin/env python3
from math import ceil


def main() -> None:
    try:
        qtw_money = input()
        if not qtw_money:
            return
        qtw_money = int(qtw_money)
        qtw_coins = input()
        if not qtw_coins:
            return
        qtw_coins = int(qtw_coins)
        coins = []
        for _ in range(qtw_coins):
            data_coin = input().split()
            name_coin = data_coin[0]
            exchange_to_euros = data_coin[1]
            exchange_available = []
            for _ in range(len(data_coin) - 2):
                exchange_available.append(float(input()))

            is_order = exchange_available == sorted(exchange_available, reverse=True)
            if not is_order:
                raise Exception('Must introduce the change in an orderly manner.')
            coins.append((name_coin, exchange_to_euros, exchange_available))
    except ValueError as e:
        print("Error Value: ", e)
    except Exception as e:
        print("Error: ", e)





if __name__ == "__main__":
    main()
