from flask import Flask, request, redirect, render_template, session
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'HiHelloYou'  # Replace with a strong secret key

# Replace with your hashed password (see Step 4 below)
PASSWORD_HASH = 'scrypt:32768:8:1$TV08KdRAe1uXxyne$6c7af32ee0262c4ae4580e05d9b7ecdb889231f9b8e89be527e0449c41fd214c3ca1f5e973a7344cb2f6a5a9eda44c3a4155627948ce876ea6dc619c7a746111'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if check_password_hash(PASSWORD_HASH, password):
            session['authenticated'] = True
            return redirect('/chat')
    return render_template('login.html')

@app.route('/chat')
def chat():
    if not session.get('authenticated'):
        return redirect('/')
    return render_template('chat.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)