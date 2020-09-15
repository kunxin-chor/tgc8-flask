from flask import Flask, render_template, request, redirect, url_for
import os

# To create the Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return "home"


@app.route('/booking', methods=['GET'])
def show_booking_form():
    return render_template('show_booking_form.template.html')


@app.route('/booking', methods=['POST'])
def process_booking_form():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    return render_template("say_hello.template.html",
                           fname=first_name, lname=last_name)


if __name__ == '__main__':
    # this is the line that starts the server
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
