from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello, Manoj! Today is {date.today()}."

@app.route("/about")
def about():
    return "Project: Airline Crew Scheduling | Case 57"

if __name__ == "__main__":
    app.run(debug=True)