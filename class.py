'''Lista wydatków, aktualny stan konta z uwzg. wpływow, wypłat'''

import json

class Finance():
    def __init__(self):
        self.filepath = "tracker.json"

    # def deposit(self):
    #     try:
    #         ...
    #     make deposit with balance, later create app with nice format and graphs with matplotlib 
    #     except ValueError:
    #         print("Invalid input.")
    #     except FileNotFoundError:
    #         print("Tracker not found.")

    def create(self):
        # create new dictionary for new month
        my_dict = {}
        categories = ["balance", "grocerries", "transport", "tuition", "fees", "entertainment", "restaurant"]
        values = [0, 0, 0, 0, 0, 0, 0]

        # display dictionary and save to json
        for i in range(len(categories)):
            my_dict[categories[i]] = values[i]
        print(my_dict)
        json.dump(my_dict, open(self.filepath, 'w'))
        
    def payment(self):
        amount = int(input("Payment value:"))

        with open(self.filepath, "r") as f:
            data = json.load(f)
            print(data)

        categories = list(data.keys())
        values = list(data.values())
        # payment to each category
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