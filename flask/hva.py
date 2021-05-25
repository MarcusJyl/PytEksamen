#!flask/bin/python
import os
import birdScraper
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'PytEksamen/flask/static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
DISPLAY_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = DISPLAY_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect("output" + url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


#@app.route('/index')
#def home():
#    return render_template('index.html') # Render home.html

#/@app.route('/uploader', methods = ['GET', 'POST'])
#def upload_file():
  # if request.method == 'POST':
  #    f = request.files['file']
 #     f.save(f.filename)
#      return redirect()

@app.route('/output/',methods=['GET'])
def classify_type():
    
    filename = os.path.join(DISPLAY_FOLDER, request.args.get('filename'))
        # Get the output from the classification model
    variety = birdScraper.modelFinal(os.path.join(UPLOAD_FOLDER, request.args.get('filename')))
    picture = birdScraper.getPicture(birdScraper.processBirdName(os.path.join(UPLOAD_FOLDER, request.args.get('filename'))))
        # Render the output in new HTML page

    return render_template('output.html', variety=variety,picture=picture,filename= request.args.get('filename'))


@app.route('/display/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename)
	return redirect(url_for('static', filename= "uploads/" +filename), code=301)

if(__name__=='__main__'):
    app.run(debug=True) 