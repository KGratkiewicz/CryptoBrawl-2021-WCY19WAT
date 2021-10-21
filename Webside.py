from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from enum import Enum

class Currency(Enum):
    BTC = 1
    ETH = 2
    USD = 3

class Webside:
    def __init__(self, address = "https://platform.cryptobrawl.pl/ui/protected/trade"):
        
        self.xpathPriceBTC = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[2]/div[2]/div[2]/span"
        self.xpathPriceETH = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[2]/div[3]/div[2]/span"
        self.xpathPortfolioUSD = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[1]/h1[1]"
        self.xpathPortfolioBTC = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[1]/h1[2]"
        self.xpathPortfolioETH = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[1]/h1[3]"
        self.xpathComfirmTransactionButton = "/html/body/div[1]/div/main/div/div[2]/div[2]/div/div[8]/button[2]"
        
        self.idSellList = "downshift-0-toggle-button"
        self.idBuyList = "downshift-1-toggle-button"
        self.idAmount = "sold-amount"

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(address)
        self.accept = input("Login into side by browser opened by me. Next go to the trade side and press ENTER button...")

    def __del__(self):
        self.driver.close()
        self.driver.quit()

    def stringPriceToFloat(self, stringPrice):
        price = str(stringPrice)
        price = price.replace("$","")
        price = price.replace(",","")
        return float(price)

    def checkPrice(self, xpathPrice):
        priceElement = self.driver.find_element_by_xpath(xpathPrice)
        priceString = priceElement.get_attribute('innerHTML')
        price = self.stringPriceToFloat(priceString)
        return price

    def stringPortfolioToFloat(self, stringPortfolio):
        portfolio = stringPortfolio[17:]
        portfolio = portfolio.replace(",","")
        return float(portfolio)

    def checkPortfolio(self, xpathPortfolio):
        portfolioElement = self.driver.find_element_by_xpath(xpathPortfolio)
        portfolioString = portfolioElement.get_attribute('innerHTML')
        portfolio = self.stringPortfolioToFloat(portfolioString)
        return portfolio

    def setList(self, idList, option):
        list = self.driver.find_element_by_id(idList)
        list.click()
        time.sleep(1)
        if option == Currency.BTC:
            list.send_keys(Keys.DOWN, Keys.ENTER)
        elif option == Currency.ETH: 
            list.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        elif option == Currency.USD:
            list.send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)

    def insetStringIntoForm(self, idForm, string):
        form = self.driver.find_element_by_id(idForm)
        form.click()
        time.sleep(1)
        form.send_keys(str(string))

    def clickButton(self, xpathButton):
        time.sleep(1)
        button = self.driver.find_element_by_xpath(xpathButton)   
        button.click()