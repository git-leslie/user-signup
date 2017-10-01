from flask import Flask, request, redirect, render_template
import validators
import cgi

app = Flask(__name__)
app_static_folder = "./static"

app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html') #pulls this page when loading page


@app.route("/", methods=["POST"])
def validate_signup():

    username = request.form["username"] #gets whatever they typed in username text box
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    username_error = validators.general_validator(username) #if error run this function
    password_error = validators.general_validator(password)
    verify_password_error = validators.verify_pw_validator(password, verify_password)
    email_error = validators.email_validator(email)


    if not username_error and not password_error and not verify_password_error and not email_error: #if no errors, it's good!
        #return "Welcome, {}!".format(username)
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', #if errors, do this
                                username=username, #passing variable back to form ????????????????
                                email=email,        #send variable username to html
                                username_error=username_error, #send white username back to html with blue username as variable name
                                password_error=password_error, #passess the value of the username variable(white) under the keyname to the template, so the template will render the words in {{ }}
                                verify_password_error=verify_password_error,
                                email_error=email_error) 

app.run()
