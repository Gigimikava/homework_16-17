from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('login.html')

# Logout page
@app.route('/logout')
def logout():
    return render_template('logout.html')

# Registration form
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('registration.html')

# Search form
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Perform search logic here
        return redirect(url_for('search_results'))
    return render_template('search.html')

if __name__ == '__main__':
    app.run()
