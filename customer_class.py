class customer:
	def __init__(self, name, phone, purchase, date):
		self.name = name
		self.phone = phone
		self.purchase = purchase
		self.date = date

	def __repr__(self):
		return 'Name: ' + self.name + '\nPhone: ' + self.phone + '\nItem Purchased: ' + self.purchase + '\nDate of Del/Purchase: ' + self.date

	def update(self):
		pass