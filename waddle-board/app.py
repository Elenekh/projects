from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('first-page.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if not username or not password or not email:
            return "All fields are required. Please try again."
        
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        for user in data:
            if user['emails'] == email:
                return "Email already registered. Please log in."

        new_user = {"usernames": username, "passwords": password, "emails": email}
        data.append(new_user)

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        return redirect(url_for('login'))

    return render_template('register.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        attempted_email = request.form['email']
        attempted_password = request.form['password']

        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return "No users registered. Please sign up first."
        
        for user in data:
            if user["emails"] == attempted_email and user['passwords'] == attempted_password:
                return redirect(url_for('main_page'))
            
        return "Invalid credentials. Please try again."
    return render_template('login.html')

# Route for the main page after login
@app.route('/mainpage')
def main_page():
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run(debug=True)
