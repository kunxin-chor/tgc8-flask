from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.template.html')


@app.route('/about-me/<first_name>/<last_name>')
def about_me(first_name, last_name):
    return render_template('about_me.template.html', 
                            fname=first_name, lname=last_name)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
