from flask import Flask, render_template, request, redirect, url_for
import os

# To create the Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("homepage.template.html")


@app.route('/author/<author_name>')
def search_by_author(author_name):
    # image we have code here that access a database
    # we can use the database to search for all the books by the author
    # and then pass it to the template to be rendered
    return render_template('author_search.template.html', aname=author_name)


@app.route('/latest-news')
def view_latest_news():
    return render_template('latest_news.template.html')


if __name__ == '__main__':
    # this is the line that starts the server
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


