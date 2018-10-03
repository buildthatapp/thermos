from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

bookmarks = []

def store_bookmarks(url):
    bookmarks.append(dict(
        url = url,
        user = "reindert",
        date = datetime.utcnow()
    ))
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmarks(url)
        app.logger.debug('stored url: ' + url)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)