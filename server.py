from contextlib import redirect_stderr
from urllib import request
from flask import Flask, render_template, request, redirect 

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got post info")
    print(request.form)
    print(request.form['name'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)