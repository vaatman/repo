# import csv module
import csv

# open files as variables
r = open("list","r")

# get CSV data
r_read = csv.reader(r)

for row in r_read:
	if row[2] == "IT":
		w = open("deptOut","a")
		wrt = csv.writer(w)
		wrt.writerow(row)
		w.close()
	if row[2] == "Finance":
		w = open("financeOut","a")
		wrt = csv.writer(w)
		wrt.writerow(row)
		w.close()
	if row[2] == "Sales":
		w = open("salesOut","a")
		wrt = csv.writer(w)
		wrt.writerow(row)
		w.close()
	if row[2] == "Corporate":
		w = open("corporateOut","a")
		wrt = csv.writer(w)
		wrt.writerow(row)
		w.close()

r.close()
