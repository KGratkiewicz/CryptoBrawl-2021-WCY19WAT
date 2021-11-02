from Webside import Webside
from datetime import datetime
from Webside import Currency
import pandas as pd
import time

class VirtualAccount:
    def __init__(self):
        self.portfolioUSD = 1000000
        self.portfolioBTC = 0
        self.portfolioETH = 0

        data = pd.read_csv("Binance_BTCUSDT_minute3.csv");
        data = data.loc[:,['open']]
        data = data.head(80640)
        data = data.tail(10080)
        self.dataBTC = data

        data = pd.read_csv("Binance_ETHUSDT_minute3.csv");
        data = data.loc[:,['open']]
        data = data.head(80640)
        data = data.tail(10080
                         )
        self.dataETH = data

        self.index = 10079

        self.priceBTC = 0        
        self.priceETH = 0
        

        self.portfolioValueUSD = 0

    def update(self):
        self.priceBTC = float(self.dataBTC.iloc[self.index])
        self.priceETH = float(self.dataETH.iloc[self.index])
        self.portfolioValueUSD = self.portfolioBTC * self.priceBTC + self.portfolioETH * self.priceETH + self.portfolioUSD 
        self.index -= 1

    def trade(self, amount, currencyToSell, currencyToBuy):
        if currencyToSell == Currency.BTC and currencyToBuy == Currency.USD:
            self.sellBTC(amount)
        elif currencyToSell == Currency.ETH and currencyToBuy == Currency.USD:
            self.sellETH(amount)
        elif currencyToSell == Currency.USD and currencyToBuy == Currency.BTC:
            self.buyBTC(amount)
        elif currencyToSell == Currency.USD and currencyToBuy == Currency.ETH:
            self.buyETH(amount)

    def buyBTC(self, amount):
        self.portfolioUSD -= amount
        self.portfolioBTC += amount/self.priceBTC

    def buyETH(self, amount):
        self.portfolioUSD -= amount
        self.portfolioETH += amount/self.priceETH

    def sellBTC(self, amount):
        self.portfolioBTC -= amount
        self.portfolioUSD += amount * self.priceBTC

    def sellETH(self, amount):
        self.portfolioETH -= amount
        self.portfolioUSD += amount * self.priceETH

    def displayAccount(self):
        print("\n### "+str(datetime.now())+" ###")
        print("Portfolio: ")
        print("--------------------------------")
        print("USD : " + str(self.portfolioUSD))
        print("BTC : " + str(self.portfolioBTC))
        print("ETH : " + str(self.portfolioETH))
        print("--------------------------------")
        print("Portfolio Value (USD): " + str(self.portfolioValueUSD))
        print("================================")
        print("Price: ")
        print("--------------------------------")
        print("BTCUSD : " + str(self.priceBTC))
        print("ETHUSD : " + str(self.priceETH))
        print("================================")

        

class Account:
    def __init__(self):
        self.webside = Webside()

        self.webside.refresh()
        
        self.portfolioUSD = self.webside.checkPortfolio(self.webside.xpathPortfolioUSD)
        self.portfolioBTC = self.webside.checkPortfolio(self.webside.xpathPortfolioBTC)
        self.portfolioETH = self.webside.checkPortfolio(self.webside.xpathPortfolioETH)

        self.priceBTC = self.webside.checkPrice(self.webside.xpathPriceBTC)
        self.priceETH = self.webside.checkPrice(self.webside.xpathPriceETH)

        self.priceCoinETH = self.webside.getCoinGekoBTC(self.webside.xpathCoin)
        self.priceCoinBTC = self.webside.getCoinGekoETH(self.webside.xpathCoin)

        self.portfolioValueUSD = self.portfolioBTC * self.priceBTC + self.portfolioETH * self.priceETH + self.portfolioUSD

    def trade(self, amount, currencyToSell, currencyToBuy):
        self.webside.setList(self.webside.idSellList, currencyToSell)
        self.webside.setList(self.webside.idBuyList, currencyToBuy)
        self.webside.insetStringIntoForm(self.webside.idAmount, amount)
        self.webside.clickButton(self.webside.xpathComfirmTransactionButton)

    def update(self):
        self.portfolioUSD = self.webside.checkPortfolio(self.webside.xpathPortfolioUSD)
        self.portfolioBTC = self.webside.checkPortfolio(self.webside.xpathPortfolioBTC)
        self.portfolioETH = self.webside.checkPortfolio(self.webside.xpathPortfolioETH)

        self.priceBTC = self.webside.checkPrice(self.webside.xpathPriceBTC)
        self.priceETH = self.webside.checkPrice(self.webside.xpathPriceETH)

        self.priceCoinETH = self.webside.getCoinGekoETH(self.webside.xpathCoin)
        self.priceCoinBTC = self.webside.getCoinGekoBTC(self.webside.xpathCoin)

        self.portfolioValueUSD = self.portfolioBTC * self.priceBTC + self.portfolioETH * self.priceETH + self.portfolioUSD

    def displayAccount(self):
        print("\n### "+str(datetime.now())+" ###")
        print("Portfolio: ")
        print("--------------------------------")
        print("USD : " + str(self.portfolioUSD))
        print("BTC : " + str(self.portfolioBTC))
        print("ETH : " + str(self.portfolioETH))
        print("--------------------------------")
        print("Portfolio Value (USD): " + str(self.portfolioValueUSD))
        print("================================")
        print("Price: ")
        print("--------------------------------")
        print("BTCUSD : " + str(self.priceBTC)+" :: "+str(self.priceCoinBTC))
        print("ETHUSD : " + str(self.priceETH)+" :: "+str(self.priceCoinETH))
        print("================================")
