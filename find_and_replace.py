import string
from flask import Flask

app = Flask(__name__)
"""app.config.from_object(__name__)
app.config.from_envvar('Shopifyfix', silent=True)"""

@app.route('/')
def fixit():
	old_file = input('File path: ')
	with open(old_file, 'r') as myfile:
	    str = myfile.read()

	new = ""
	for i in str:
		if i in string.printable or i == "'":
			new += i

	print('Creating new file, give some time.')
	create = open(old_file + ' (fixed)','w')
	create.write(new)
	create.close()

if __name__ == '__main__':
	app.run()
