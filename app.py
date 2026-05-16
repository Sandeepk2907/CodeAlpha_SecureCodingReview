from flask import Flask, request, render_template_string
from database import connect_db

app = Flask(__name__)

# Simple Login Page
LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>

<h2>Login System</h2>

<form method="POST">
    <input type="text" name="username" placeholder="Username"><br><br>

    <input type="password" name="password" placeholder="Password"><br><br>

    <button type="submit">Login</button>
</form>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = connect_db()
        cursor = conn.cursor()

        # INTENTIONALLY VULNERABLE SQL QUERY
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        print("\nExecuted Query:")
        print(query)
        cursor.execute(query)

        # query = "SELECT * FROM users WHERE username=? AND password=?"
        # cursor.execute(query, (username, password))

        user = cursor.fetchone()

        conn.close()

        if user:
            return f"Welcome {username}"
        else:
            return "Invalid Credentials"

    return render_template_string(LOGIN_PAGE)

if __name__ == '__main__':
    app.run(debug=True)