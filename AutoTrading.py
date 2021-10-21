from TradingTools import Account
from TradingTools import Currency
import time

class AutoTrading:
    def __init__(self, targetBuyPrice = 0, targetSellPrice = 0, amountBuy = 0, amountSell = 0, currency = Currency.BTC):
        self.account = Account()
        self.targetBuyPrice = targetBuyPrice
        self.targetSellPrice = targetSellPrice
        self.amountBuy = amountBuy
        self.amountSell = amountSell
        self.currency = currency

    def displayParametrs(self):
        print("+++ Trading Parametrs +++")
        print("-------------------------")
        print("Target buy price  : "+ str(self.targetBuyPrice))
        print("Target sell price : "+ str(self.targetSellPrice))
        print("Amout buy (USD)   : "+ str(self.amountBuy))
        if self.currency == Currency.BTC:
            print("Amout sell (BTC)   : "+ str(self.amountSell))
        else:
            print("Amout sell (ETH)   : "+ str(self.amountSell))


    def configParametrs(self):
        targetBuyPrice = input("Input target buy price: ")
        targetSellPrice = input("Input target sell price: ")
        amountBuy  = input("Input amout to transaciotn: ")
        currency = input("Input currency: ")
        
        self.targetSellPrice = float(targetSellPrice)
        self.targetBuyPrice = float(targetBuyPrice)
        self.amountBuy = float(amountBuy)
        self.amountSell = float(amountBuy)/float(targetBuyPrice)
        if str.upper(currency) == "BTC":
            self.currency = Currency.BTC
        elif upper(currency) == "ETH":
            self.currency = Currency.ETH
        else:
            print("There is no "+currency+" currency...")

    def autoBuy(self):
        bought = False
        while bought == False:
            self.account.update()
            actualPrice = 0
            if self.currency == Currency.BTC:
                actualPrice = self.account.priceBTC
            else:
                actualPrice = self.account.priceETH

            self.account.displayAccount()
            self.displayParametrs()

            if self.targetBuyPrice >= actualPrice:
                self.account.trade(self.amountBuy, Currency.USD, self.currency)
                self.amountSell = self.amountBuy/actualPrice
                print("\n BOUGHT ")
                bought = True
            else:
                time.sleep(59)

    def autoSell(self):
        sold = False
        while sold == False:
            self.account.update()
            actualPrice = 0
            if self.currency == Currency.BTC:
                actualPrice = self.account.priceBTC
            else:
                actualPrice = self.account.priceETH

            self.account.displayAccount()
            self.displayParametrs()

            if self.targetBuyPrice <= actualPrice:
                self.account.trade(self.amountSell, self.currency, Currency.USD)
                print("\n SOLD")
                sold = True
            else:
                time.sleep(59)

    def autoTrade(self):
        self.autoBuy()
        self.autoSell()

    def tradeMenu(self):
        accept = False
        while accept == False:
            self.account.displayAccount()
            self.displayParametrs()
            print("MENU")
            print("===============")
            print("1. Change parametrs")
            print("2. Make order")
            print("0. Exit")
            choice = input("Your choice: ")
            if choice == '1':
                self.configParametrs()
            elif choice == '2':
                self.autoTrade()
            elif choice == '0':
                accept = True



        

