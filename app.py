from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calc.html', pageTitle="Calculator")

@app.route('/add',methods=['GET','POST'])
def addition():
    if request.method == 'POST':
        form = request.form
        numberOne = int(form['numOne'])
        numberTwo = int(form['numTwo'])
        calc = numberOne + numberTwo
        return render_template('calc.html',display=calc, pageTitle='Calculator')

@app.route('/subtract',methods=['GET','POST'])
def addition():
    if request.method == 'POST':
        form = request.form
        numberOne = int(form['numOne'])
        numberTwo = int(form['numTwo'])
        calc = numberOne - numberTwo
        return render_template('calc.html',display=calc, pageTitle='Calculator')

if __name__ == '__main__':
    app.run(debug=True)
