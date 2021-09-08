from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Lesson(db.Model):
    id: db.Column(db.Integer, primary_key=True)


# Home Route
@app.route('/')
def index():
    return 'Hello!'

# All lesson plans
@app.route('/plans')
def get_plans():
    return{"Plans": "Plan Data"}

# Lesson plan by ID
@app.route('/plans/:id')
def get_plans():
    return{"Plans": "Plan Data"}
