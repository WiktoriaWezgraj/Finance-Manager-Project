'''Lista wydatków, aktualny stan konta z uwzg. wpływow, wypłat'''

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

class Finance():
    def __init__(self):
        self.filepath = "tracker.json"

    def deposit(self, amount):
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
            data["balance"] += amount
            print(data)
            json.dump(data, open(self.filepath, 'w'))
            return data
        # make deposit with balance, later create app with nice format and graphs with matplotlib 
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
        
    def payment(self, category, f_amount):

        with open(self.filepath, "r") as f:
            data = json.load(f)

        if category in data:
            data[category] += f_amount
            data["balance"] -= f_amount
            json.dump(data, open(self.filepath, 'w'))
            return data
        else:
            return "Invalid category."              
                
f = Finance()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_tracker():
    data = f.create()
    return jsonify(data)

@app.route('/deposit', methods=['POST'])
def deposit():
    amount = float(request.form['amount'])
    data = f.deposit(amount)
    return jsonify(data)

@app.route('/payment', methods=['POST'])
def make_payment():
    category = request.form['category']
    f_amount = float(request.form['amount'])
    data = f.payment(category, f_amount)
    return jsonify(data)

