from flask import Flask, request, redirect, render_template
import validators
import cgi

app = Flask(__name__)
app_static_folder = "./static"

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=["POST"])
def validate_signup():

    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form ["email"]

    username_error = validators.general_validator(username)
    password_error = validators.general_validator(password)
    verify_password_error = validators.verify_pw_validator(password, verify_password)
    email_error = validators.email_validator(email)


    if not username_error and not password_error and not verify_password_error and not email_error:
        return "Success!"
    else:
        return html.format(username_error=username_error,
            password_error=password_error,
            verify_password_error=verify_password,
            email_error=email) 

app.run()
