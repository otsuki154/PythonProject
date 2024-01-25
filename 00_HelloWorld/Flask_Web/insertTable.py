from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/dvdrental'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)

    def __init__(self,name, age):
        self.name = name
        self.age = age

@app.route('/addCat', methods=['POST'])
def addCat():
    name = request.form['name']
    age = request.form['age']
    newCat = Cat(name,age)
    db.session.add(newCat)
    db.session.commit()

    return '<h1>Hello, New cat is inserted!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
