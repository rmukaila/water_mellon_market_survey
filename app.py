from flask import Flask, render_template, request, jsonify
from .melon_db import insert_form_data, get_survey_results, db_init

app = Flask(__name__)
db_init()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#View/end-point for serving seller survey form
@app.route("/seller_intake_survey", methods=["GET"])
def take_survey():    
    return render_template("seller_intake_survey.html")



#View/endpoint for saving survey results
@app.route("/process_survey_intake", methods=["POST"])
def save_survey():
    #Code to save the form data into SQLlite database
    if request.method=="POST":
        try:
            insert_form_data(request.form)
        except:
            return "<h2 style='margin:20%'>Sorry, your response could not be saved due to an error. Please try again later.</h2>"
        
        return render_template("thank_you.html")
    

#View/end-point for displaying survey results
@app.route("/seller_intake_survey_results", methods=["GET"])
def retrieve_survey_results():
    #code to fetch the survey results from the sqllite db
    results =''
    try:
        results = get_survey_results()

    except:
        return "<h2 style='margin:20%'>Sorry, there was an error getting the data. Please try again later.</h2>"
      
    return render_template("seller_survey_results.html", data=results)

