from flask import Flask, request, render_template

import re

app = Flask(__name__, template_folder='templates')

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    string = request.form.get('string')
    regex = request.form.get('regex')
    match = re.findall (regex, string) 
    match1=len(match)
    return render_template('result.html', match =match, match1=match1)


if __name__=="__main__":
    app.run(debug=True)