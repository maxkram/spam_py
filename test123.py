from rassylka.py import MessageUser

obj = MessageUser()
obj.add_user("Nina", 1450, email = 'info@hse.ru')		
obj.add_user("Ivan", 1500)
obj.add_user("Sasha", 1300)
obj.add_user("Olga", 1100)
obj.add_user("Sveta", 1200)
obj.add_user("Kolya", 2100)
obj.add_user("Semen", 1600)
obj.add_user("Alex", 900)

print(obj.make_messages())