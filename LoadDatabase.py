import csv
import os
path =  "/Users/garvitkataria/Desktop/DjangoEnv/WineExpert/" # Set path of new directory here
os.chdir(path) # changes the directory
from Wines.models import Wine # imports the model
with open('winemag-data_first150k3ed116a.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	print(reader)
	i=0
	for row in reader:
		print(row['points'],row['price'])
		if(row['points']==''):
			p = Wine(country=row['country'], description=row['description'], designation=row['designation'], price=row['price'], province=row['province'], region_1=row['region_1'], region_2=row['region_2'], variety=row['variety'], winery=row['winery'])
		elif(row['price']==''):
			p = Wine(country=row['country'], description=row['description'], designation=row['designation'], points=row['points'], province=row['province'], region_1=row['region_1'], region_2=row['region_2'], variety=row['variety'], winery=row['winery'])
		else:
			p = Wine(country=row['country'], description=row['description'], designation=row['designation'], points=row['points'], price=row['price'], province=row['province'], region_1=row['region_1'], region_2=row['region_2'], variety=row['variety'], winery=row['winery'])
		p.save()
		i+=1
		if(i==200):
			break

exit()