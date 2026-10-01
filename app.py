from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Imagine we pulled this data from your SQLite database!
    hospital_name = "City Care Hospital"
    active_doctors = ["Dr. Smith (Cardiology)", "Dr. Jones (Pediatrics)", "Dr. Lee (Neurology)"]
    
    # We pass these Python variables into our HTML file
    return render_template('home.html', name=hospital_name, doctors=active_doctors)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the user clicks the "Login" button on the form...
    if request.method == 'POST':
        # We grab the data using the 'name' attributes from the HTML inputs
        username = request.form['username']
        password = request.form['password']
        
        # We will add database logic here later. For now, let's just prove it works:
        return f"Hello {username}! You tried to login with password: {password}. (Database coming soon!)"
        
    # If they just clicked a link to view the page...
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        # We will save this patient to the DB later
        return f"Success! Patient {name} (username: {username}) is registered! (DB coming soon)"
        
    return render_template('register.html')

@app.route('/patient/dashboard')
def patient_dashboard():
    # Hardcoded for now, later we will get the real logged-in user's name
    return render_template('patient_dashboard.html', patient_name="John Doe")

if __name__ == '__main__':
    app.run(debug=True)
