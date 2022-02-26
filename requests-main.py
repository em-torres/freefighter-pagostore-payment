import sys
import requests
from helpers.constants import URL, HEADER


class BuyDiamonds():
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount
        self.header = HEADER
        self.url = URL

def main():
    buy_diamonds = BuyDiamonds(sys.argv[1], sys.argv[2])
    r = requests.get(
            buy_diamonds.url,
            headers=buy_diamonds.header,
            params=buy_diamonds.id
        )
    print(r.text)
    return

if __name__ == "__main__":
    main()