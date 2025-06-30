import csv
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

# Your existing backend code (shortened here for space)
class bankinfo:
    def __init__(self, firstname, lastname, gender, address):
        self.fn = firstname
        self.ln = lastname
        self.gender = gender
        self.add = address

class bankaccount(bankinfo):
    def __init__(self, fn, ln, gender, address, accountno, amount):
        super().__init__(fn, ln, gender, address)
        self.accno = accountno
        self.amount = amount

class saving(bankaccount):
    minamount = 10000
    rate = 0.06
    def isvalid(self):
        return self.amount >= saving.minamount
    def interest(self, months):
        return self.amount * saving.rate * (months / 12)

class current(bankaccount):
    minamount = 5000
    def isvalid(self):
        return self.amount >= current.minamount
    def interest(self, months):
        return 0

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    fn = request.form["fn"]
    ln = request.form["ln"]
    gender = request.form["gender"]
    address = request.form["address"]
    accno = request.form["accno"]
    acctype = request.form["acctype"].lower()
    amount = float(request.form["amount"])
    months = int(request.form["months"])

    if acctype == "saving":
        acc = saving(fn, ln, gender, address, accno, amount)
    elif acctype == "current":
        acc = current(fn, ln, gender, address, accno, amount)
    else:
        return "Invalid account type"

    if not acc.isvalid():
        return "Invalid amount for account type"

    interest = acc.interest(months)

    # Save to CSV
    with open("accounts_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        
        if file.tell() == 0:  # write header only if file is empty
            writer.writerow([
                "Timestamp", "First Name", "Last Name", "Gender", "Address",
                "Account Number", "Account Type", "Amount", "Months", "Interest"
            ])
        
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            fn, ln, gender, address,
            accno, acctype, amount,
            months, round(interest, 2)
        ])

    return render_template('result.html', acc=acc, interest=interest, months=months)

if __name__ == '__main__':
    app.run(debug=True)
