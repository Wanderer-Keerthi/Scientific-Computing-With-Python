class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
            total += item['amount']
        output = title + items + f"Total: {total:.2f}"
        return output

def create_spend_chart(categories):
    spent = []
    names = []
    total_spent = 0
    for category in categories:
        spent.append(sum(item['amount'] for item in category.ledger if item['amount'] < 0))
        total_spent += spent[-1]
        names.append(category.name)
    
    percentages = [int((s / total_spent) * 10) * 10 for s in spent]
    
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    max_name_length = max(len(name) for name in names)
    for i in range(max_name_length):
        chart += "     "
        for name in names:
            chart += name[i] + "  " if i < len(name) else "   "
        chart += "\n"
    
    return chart[:-1]
