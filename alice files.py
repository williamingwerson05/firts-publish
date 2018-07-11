name=input("What is your name?")
age=input("What is your age?")
# name = 'Alice'
if name.lower() == 'alice':  
	print('Hi Alice')
elif int(age) <= 12:
	print('You are not alice')
elif int(age) > 100:
	print('You are not Alice, grannie.')
elif int(age) > 2000:
	print('Unlike you, Alice is not an undead, immortal vampire.')
