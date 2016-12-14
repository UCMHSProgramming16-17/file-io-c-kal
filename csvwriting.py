# csvwriting.py 

# import module
import requests 
import csv
# create file
csvfile= open('csvwriting2.txt', 'w')
# creat csvwriter

csvwriter= csv.writer(csvfile, delimiter= ',')

csvwriter.writerow(['a', 'b', 'c'])

csvfile.close()
# write information

# close file 