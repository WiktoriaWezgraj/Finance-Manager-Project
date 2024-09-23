'''Lista wydatków, aktualny stan konta z uwzg. wpływow, wypłat'''

import json

class Finance():
    def __init__(self):
        self.filepath = "tracker.json"

    def deposit(self):
        amount = input("How much you want to deposit?")
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
            data["balance"] += amount
            print(data)
            with open(self.filepath, 'w') as f:
                json.dump(data, f)
            
        except ValueError:
            print("Invalid input")
        except FileNotFoundError:
            print("Tracker not found")

    def create(self):
        my_dict = {}
        categories = ["balance", "groceries", "transport", "fees", "entertainment", "clothes", "restaurant"]
        values = [0, 0, 0, 0, 0, 0, 0]

        for i in range(len(categories)):
            my_dict[categories[i]] = values[i]

        print(my_dict)
        with open(self.filepath, 'w') as f:
            json.dump(my_dict, f)
        
    def payment(self):
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)

            print("Categories:")
            for option in data.keys():
                print(option)
            category = input("What is your choice?")
            
            f_amount = input("How much did you pay?")
            f_amount= f_amount.replace(",", ".")
            f_amount = float(f_amount)

            if category in data.keys():
                data[category] += f_amount
                data["balance"] -= f_amount
            
                with open(self.filepath, 'w') as f:
                    json.dump(data, f)
            else:
                print("Invalid category")
            print(data)
            
        except FileNotFoundError:
            print("Tracker not found")
        except ValueError:
            print("Invalid amount")

f = Finance()
f.payment()


