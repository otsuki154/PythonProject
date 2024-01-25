from flask import Flask, request, render_template
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

@app.route('/getAll')
def getAllCat():
    cats = Cat.query.all()
    #bắt buộc file html phải để trong thư mục có tên là templates để cho framework dò tìm file tương ứng
    return render_template('allCat.html',myCats=cats)


if __name__ == '__main__':
    app.run(debug=True)
