from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.String())
    date = db.Column('date_published', db.DateTime,
                     default=datetime.datetime.now)
    description = db.Column('description', db.Text)
    skills = db.Column('skills', db.Text)
    repo_url = db.Column('repo_url', db.Text)

    def __repr__(self):
        return f'''
        Project Title: {self.title}
        Published Date: {self.date}
        Description: {self.description}
        Skills Learned: {self.skills}
        GitHub Repo Link: {self.repo_url}'''
