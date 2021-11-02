from AutoTrading import AutoTrading
from Bot import BotCube
from Webside import Webside

def main():
    bot = BotCube(0.1, 500000, 3.33, 50)
    bot.work()

if __name__ == "__main__":
    main()