from flask import Flask, render_template, request, redirect, url_for
import os

# To create the Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("homepage.template.html")


@app.route('/author/<author_name>')
def search_by_author(author_name):
    return render_template('author_search.template.html', aname=author_name)


if __name__ == '__main__':
    # this is the line that starts the server
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


