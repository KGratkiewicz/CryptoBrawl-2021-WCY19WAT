from TradingTools import Account
import statistics 
from Webside import Currency
import time

class BotCube:
    def __init__(self, procent, amoutUSD, amoutBTC, amoutETH):
        self.account = Account()

        self.procent = procent
        self.amoutUSD = amoutUSD
        self.amoutBTC = amoutBTC
        self.amoutETH = amoutETH

        self.buyingBTC = True
        self.buyingETH = True

        self.lastHopBTC = 0
        self.lastDigBTC = 100000000

        self.lastHopETH = 0
        self.lastDigETH = 100000000

        self.last24hpriceBTC = []
        self.last24hHighBTC = []
        self.oldHighBTC = []
        self.last24hLowBTC = []
        self.oldLowBTC = []
        self.avgPriceBTC = 0
        self.avgHighBTC = 0
        self.avgLowBTC = 0

        self.last24hpriceETH = []
        self.last24hHighETH = []
        self.oldHighETH = []
        self.last24hLowETH = []
        self.oldLowETH = []
        self.avgPriceETH = 0
        self.avgHighETH = 0
        self.avgLowETH = 0

    def addNewPrice(self, newPriceBTC,newPriceETH):

        if self.lastDigBTC > newPriceBTC:
            self.lastDigBTC = newPriceBTC
        if self.lastHopBTC < newPriceBTC:
            self.lastHopBTC = newPriceBTC

        if self.lastDigETH > newPriceETH:
            self.lastDigETH = newPriceETH
        if self.lastHopETH < newPriceETH:
            self.lastHopETH = newPriceETH
        

        self.last24hpriceBTC.insert(0,float(newPriceBTC))
        size = len(self.last24hpriceBTC)
        if size > 1440:
            self.last24hpriceBTC.pop()
        self.avgPriceBTC = statistics.mean(self.last24hpriceBTC)

        self.last24hpriceETH.insert(0,float(newPriceETH))
        size = len(self.last24hpriceETH)
        if size > 1440:
            self.last24hpriceETH.pop()
        self.avgPriceETH = statistics.mean(self.last24hpriceETH)

    def addHiLo(self):
        if size > 2:
            if self.last24hpriceBTC[0] < self.last24hpriceBTC[1] and self.last24hpriceBTC[1] > self.last24hpriceBTC[2]:
               self.last24hHighBTC.insert(0,float(self.last24hpriceBTC[1]))
               self.oldHighBTC.insert(0,1440)

            sizeHighBTC = len(self.last24hHighBTC)
            if sizeHighBTC > 1:
               for i in range(0,sizeHighBTC):
                    self.oldHighBTC[i] -= 1
               if self.oldHighBTC[sizeHighBTC-1] <=0:
                   self.last24hHighBTC.pop()
                   self.oldHighBTC.pop
               self.avgHighBTC = statistics.mean(self.last24hHighBTC)
               


            if self.last24hpriceBTC[0] > self.last24hpriceBTC[1] and self.last24hpriceBTC[1] < self.last24hpriceBTC[2]:
               self.last24hLowBTC.insert(0,float(self.last24hpriceBTC[1]))
               self.oldLowBTC.insert(0,1440)

            sizeLowBTC = len(self.last24hLowBTC)
            if sizeLowBTC > 1:
               for i in range(0,sizeLowBTC):
                    self.oldLowBTC[i] -= 1
               if self.oldLowBTC[sizeLowBTC-1] <=0:
                   self.last24hLowBTC.pop()
                   self.oldLowBTC.pop
               self.avgLowBTC = statistics.mean(self.last24hLowBTC)

        if size > 2:
            if self.last24hpriceETH[0] < self.last24hpriceETH[1] and self.last24hpriceETH[1] > self.last24hpriceETH[2]:
               self.last24hHighETH.insert(0,float(self.last24hpriceETH[1]))
               self.oldHighETH.insert(0,1440)

            sizeHighETH = len(self.last24hHighETH)
            if sizeHighETH > 1:
               for i in range(0,sizeHighETH):
                    self.oldHighETH[i] -= 1
               if self.oldHighETH[sizeHighETH-1] <=0:
                   self.last24hHighETH.pop()
                   self.oldHighETH.pop
               self.avgHighETH = statistics.mean(self.last24hHighETH)


            if self.last24hpriceETH[0] > self.last24hpriceETH[1] and self.last24hpriceETH[1] < self.last24hpriceETH[2]:
               self.last24hLowETH.insert(0,float(self.last24hpriceETH[1]))
               self.oldLowETH.insert(0,1440)

            sizeLowETH = len(self.last24hLowETH)
            if sizeLowETH > 1:
               for i in range(0,sizeLowETH):
                    self.oldLowETH[i] -= 1
               if self.oldLowETH[sizeLowETH-1] <=0:
                   self.last24hLowETH.pop()
                   self.oldLowETH.pop
               self.avgLowETH = statistics.mean(self.last24hLowETH)
               self.lastDigETH = self.last24hLowETH[0]

               self.last24hpriceETH.insert(0,float(newPriceETH))
        size = len(self.last24hpriceETH)
        if size > 1440:
            self.last24hpriceETH.pop()
        self.avgPriceETH = statistics.mean(self.last24hpriceETH)

        if size > 2:
            if self.last24hpriceETH[0] < self.last24hpriceETH[1] and self.last24hpriceETH[1] > self.last24hpriceETH[2]:
               self.last24hHighETH.insert(0,float(self.last24hpriceETH[1]))
               self.oldHighETH.insert(0,1440)

            sizeHighETH = len(self.last24hHighETH)
            if sizeHighETH > 1:
               for i in range(0,sizeHighETH):
                    self.oldHighETH[i] -= 1
               if self.oldHighETH[sizeHighETH-1] <=0:
                   self.last24hHighETH.pop()
                   self.oldHighETH.pop
               self.avgHighETH = statistics.mean(self.last24hHighETH)
     
    def buingCryterium2BTC(self):
        if self.account.portfolioUSD > 1:
            if self.account.priceBTC < self.account.priceCoinBTC:
                return True

    def buingCryterium2ETH(self):
        if self.account.portfolioUSD > 1:
            if self.account.priceETH < (self.account.priceCoinETH - 0.1):
                return True
    
    def sellingCryterium2BTC(self):
        if self.account.portfolioBTC > 1:
            if self.account.priceBTC > self.account.priceCoinBTC:
                return True

    def sellingCryterium2ETH(self):
        if self.account.portfolioETH > 1:
            if self.account.priceETH > (self.account.priceCoinETH + 0.1):
                return True

    

        

    def buingCryteriumBTC(self):
        if self.buyingBTC == True:
            if self.lastDigBTC > 0:
                increase = (self.account.priceBTC - self.lastDigBTC)/self.avgPriceBTC
                increase *= 100
                if increase >= self.procent:
                    self.buyingBTC = False
                    self.lastHopBTC = self.account.priceBTC
                    return True
        return False

    def buingCryteriumETH(self):
        if self.buyingETH == True:
            if self.lastDigETH > 0:
                increase = (self.account.priceETH - self.lastDigETH)/self.avgPriceETH
                increase *= 100
                if increase >= self.procent:
                    self.buyingETH = False
                    self.lastHopETH = self.account.priceETH
                    return True
        return False
            
    def sellingCryteriumBTC(self):
        if self.buyingBTC == False:
            if self.lastHopBTC > 0:
                fall = (self.lastHopBTC - self.account.priceBTC)/self.avgPriceBTC
                fall *= 100
                if fall >= self.procent:
                    self.buyingBTC = True
                    self.lastDigBTC = self.account.priceBTC
                    return True
        return False

    def sellingCryteriumETH(self):
        if self.buyingETH == False:
            if self.lastHopETH > 0:
                fall = (self.lastHopETH - self.account.priceETH)/self.avgPriceETH
                fall *= 100
                if fall >= self.procent:
                    self.buyingETH = True
                    self.lastDigETH = self.account.priceETH
                    return True
        return False

    def trading(self):
        if self.buingCryterium2BTC():
            if float(self.account.portfolioUSD) >= self.amoutUSD:
                self.account.trade(self.amoutUSD, Currency.USD, Currency.BTC)
                self.amoutBTC = self.amoutUSD/self.account.priceBTC
            elif self.account.portfolioUSD > 0:
                self.account.trade(float(self.account.portfolioUSD), Currency.USD, Currency.BTC)
                self.amoutBTC = self.account.portfolioUSD/self.account.priceBTC

        if self.sellingCryterium2BTC():
            if float(self.account.portfolioBTC) >= self.amoutBTC:
                self.account.trade(self.amoutBTC, Currency.BTC, Currency.USD)

            elif self.account.portfolioBTC > 0:
                self.account.trade(float(self.account.portfolioBTC), Currency.BTC, Currency.USD)


        if self.buingCryterium2ETH():
            if float(self.account.portfolioUSD) >= self.amoutUSD:
                self.account.trade(self.amoutUSD, Currency.USD, Currency.ETH)
                self.amoutETH = self.amoutUSD/self.account.priceETH
            elif self.account.portfolioUSD > 0:
                self.account.trade(float(self.account.portfolioUSD), Currency.USD, Currency.ETH)
                self.amoutETH = self.account.portfolioUSD/self.account.priceETH

        if self.sellingCryterium2ETH():
            if float(self.account.portfolioETH) >= self.amoutETH:
                self.account.trade(self.amoutETH, Currency.ETH, Currency.USD)

            elif self.account.portfolioETH > 0:
                self.account.trade(float(self.account.portfolioETH), Currency.ETH, Currency.USD)

    def tradingETH(self):
       
        if self.buingCryterium2ETH():
            self.account.trade(float(self.account.portfolioUSD), Currency.USD, Currency.ETH)
        if self.sellingCryterium2ETH():
            self.account.trade(float(self.account.portfolioETH), Currency.ETH, Currency.USD)
            
                
                


    def displayLast24h(self):
        print("$$$$$$$$$$$$$$$$$$$")
        print("AVG:")
        print(str(self.avgPriceBTC))
        print(str(self.avgHighBTC))
        print(str(self.avgLowBTC))
        print("$$$$$$$$$$$$$$$$$$$")

    def simulate(self):
        for i in range(0, 10080):      
            self.account.update()
            self.addNewPrice(self.account.priceBTC, self.account.priceETH)
            self.trading()
        return self.account.portfolioValueUSD

    def work(self):
        while True:
            try:
                self.account.update()          
            except:
                try:
                    self.account.webside.refresh()
                    continue
                except:
                    continue

            self.addNewPrice(self.account.priceBTC, self.account.priceETH)
            self.account.displayAccount()

            try:
                self.tradingETH()
            except:
                continue

            try:
                self.account.webside.refresh()
            except:
                continue
            time.sleep(1)


