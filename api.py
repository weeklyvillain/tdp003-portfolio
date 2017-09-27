import json, copy
from pprint import pprint

def sort_projects(lst):
    """Sort_projects tar in en lista med listor och sorterar projekten efter project_no: i dicten"""
    for i, item in enumerate(lst):
        lst.insert(item[0]['project_no'] - 1, lst.pop(i))

def load(file_name):
    """Läser in en json fil samt sorterar listan efter project_no:"""
    try:
        with open(file_name) as data_file:
            data = json.load(data_file)
    except:
        return None
    sort_projects(data)
    return data

def get_project_count(db):
    number = len(db)
    return number

def get_project(db, id):
    try:
        lst = db[id - 1]
    except:
        return None
    project = lst[0]
    return project

def get_techniques(db):
    techniques = []
    for item in db:
        for t in item[0]['techniques_used']:
            if not t in techniques:
                techniques.append(t)
    techniques = sorted(techniques, key=str.upper)
    return techniques

def get_project_name(db, id):
    try:
        return db[id][0]['project_name']
    except:
        return None

def get_technique_stats(db):
    technique_dict = {}
    for i, item in enumerate(db):
        for t in item[0]['techniques_used']:
            if not t in technique_dict:
                technique_dict[t] = [{'id': i + 1, 'name': get_project_name(db, i)}]
            else:
                technique_dict[t].append({'id': i + 1, 'name': get_project_name(db, i)})

    return technique_dict

def technique_search(db, techniques):
    projects = []
    provar = get_technique_stats(db)
    for t in techniques:
        if t in provar:
            for p in provar[t]:
                if not [get_project(db, p['id'])] in projects:
                    projects.append([get_project(db, p['id'])])

    return projects

def string_search(db, search_term):
    projects = []
    for i, item in enumerate(db):
        for p in item[0]:
            if search_term.lower() in str(db[i][0][p]).lower() and not [get_project(db, i+1)] in projects:
                projects.append([get_project(db, i+1)])
    return projects

def fields_search(db, search_fields, search):
    projects = []
    for i, item in enumerate(db):
        for p in item[0]:
            if p in search_fields:
                if search.lower() in db[i][0][p].lower() and not [get_project(db, i+1)] in projects:
                    projects.append([get_project(db, i+1)])
    return projects
               
def by_sorter(project_lst, search_by, sort_order, db):
    projects = []
    s_project_list = []
    for i, item in enumerate(project_lst):
        for p in item[0]:
            if str(p) in search_by:
                projects.append((item[0][str(p)] , item[0]['project_no']))
    if sort_order == 'asc':
        projects.sort(reverse=True)
    else:
        projects.sort()

    for item in projects:
        s_project_list.append(get_project(db, item[1]))

    return(s_project_list)    
    
    
        

def search(db, sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None):
    project_lst = []
    if techniques != None:
        project_lst = technique_search(db, techniques)
    else:
        project_lst = copy.copy(db)
        
    if search_fields != None:
        project_lst = fields_search(project_lst, search_fields, search)
    else:
        project_lst = string_search(project_lst, search)

    project_lst = by_sorter(project_lst, sort_by, sort_order, db)


        
    return project_lst







    
