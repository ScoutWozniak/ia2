from flask import Flask, render_template, request, session
from password import check_user_credentials
from points import *
from user import User, GetUserFromCode, GetUserFromEmail
app = Flask(__name__)


def IsLoggedIn():
    return 'email' in session

@app.route('/')
def home():
    name = ""
    if IsLoggedIn():
        name = GetUserFromEmail(session['email']).name
    return render_template('index.html', items=GetHousePoints(), loggedIn = IsLoggedIn(), name=name)

@app.route('/login', methods=['POST', 'GET'])
def checkLogin():
    result = False
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = check_user_credentials(email, password)
        if result:
            # Save the form data to the session object
            session['email'] = email
            return home()
        else:
            error="Invalid password or username"
    return render_template('login.html', error=error, loggedIn = IsLoggedIn())


@app.route('/loginpage')
def loginPage():
    return render_template('login.html', loggedIn = IsLoggedIn())

@app.route('/recordpoints', methods=['POST', 'GET'])
def recordPoints():
    if (request.method == 'POST'):
        # Make sure runner is real 
        user = request.form['studentNo']
        place = request.form['place']
        time = ""
        type = "NC"
        if 'time' in request.form:
            time = request.form['time']
            type = "C"
        # More error checks
        GivePoints(user, type, place, time)
        # ADD RESULTS
        pass
    
    return render_template('pointrecord.html', loggedIn = IsLoggedIn())

def nominationStudent():
    curUser = GetUserFromEmail(session['email'])
    if (request.method == 'POST'):
        if (curUser.IsNominated()):
            curUser.UnNominate()
        else:
            curUser.Nominate()
    
    return render_template('studentnom.html', loggedIn = IsLoggedIn(), nominated = curUser.IsNominated())

@app.route('/nominate', methods=['POST', 'GET'])
def nominationPage():
    # If the user is not logged in, redirect to the home page
    if not IsLoggedIn():
        return home()
    
    # If the user is a student, redirect to the student nomination page
    if GetUserFromEmail(session['email']).role == "Student":
        return nominationStudent()

    if (request.method == 'POST'):
        TempUser = None

        # Basic error handling incase the user does not exist
        try:
            TempUser = GetUserFromCode(request.form['code'])
        except:
            return render_template('nominations.html', error="Invalid Code", loggedIn = IsLoggedIn())
        
        # If the user is not a student, exit
        if TempUser.role != "Student":
            return render_template('nominations.html', error="User is not a student", loggedIn = IsLoggedIn())
        
        # If the student is already nominated, exit
        if TempUser.IsNominated():
            return render_template('nominations.html', error="User already nominated", loggedIn = IsLoggedIn())
        
        TempUser.Nominate()
        return render_template('nominations.html', success="User nominated", loggedIn = IsLoggedIn())

    return render_template('nominations.html', loggedIn = IsLoggedIn())

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)