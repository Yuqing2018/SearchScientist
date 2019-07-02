from datetime import datetime
from flask import Flask, render_template
from . import app
from hello_app.sparql import GetScientists

@app.route("/")
def home():
    result = reformatData(GetScientists())
    count = len(result)
    return render_template("todayScientists.html", result=result,totalCount = count)

def reformatData(rs):
    result =[]
    print(len(rs))
    # for index, row in df.iterrows():
    #     temp ={}
    #     temp['entityLabel'] = row['entityLabel.value']
    #     temp['genderLabel'] = row['genderLabel.value']
    #     temp['entityImage'] = row['entityImage.value']
    #     temp['birthPlace'] = row['birthPlaceLabel.value']
    #     temp['entityDescription'] = row['entityDescription.value']
    #     temp['year'] = row['year.value']
    #     result.append(temp)
    for line in rs:
        keys = line.keys()
        temp ={}
        temp['entity'] = line['entity']['value'] if 'entity' in keys else ""
        temp['entityImage'] = line['entityImage']['value'] if 'entityImage' in keys else ""
        temp['entityLabel'] = line['entityLabel']['value'] if 'entityLabel' in keys else ""
        temp['genderLabel'] = line['genderLabel']['value'] if 'genderLabel' in keys else ""    
        temp['birthPlace'] = line['birthPlaceLabel']['value'] if 'birthPlaceLabel' in keys else ""
        temp['entityDescription'] = line['entityDescription']['value'] if 'entityDescription' in keys else ""
        temp['year'] = line['year']['value'] if 'year' in keys else ""
        result.append(temp)
    return result
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
