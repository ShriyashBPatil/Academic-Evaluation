from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
app.secret_key = 'your-secret-key'

cred = credentials.Certificate(r'./privatekey.json') 
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def home():
    if 'user' in session:
        return 'Logged in as ' + session['user']['email']
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            # Assuming you have a way to verify the user's credentials and fetch their role
            user = db.collection('Users').where('email', '==', email).get()
            if user:
                user_data = user[0].to_dict()
                session['user'] = {'email': email, 'role': user_data['role']}
                if user_data['role'] == 'student':
                    return redirect(url_for('student_dashboard'))
                else:
                    return redirect(url_for('home'))
            else:
                return 'Login failed'
        except Exception as e:
            return f'An error occurred: {str(e)}'
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']  # Get the role from the form
        try:
            # Save user data including role to session or database
            session['user'] = {'email': email, 'role': role}  
            return redirect(url_for('home'))
        except:
            return 'Signup failed'
    return render_template('signup.html')

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'role': request.form['role'],
            'class': request.form['class'],
            'Programme':request.form['Programme'],
            'Examination':request.form['Examination'],
            'date':request.form['date']
        }
        try:
            db.collection('Students').add(data)
            return 'Data added successfully'
        except Exception as e:
            return f'An error occurred: {str(e)}'
    return render_template('add_data.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/student_dashboard')
def student_dashboard():
    if 'user' in session and session['user']['role'] == 'student':
        return render_template('dashboard.html')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
