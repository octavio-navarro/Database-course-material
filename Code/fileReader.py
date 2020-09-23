import csv

with open("TextFiles/populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
         print(row)

    #reader = csv.DictReader(csvFile)
    
    #print(reader.fieldnames)


    