from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # Instance of SQLAlchemy

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(100), unique = True, nullable = False)

@app.route("/")
def index():
    tasks = ["Task 1", "Task 2", "Task 3"]
    return render_template('index.html', tasks = tasks)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port="8000")
