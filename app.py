from flask import Flask, render_template , request
from auth import sign_in_flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      result = sign_in_flask(email, password)
      return result
    else:
        return render_template('login.html')

app.run(debug=True)