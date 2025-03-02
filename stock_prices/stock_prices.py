#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = prices[1] - prices[0]
    for i in range(0, len(prices)-1):
        profit = 0
        for j in range(i+1, len(prices)-1):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                # elif profit < 0:
                #     max_profit = profit

    return max_profit


    


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
