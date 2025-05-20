from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        return f"<h2>Thank you, {name}! Your message was received.</h2>"
    return '''
        <form method="POST">
            <label>Name:</label><br>
            <input type="text" name="name"><br>
            <label>Message:</label><br>
            <textarea name="message"></textarea><br><br>
            <input type="submit" value="Send">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
