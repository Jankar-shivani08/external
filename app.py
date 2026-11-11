from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <center>
        <h1>Registration Form</h1>
        <a href="/register">Go to Registration Page</a>
    </center>
    """

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        year = request.form['year']
        return render_template('success.html', name=name)
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)