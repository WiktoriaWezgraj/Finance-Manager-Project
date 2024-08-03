'''Lista wydatków, aktualny stan konta z uwzg. wpływow, wypłat'''

import json

class Finance():
    def __init__(self):
        self.filepath = "tracker.json"

    def deposit(self):
        amount = int(input("Deposit value:")) 
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
            data["balance"] += amount
            print(data)
            json.dump(data, open(self.filepath, 'w'))
    #     make deposit with balance, later create app with nice format and graphs with matplotlib 
        except ValueError:
            print("Invalid input.")
        except FileNotFoundError:
            print("Tracker not found.")

    def create(self):
        # create new dictionary for new month
        my_dict = {}
        categories = ["balance", "grocerries", "transport", "fees", "entertainment", "clothes", "restaurant"]
        values = [0, 0, 0, 0, 0, 0, 0]

        # display dictionary and save to json
        for i in range(len(categories)):
            my_dict[categories[i]] = values[i]
        print(my_dict)
        json.dump(my_dict, open(self.filepath, 'w'))
        
    def payment(self):
        choose = 0

        with open(self.filepath, "r") as f:
            data = json.load(f)

        categories = list(data.keys())
        values = list(data.values())
        # payment to each category

        while choose<=0:
                choose = int(input("Press 1 to end payments & Press 0 to continue"))
                if choose != 0 and choose != 1:
                    print("Invalid input. Please press 1 to end payments or 0 to continue.")
                    choose = 0
                    
                amount = int(input("Payment value:"))
                print("Choose category:")
                for i in range(1, len(categories)):
                    print(i ,".", categories[i])
                category= int(input("Choose number of category:"))
                values[category] += amount
                values[0] -= amount

            
                # display dictionary
                for i in range(len(categories)):
                    data[categories[i]] = values[i]
                print(data)
                json.dump(data, open(self.filepath, 'w'))
        
f = Finance()
f.payment()
