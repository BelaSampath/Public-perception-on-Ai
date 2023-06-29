from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def Artificial_Intelligence():
    return render_template("index.html")

@app.route('/DashBoard.html')
def courses():
    return render_template("DashBoard.html")

@app.route('/StoryBoard.html')
def events():
    return render_template("StoryBoard.html")

@app.route('/Charts.html')
def pricing():
    return render_template("Charts.html")

@app.route('/about.html')
def win():
    return render_template("about.html")

@app.route('/contact.html')
def sent():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug = True, port = 5000)