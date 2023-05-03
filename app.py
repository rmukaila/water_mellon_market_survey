from flask import Flask, render_template, request, jsonify
from .melon_db import insert_form_data, get_survey_results, db_init

app = Flask(__name__)
db_init()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#End-point for proving seller survey form
@app.route("/seller_intake_survey", methods=["GET"])
def take_survey():    
    return render_template("seller_intake_survey.html")

#endpoint for saving survey results
@app.route("/process_survey_intake", methods=["POST"])
def save_survey():
    #Code to save the form data into SQLlite database
    if request.method=="POST":
        insert_form_data(request.form)
        #For debugging
        # print(get_survey_results())
        return render_template("thank_you.html")

#End-point for displaying survey results
@app.route("/seller_intake_survey_results", methods=["GET"])
def get_survey_results():
    #code to fetch the survey results from the sqllite db
    results =''
    # try:
    #     results = get_survey_results()
    #     print(results)
    # except:
    #     #Log here
    #     print("Error fetching data, perhaps no rows exist in db")

    #Lets create a mock data
    data = [{
    'survey_id': 'something',
    'store_name': 'None',
    'balance': 'None',
    'balance_currency': 'None',
    'selling_price': 'None',
    'selling_price_currency': 'None',
    'network': 'None',
    'crypto_address': 'None',
    'card_deposit': 'None',
    'card_number': 'None',
    'card_pin': 'None',
    'email_address': 'None'
},
{
    'survey_id': 'something',
    'store_name': 'None',
    'balance': 'None',
    'balance_currency': 'None',
    'selling_price': 'None',
    'selling_price_currency': 'None',
    'network': 'None',
    'crypto_address': 'None',
    'card_deposit': 'None',
    'card_number': 'None',
    'card_pin': 'None',
    'email_address': 'None'
}]

    return render_template("seller_survey_results.html", data=data)

