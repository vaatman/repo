# import csv
import csv

# open file for reading
f = open("list", "r")

# ask for department
dept = input("What Department [ID=1,Firstname=2,Dept=3]? ")
dpt = int(dept) -  1

# read file as csv
rdr = csv.reader(f)

# printout each line
for line in rdr:
	if dpt == 1:
		print(line[1])
f.close()
