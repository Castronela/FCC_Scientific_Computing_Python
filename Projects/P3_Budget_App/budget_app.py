#!/bin/python3.11

class Category:
	def __init__(self, category):
		self.category = category
		self.ledger = []
	def __str__(self):
		self.output = f"{self.category:*^30}" + '\n'
		self.output += '\n'.join(f"{log['description']: <23}"[:23] + f"{log['amount']:>7.2f}" for log in self.ledger)
		self.output += '\nTotal: ' + f"{self.get_balance():.2f}"
		return self.output
	def deposit(self, amount, description=''):
		self.ledger.append({'amount':amount, 'description': description})
	def withdraw(self, amount, description=''):
		if not self.check_funds(amount):
			return False
		self.ledger.append({'amount':-amount, 'description': description})
		return True	  
	def get_balance(self):
		return (sum(log['amount'] for log in self.ledger))
	def transfer(self, amount, category):
		if self.withdraw(amount, f"Transfer to {category.category}"):
			category.deposit(amount, f"Transfer from {self.category}")
			return True
		return False
	def check_funds(self, amount):
		return amount <= self.get_balance()

def create_spend_chart(categories):
	# Calculate amount spent by category and total spent
	total_spent = 0
	by_category = {}
	for category in categories:
		spent = -sum(log['amount'] if log['amount'] < 0 else 0 for log in category.ledger)
		by_category[category.category] = spent
		total_spent += spent

	# Calculate percentage spent by category
	by_category = {cat: spent * 100 / total_spent if total_spent > 0 else 0 for cat, spent in by_category.items()}
	
	# Build output string
	output = 'Percentage spent by category\n'
	for percent in range(100, -1, -10):
		output += f"{percent:>3}| "
		for category in categories:
			if by_category[category.category] >= percent:
				output += 'o  '
			else:
				output += '   '
		output += '\n'
		
	output += ' ' * 4 + '-' * (len(categories) * 3 + 1)
	max_len = max(len(category.category) for category in categories)
	for index in range(max_len):
		output += '\n' + ' ' * 5
		for category in categories:
			if index < len(category.category):
				output += category.category[index] + ' ' * 2
			else:
				output += ' ' * 3
	return output

if __name__ == '__main__':
	# apple = Category('apple')
	# apple.deposit(300, 'carrot')
	# apple.deposit(600, 'banana on the floor yoho and a bottle')
	# apple.withdraw(4.5677, 'one')
	# banana = Category('banana')
	# print(apple.get_balance())
	# apple.transfer(200, banana)
	# print(apple)
	# print('\n')
	# print(banana)

	food = Category('Food')
	food.deposit(1000, 'deposit')
	food.withdraw(10.15, 'groceries')
	food.withdraw(15.89, 'restaurant and more food for dessert')
	clothing = Category('Clothing')
	food.transfer(50, clothing)
	# print(food, '\n')
	# print(clothing, '\n')
	print(create_spend_chart([food, clothing]))