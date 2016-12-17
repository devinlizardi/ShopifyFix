import string
old_file = input('File path: ')
with open(old_file, 'r') as myfile:
    str = myfile.read()

new = ""
for i in str:
	if i in string.printable or i == "'":
		new += i

print('Creating new file, give some time.')
create = open('newfile.csv','w')
create.write(new)
create.close()
