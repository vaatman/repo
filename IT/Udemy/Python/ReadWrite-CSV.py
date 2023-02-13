# read data from CSV file then print out to another CSV file

# import the csv module
import csv

# open the files to use
f = open("list", "r")	# input
w = open("myList", "w")	# output

# read the csv data from the file
rdr = csv.reader(f,delimiter=",")
wrt = csv.writer(w,delimiter=",")

# print the data
#for row in rdr:	# not needed for copy'ing
	#print(row)
for row in rdr:
	wrt.writerow(row)

# close the opened files
f.close()
w.close()
