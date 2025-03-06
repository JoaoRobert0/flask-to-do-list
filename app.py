from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    tasks = ["Task 1", "Task 2", "Task 3"]
    return render_template('index.html', tasks = tasks)

if __name__ == "__main__":
    app.run(debug=True, port="8000")
