import datetime

class MessageUser():
	user_details = []
	messages = []
	base_message = """Salut, {name}!
	Merci {date}! Le sum ${total}. Bon sour! Votre amis"""
	
	def add_user(self, name, amount, email = None):
		
		name = name[0].upper() + name[1:].lower()
		amount = "%.2f" %(amount)
		detail = {
			"name": name, 
			"amount": amount,
		}
		
		today = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		detail['date'] = date_text
		
		if email is not None:
			detail["email"] = email
		
		self.user_details.append(detail)
	
	def get_details(self):
		return self.user_details
		
	def make_message(self):
		if len(self.user_details) > 0:
			for detail in self.get_details():
				name = detail["name"]
				amount = detail["amount"]
				date = detail["date"]
				message = self.base_message
				new_msg = message.format(
					name = name,
					date = text,
					total = amount
				)
				self.messages.append(new_msg)
			return self.messages
		return []
		
obj = MessageUser()
obj.add_user("Nina", 1450, email = 'info@hse.ru')		
obj.add_user("Ivan", 1500)
obj.add_user("Sasha", 1300)
obj.add_user("Olga", 1100)
obj.add_user("Sveta", 1200)
obj.add_user("Kolya", 2100)
obj.add_user("Semen", 1600)
obj.add_user("Alex", 900)
obj.get_details()
obj.make_message()



	
def_names = ["Ivan", "Sasha", "Olga", "Sveta", "Kolya", "Semen", "Alex"]
def_amounts = [1500, 1300, 1100, 1400, 2100, 1600, 900]

	unf_message = """Salut, {name}!
	Merci {date}! Le sum ${total}. Bon sour! Votre amis"""


def make_message(names, amounts):
	messages = []
	if len(names) == len(amounts):
		i = 0
		today = datetime.date.today()
		text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		for name in names:
			
			name = name[0].upper() + name[1:].lower()
		
			new_amount = "%.2f" %(amounts[i])
			new_msg = unf_message.format(
				name = name,
				date = text,
				total = amounts[i]
				)
			i += 1
			print(new_msg)
			
make_message(def_names, def_amounts)