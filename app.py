from flask import (render_template, url_for, request, redirect)
from datetime import datetime
from models import db, Project, app


def clean_date(date_str):
    return datetime.strptime(date_str, '%Y-%m')


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    projects = Project.query.all()
    if request.form:
        new_project = Project(title=request.form['title'], date=clean_date(request.form['date']),
                              description=request.form['description'], skills=request.form['skills'], repo_url=request.form['repo_url'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/projects/<id>')
def detail(id):
    projects = Project.query.all()
    project = Project.query.get(id)
    return render_template('detail.html', projects=projects, project=project)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get(id)
    projects = Project.query.all()
    if request.form:
        project.title = request.form['title']
        project.date = request.form['date']
        project.description = request.form['description']
        project.skills = request.form['skills']
        project.repo_url = request.form['repo_url']
        db.session.commit()
        return redirect(url_for('index.html'))
    return render_template('projectform.html', project=project, projects=projects)


@app.route('/projects/<id>/delete')
def delete_project(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
