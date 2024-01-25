from flask import Flask

app = Flask(__name__)
print("__name__ is: ",__name__)
@app.route("/")
def index():
    return "<p style='color:red'> This is Home page</p>"
@app.route("/about")
def about():
    return "<p style='color:blue'> This is About page</p>"

@app.route("/contact")
def contact():
    return "<p style='color:violet'> This is Contact page</p>"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5001')
