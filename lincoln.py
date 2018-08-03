import random

def do():
	population = {}

	number = 5000
	number += 1

	for _ in range(0,number):
		population[_] = 0

	marked = []

	percentage = random.randint(17,23)
	collect = int((number / 100) * percentage)

	for _ in range(0, collect):
		f = random.randint(0, number)
		marked.append(f)
		population[f] = 1

	match = []

	percentage_2 = random.randint(17,23)
	collect_2 = int((number / 100) * percentage_2)

	for _ in range(0, collect_2):
		f = random.randint(0, number)
		#marked_2.append(f)
		if population[f] == 1:
			match.append(f)

		
	print("marked: ", len(marked))
	print("collected: ", collect_2)
	print("match: ", len(match))
	print("population: ", (number - 1))
	print("lincoln index estimation: " + str((collect * collect_2)/(len(match))))
	print ""

i = 0
while i < 10:
	try:
		do()
		i += 1

	except KeyError:
		i = i
