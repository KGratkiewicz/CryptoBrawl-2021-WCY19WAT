from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from enum import Enum
from Login import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Currency(Enum):
    BTC = 1
    ETH = 2
    USD = 3

class Webside:
    def __init__(self, address = "https://platform.cryptobrawl.pl/ui/protected/trade", address2 = "https://www.coingecko.com/pl/waluty/ethereum", address3 = "https://www.coingecko.com/pl/waluty/bitcoin"):
        
        self.log = Login()

        self.xpathPriceBTC = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[2]/div[2]/div[2]/span"
        self.xpathPriceETH = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[2]/div[3]/div[2]/span"
        self.xpathPortfolioUSD = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[1]/h1[1]"
        self.xpathPortfolioBTC = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[1]/h1[2]"
        self.xpathPortfolioETH = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[1]/h1[3]"
        self.xpathComfirmTransactionButton = "/html/body/div[1]/div/main/div/div[2]/div[2]/div/div[8]/button"
        self.xpathTrade = "/html/body/div[1]/header/nav[1]/ul/a[2]"

        self.xpathLoginForm = "/html/body/div/article[1]/div[2]/div[3]/div/form/div[1]/div[1]/input"
        self.xpathPassworForm = "/html/body/div/article[1]/div[2]/div[3]/div/form/div[2]/div[1]/input"
        self.xpathLoginButton = "/html/body/div/article[1]/div[2]/div[3]/div/form/div[3]/button"

        self.xpathCoin = "/html/body/div[4]/div[4]/div[1]/div/div[1]/div[4]/div/div[1]/span[1]/span"
        
        self.idSellList = "downshift-0-toggle-button"
        self.idBuyList = "downshift-1-toggle-button"
        self.idAmount = "sold-amount"



        


        self.coinGekoETH = webdriver.Chrome(ChromeDriverManager().install())
        self.coinGekoETH.get(address2)

        self.coinGekoBTC = webdriver.Chrome(ChromeDriverManager().install())
        self.coinGekoBTC.get(address3)

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(address)
        
        time.sleep(3)

        self.login()

    def __del__(self):
        self.driver.close()
        self.driver.quit()

    def login(self):
        loginForm = self.driver.find_element_by_xpath(self.xpathLoginForm)
        loginForm.send_keys(self.log.login)

        passwordForm = self.driver.find_element_by_xpath(self.xpathPassworForm)
        passwordForm.send_keys(self.log.password)

        time.sleep(1)

        self.clickButton(self.xpathLoginButton)

    def getCoinGekoETH(self, xpathCoin):
        priceElement = self.coinGekoETH.find_element_by_xpath(xpathCoin)
        priceString = priceElement.get_attribute('innerHTML')
        price = priceString.replace("BTC","")
        price = price.replace("USD","")
        price = price.replace("&nbsp;","")
        price = price.replace(",",".")
        price = float(price)
        return price

    def getCoinGekoBTC(self, xpathCoin):
        priceElement = self.coinGekoBTC.find_element_by_xpath(xpathCoin)
        priceString = priceElement.get_attribute('innerHTML')
        price = priceString.replace("BTC","")
        price = price.replace("USD","")
        price = price.replace("&nbsp;","")
        price = price.replace(",",".")
        price = price.replace("$","")
        price = price.replace(" ",".")
        price = float(price)
        return price

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
        time.sleep(2)

    def clickButton(self, xpathButton):
        time.sleep(1)
        button = self.driver.find_element_by_xpath(xpathButton)   
        button.click()
        time.sleep(1)

        try:
            button.click()
            time.sleep(7)
        except:
            time.sleep(7)

    def refresh(self):
        self.driver.get("https://platform.cryptobrawl.pl/ui/protected/trade")
        time.sleep(3)
        current_url = self.driver.current_url
        while current_url != "https://platform.cryptobrawl.pl/ui/protected/trade":
            if current_url == "https://platform.cryptobrawl.pl/ui/home":
                self.driver.get("https://platform.cryptobrawl.pl/ui/protected/trade")
                time.sleep(3)
                current_url = self.driver.current_url
            else:
                time.sleep(3)
                self.login()
                time.sleep(8)
                self.driver.get("https://platform.cryptobrawl.pl/ui/protected/trade")
                time.sleep(3)
                current_url = self.driver.current_url
        self.coinGekoBTC.refresh()
        self.coinGekoETH.refresh()
        time.sleep(2)
        
        

        