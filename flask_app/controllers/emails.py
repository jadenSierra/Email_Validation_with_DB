from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email_model import Email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/email/save", methods=['POST'])
def save():

    if not Email.validate_email(request.form):
        return redirect('/')

    data = {
        'email' : request.form['email'],
        "id" : request.form['id']
    }

    Email.save(data)

    return redirect("/email")

@app.route('/email')
def emails():

    emails = Email.get_all()
    print(emails)
    return render_template("success.html", emails = emails)