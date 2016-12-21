from app import app
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import string

count_variables = 0
ALLOWED_EXTENSIONS = ['csv', 'txt']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def fixit(file):
    old = file.read()
    new = ""
    global count_variables
    for i in old:
        if str(i) in string.printable or i == "'":
            new += str(i)
    else:
        count_variables += 1
    create = open(str(count_variables) + 'fixes.csv','w')
    create.write(new)
    create.close()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            filename = fixit(file)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('index.html')
