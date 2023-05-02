from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/seller_intake_survey")
def take_survey():
    
    return render_template("seller_intake_survey.html")

@app.route("/process_survey_intake")
def process_survey():

    #Code to save the form data into SQLlite database
    pass

@app.route("/seller_intake_survey_results")
def get_survey_results():
    #code to fetch the survey results from the sqllite db
    pass

