from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/dvdrental'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)

    def __init__(self,name, age):
        self.name = name
        self.age = age


@app.route("/")
def index():
    return "<p style='color:red'> This is Home page</p>"

@app.route('/createCat')
def createCat():
    # Đảm bảo rằng trong hàm route hoặc nơi bạn muốn tạo bảng, bạn sử dụng
    # context ứng dụng bằng cách sử dụng app.app_context()
    with app.app_context():
        db.create_all()
    return '<h1>Hello, Cat table is created!</h1>'

#Dung postman de gui request
@app.route('/addCat', methods=['POST'])
def addCat():
    name = request.form['name']
    age = request.form['age']
    newCat = Cat(name,age)
    db.session.add(newCat)
    db.session.commit()

    return '<h1>Hello, New cat is inserted!</h1>'

@app.route('/getAll')
def getAllCat():
    cats = Cat.query.all()
    #bắt buộc file html phải để trong thư mục có tên là templates để cho framework dò tìm file tương ứng
    return render_template('allCat.html',myCats=cats)

if __name__ == '__main__':
    app.run(debug=True)
