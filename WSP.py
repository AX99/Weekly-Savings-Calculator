from datetime import datetime
#Will contain week number:weekly saving amount
weeks = {}

now = datetime.now()
week_numb = datetime.date(now).isocalendar()[1]

#Pushes January weeks to weeks dictionary
def January():
	saving = 0
	for i in range(1, 5):
		saving = 5
		weeks[i] = saving
		
#Pushes rest of year weeks to weeks dictionary
def rest_of_year():
	for i in range(5, 53):
		weeks[i] = i
		
#Get the current pot total
def current_pot():
	acc_total = 0
	for i in range(1, len(weeks)+1):
		if i <= week_numb:
			acc_total += weeks[i]
	return acc_total

#Called to fill the weeks dictionary
January()
rest_of_year()


#Console Prints
print("###############################################")
print("             Weekly Savings Checker")
print("###############################################")
print()
print("################ ",now.day,"/",now.month,"/",now.year, "###############")
print()
print('This week you should add £',weeks[week_numb], 'to the pot')
print()
print("The total amount in the pot is £",current_pot())
