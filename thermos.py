from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
from forms import BookmarkForm

app = Flask(__name__)

bookmarks = []
app.config['SECRET_KEY'] = "b'/J\xbf@\x17\xbcg#\x85\xcd\xc3\x0e\x1b\xcfa\x02r\x82\xd5\xfb\xf5\xc9\x1dc"
def store_bookmark(url, description):
    bookmarks.append(dict(
        url = url,
        description = description,
        user = "Louis Magdaleno",
        date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True) [:num]
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)