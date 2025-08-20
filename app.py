from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sensitive Information (FAKE DATA for Assignment)
USERNAME = "admin"
PASSWORD = "password123"
API_KEY = "ABCD1234XYZ"
IP_ADDRESS = "192.168.1.100"

# Home Page
@app.route('/')
def home():
    return "<h1>Welcome to My Flask App</h1><p>Go to /login to login.</p>"

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        if user == USERNAME and pwd == PASSWORD:
            return f"<h2>Login Successful!</h2><p>Your API Key: {API_KEY}</p>"
        else:
            return "<h2>Invalid Credentials</h2>"
    
    # HTML Form
    return '''
        <h1>Login Page</h1>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <button type="submit">Login</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
