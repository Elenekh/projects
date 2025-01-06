from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

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

        new_user =  {"usernames": username, "passwords": password, "emails": email}
        data.append(new_user)


        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)