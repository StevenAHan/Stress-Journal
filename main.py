import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'not so secret'

@app.route('/')
def home():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created ASC').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        rating = request.form['rating']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, rating, content) VALUES (?, ?, ?)',
                         (title, rating, content))
            conn.commit()
            conn.close()
            return redirect(url_for('home'))

    return render_template('create.html')

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

if __name__ == "__main__":
    app.run(debug=True)