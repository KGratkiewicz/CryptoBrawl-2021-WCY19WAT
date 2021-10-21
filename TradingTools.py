from Webside import Webside
from datetime import datetime
from Webside import Currency



class Account:
    def __init__(self):
        self.webside = Webside()
        
        self.portfolioUSD = self.webside.checkPortfolio(self.webside.xpathPortfolioUSD)
        self.portfolioBTC = self.webside.checkPortfolio(self.webside.xpathPortfolioBTC)
        self.portfolioETH = self.webside.checkPortfolio(self.webside.xpathPortfolioETH)

        self.priceBTC = self.webside.checkPrice(self.webside.xpathPriceBTC)
        self.priceETH = self.webside.checkPrice(self.webside.xpathPriceETH)

        self.portfolioValueUSD = self.portfolioBTC * self.priceBTC + self.portfolioETH * self.priceETH + self.portfolioUSD

    def trade(self, amount, currencyToSell, currencyToBuy):
        self.webside.setList(self.webside.idSellList, currencyToSell)
        self.webside.setList(self.webside.idBuyList, currencyToBuy)
        self.webside.insetStringIntoForm(self.webside.idAmount, amount)
        # self.webside.cklickButton(self.webside.xpathComfirmTransactionButton)


    def update(self):
        self.portfolioUSD = self.webside.checkPortfolio(self.webside.xpathPortfolioUSD)
        self.portfolioBTC = self.webside.checkPortfolio(self.webside.xpathPortfolioBTC)
        self.portfolioETH = self.webside.checkPortfolio(self.webside.xpathPortfolioETH)

        self.priceBTC = self.webside.checkPrice(self.webside.xpathPriceBTC)
        self.priceETH = self.webside.checkPrice(self.webside.xpathPriceETH)

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
        print("BTCUSD : " + str(self.priceBTC))
        print("ETHUSD : " + str(self.priceETH))
        print("================================")
