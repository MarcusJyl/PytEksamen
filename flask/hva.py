#!flask/bin/python
import birdScraber
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') # Render home.html

@app.route('/classify',methods=['GET'])
def classify_type():
    
    bird_url = request.args.get('bird')
    print(bird_url)
        # Get the output from the classification model
    variety = birdScraber.modelFinal(bird_url)

        # Render the output in new HTML page
    return render_template('output.html', variety=variety)
    

if(__name__=='__main__'):
    app.run(debug=True) 