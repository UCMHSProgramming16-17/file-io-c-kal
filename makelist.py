# open the file in which the information will be in
file = open('mylist.txt', 'w')

# make a numbered list with the user input
for n in range (10):
    file.write(str(n+1) + '. ' + input('New term?') + '\n')
    
#close the file 
file.close()
