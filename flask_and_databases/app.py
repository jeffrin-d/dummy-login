from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://vosyfbarqxizvz:a43b0d865deff2b6202b4bfcb0312e40ce94b54818f2c7592543a0c5a2b52081@ec2-3-89-0-52.compute-1.amazonaws.com:5432/d7jeddrhirnd7r?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email_ = email
        self.height_ = height

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method == 'POST':
        file=request.files["file"]
        file.save(secure_filename("uploaded"+file.filename))
        with open("uploaded"+file.filename, "a") as f:
            f.write("This line was added later!")
       # email=request.form["email_name"]
       # height=request.form["height_name"]
       # if db.session.query(Data).filter(Data.email_==email).count() == 0:
       #     data=Data(email, height)
       #     db.session.add(data)
       #     db.session.commit()
       #     avg_height=db.session.query(func.avg(Data.height_)).scalar()
       #     avg_height=round(avg_height, 1)
       #     count=db.session.query(Data.height_).count()
       #     send_email(email, height, avg_height, count)
        return render_template("index.html", btn="download.html")

       # return render_template("success.html")
       # else:
       #     return render_template("index.html", 
       #     text="Seems like that email address has already been used, try another address!")

@app.route("/download")
def download():
    return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)

if __name__ == '__main__':
    app.debug=True
    app.run(port=5001)