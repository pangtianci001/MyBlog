from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="myblog"
    )

@app.route('/')
def home():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
    posts = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("home.html", posts=posts)

@app.route('/post/<int:id>')
def post(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM posts WHERE id=%s", (id,))
    post = cursor.fetchone()
    cursor.close()
    db.close()
    return render_template("post.html", post=post)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO posts (title, content) VALUES (%s, %s)",
            (title, content)
        )
        db.commit()
        cursor.close()
        db.close()

        return redirect('/')
    
    return render_template("create.html")

if __name__ == '__main__':
    app.run(debug=True)