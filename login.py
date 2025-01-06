from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        attempted_email = request.form['email']
        attempted_password = request.form['password']

        try:
            with open('data.json', 'r')as file:
               data = json.load(file)
        except FileNotFoundError:
            return "No users registered. Please sign up first."
        
        for user in data:
            if user["emails"] == attempted_email and user['passwords'] == attempted_password:
                return redirect(url_for('mainpage'))
            
        return "Invalid credentials. Please try again."
    return render_template('login.html')

@app.route('/mainpage')
def main_page():
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run(debug=True)