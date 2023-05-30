from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #using SQLAlchemy as database
app = Flask(__name__) #using Flask as web framework
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app) 


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Integer)
    # 0 - not complete, 1 - in progress, 2 - completed


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=0) #new to do not complete by default
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home")) #return to "updated" homepage when submitting new to do


@app.route("/update/<int:todo_id>")
def update(todo_id): #establishing workflow for update button - not started, ongoing, complete
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo.complete == 0:
        todo.complete = 1
    elif todo.complete == 1:
        todo.complete = 2
    else:
        todo.complete = 0
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):#defining delete button
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
