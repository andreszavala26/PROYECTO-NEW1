from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key=  'lucero'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/segura")
def segura():
    if session:
        return render_template('segura.html')
    else:
       return redirect(url_for('login')) 
     
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='post':
        return redirect(url_for('login.html'))
    return render_template('login.html')
    

@app.route("/error")
def error():
    return render_template('error.html')

if __name__  ==  "__main__":
    app.run(debug=True)