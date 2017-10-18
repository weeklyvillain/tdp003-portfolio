from flask import Flask, render_template, request
from data import *

app = Flask(__name__)

db = load('data.json')
tech = get_techniques(db)

keys = get_keys(db)

@app.errorhandler(404)
def page_not_found(e):
    error=e.description + " Error: 500"
    return render_template('fel.html', error=error)

@app.errorhandler(500)
def page_not_found(e):
    error="Projektet kunde inte hittas, Error: 404"
    return render_template('fel.html', error=error)

@app.route("/")
def index():
    db = load('data.json')
    l = search(db, 'start_date', 'desc')
    l = l[:2]
    
    return render_template("index.html" , projects=l)


@app.route("/list", methods=["GET"])
def list():
    db = load('data.json')
    project_lst = []
    
    search_term = request.args.get("search_word", default=None)
    sort_o = request.args.get("sort_order")
    sort_b = request.args.get("sort_by")
    tech_lst = request.args.getlist("tech_lst")
    field_lst = request.args.getlist("field_lst")

    project_lst = search(db, sort_by=sort_b, sort_order=sort_o, techniques=tech_lst, search=search_term, search_fields=field_lst)
    
    return render_template("list.html" , projects=project_lst, tech=tech, keys=keys)

@app.route("/techniques", methods=["GET"])
def techniques():
    db = load('data.json')
    technique = request.args.get("submit")
    project_lst = []    
    if technique != None:
        project_lst = technique_search(db, [technique])
    else:
        project_lst = technique_search(db, tech)   
    return render_template("tech.html", tech=tech, projects=project_lst)

@app.route("/project/<int:id>")
def project(id):
    db = load('data.json')
    project = get_project(db, id)
    return render_template("project.html", project=project)


if __name__ == "__main__":
    app.run()
