from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple user credentials
USERNAME = "user"
PASSWORD = "pass"

HTML = """
<!doctype html>
<title>Login</title>
<h2>Login Page</h2>
<form method="post">
  <label>Username:</label>
  <input type="text" name="username" required><br>
  <label>Password:</label>
  <input type="password" name="password" required><br>
  <input type="submit" value="Login">
</form>
{% if error %}
  <p style="color:red;">{{ error }}</p>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return f"<h3>Welcome, {username}!</h3>"
        else:
            error = "Invalid username or password."
    return render_template_string(HTML, error=error)

if __name__ == '__main__':
    app.run(debug=True)