from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Belgrade, Serbia',
    'salary': '$1,700'
  },
  {
    'id': 2,
    'title': 'Data Scientis',
    'location': 'Novi Sad, Serbia',
    'salary': '$1,800'
  },
  {
    'id': 3,
    'title': 'Backend Developer',
    'location': 'Remote',
    'salary': '$1,500'
  },
  {
    'id': 4,
    'title': 'Data Analyst',
    'location': 'Belgrade, Serbia',
    'salary': '$1,700'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)