cities = ['Pune','Junnar','Mumbai']

with open("cities.txt","w") as text_file:
	for city in cities:
		print city
		text_file.write(city)
