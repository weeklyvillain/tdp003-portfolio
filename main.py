from flask import Flask, render_template, request
from data import *

app = Flask(__name__)

db = load('data.json')
tech = get_techniques(db)

@app.route("/")
def index():
    return render_template("index.html" , projects=db, tech=tech)


@app.route("/list", methods=["GET"])
def list():
    project_lst = []
    
    search_term = request.args.get("search_word", default=None)
    sort_o = request.args.get("sort_order")
    sort_b = request.args.get("sort_by")
    tech_lst = request.args.getlist("tech_lst")
    field_lst = request.args.getlist("field_lst")

    project_lst = search(db, sort_by=sort_b, sort_order=sort_o, techniques=tech_lst, search=search_term, search_fields=field_lst)

    return render_template("list.html" , projects=project_lst, tech=tech)

@app.route("/techniques", methods=["GET"])
def techniques():
    technique = request.args.get("submit")
    project_lst = []    
    if technique != None:
        project_lst = technique_search(db, [technique])
    else:
        project_lst = technique_search(db, tech)   
    return render_template("tech.html", tech=tech, projects=project_lst)

@app.route("/project/<int:id>")
def project(id):
    project = get_project(db, id)
    return render_template("project.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)
