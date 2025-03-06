from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # Instance of SQLAlchemy

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(100), unique = True, nullable = False)

@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks = tasks)

@app.route('/task/create', methods=["POST"])
def create_task():
    description = request.form['description']

    if Task.query.filter_by(description = description).first() != None:
        return "Error: Task doesnt exist", 404

    new_task = Task(description = description)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@app.route('/task/delete/<int:task_id>', methods=["POST"])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/')

@app.route('/task/update/<int:task_id>', methods=["POST"])
def update_task(task_id):
    task = Task.query.get(task_id)

    if task:
        task.description = request.form['description']
        db.session.commit()

    return redirect("/")
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port="8000")
