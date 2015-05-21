'''
/***
Date: 20_05_2015
Splits a CSV file into multiple pieces.
***/
'''
import csv
import sys
import re
import os

arg_name = sys.argv[1]
arg_row_limit = sys.argv[2]
name = re.split('\.', arg_name)[0]

def split_big_file(filename = arg_name, row_limit = arg_row_limit):
	
	outfileNumber = 1
	outfile = None
	
	# open file to read
	f = open(filename, 'rb')
	readSource = csv.reader(f)
	# get the header
	header = readSource.next()
	# separate source to 2 parts
	for index, row in enumerate(readSource):
		if index % int(row_limit) == 0:
			if outfile is not None:
				outfile.close()
			# check if import folder is exist, if not create it
			if not os.path.exists("import"):
				os.makedirs("import")
			# create sub-file name
			outfilename = '%s-{}.csv'.format(outfileNumber) % name
			# open file to write
			outfile = open(os.path.join('import',outfilename), "wb")
			#outfile = open(outfilename, 'wb')
			outfileNumber += 1
			# write data
			writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			# write header for each sub-file
			writer.writerow(header)
		writer.writerow(row)

if __name__ == "__main__":
    split_big_file()
