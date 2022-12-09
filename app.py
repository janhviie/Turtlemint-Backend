from flask import Flask,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = '123456789abcdef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    vehicleType = db.Column(db.String(100), nullable=False)
    vehicleMaker = db.Column(db.String(100), nullable=False)
    vehicleOilType = db.Column(db.String(100))
    

@app.route('/')
@app.route('/home')
def home():
    return "Hello"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)