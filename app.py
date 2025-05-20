from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create table
def init_db():
    conn = sqlite3.connect('reviews.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS reviews
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 rating INTEGER,
                 comment TEXT)''')
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect('reviews.db')
    if request.method == "POST":
        name = request.form["name"]
        rating = int(request.form["rating"])
        comment = request.form["comment"]
        conn.execute("INSERT INTO reviews (name, rating, comment) VALUES (?, ?, ?)", (name, rating, comment))
        conn.commit()

    cursor = conn.execute("SELECT name, rating, comment FROM reviews")
    reviews = cursor.fetchall()

    # Calculate average rating
    cursor = conn.execute("SELECT AVG(rating) FROM reviews")
    avg_rating = cursor.fetchone()[0]
    conn.close()

    return render_template("index.html", reviews=reviews, avg_rating=round(avg_rating, 2) if avg_rating else 0)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
