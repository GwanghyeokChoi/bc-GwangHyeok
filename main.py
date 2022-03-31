from module import latest
from module import history
from module import convert

def Main(chose):
    chose_latest = ['1', 'latest_data', 'latest data', 'latest']
    chose_history = ['2', 'history_data', 'history data', 'history']
    chose_convert = ['3', 'convert_price', 'convert price', 'convert']

    if chose in chose_latest:
        print("latest: " + chose)
        base = input("base currency: ")
        target = input("target currency: ")

        # laatest()

    elif chose in chose_history:
        print("history: " + chose)

        base = input("base currency: ")
        target = input("target currency: ")
        starting = input("starting at: ")
        ending = input("ending at: ")

    elif chose in chose_price:
        print("from: " + chose)
        print("to: " + chose)
        print("date: " + chose)

        base = input("")
        target = input("")
        date = input("")
        
    else:
        print("Please check the value you selected again.")
        return 

    return
if __name__ == "__main__":
    print("Coin Exchange Rate Service")
    chose = input("What do you want to search for? \n1. Search latest data \n2. Search history data \n3. Convert price\n").lower()

    Main(chose)