# Description
This is a microproject developed in flask to receive and display watermelonmarkets seller surveys. The app has been deployed on render.com and the survey form can be seen at: https://watermelonmarketssurvey.onrender.com/seller_intake_survey . WHile the survey results can be reached at https://watermelonmarketssurvey.onrender.com/seller_intake_survey_results .

# Note: Because the app is hosted on a free server, the site might be a bit slow. Also since sqlite was used to store the data, any redeployments may wipe out previous data.


## How to run the app on local machine

## Prerequisits/dependencies for running the app without docker
### 1- python3
### 2- pip version 20 and above

- Clone the repository with either https link (depends on your git configuration):

    #shell command:

        git clone https://github.com/rmukaila/water_mellon_market_survey_flask.git

    OR with ssh link (depends on your git configuration):

        git clone git@github.com:rmukaila/water_mellon_market_survey_flask.git
       

- cd into the repository folder, create the environment for the project
#shell commands:

        1) cd water_mellon_market_survey_flask
        2) python -m venv env_watermelon

- Activate the created environment and install the dependencies
    #Shell commands

    For windows machines, type the following and click enter:
            
            .\env_watermelon\Scripts\activate

    For Linux machines type the following and click enter:

                source env_watermelon/bin/activate

    #install dependencies while env is activated

        pip install -r requirements.txt

- Start the app to see the website live!

    #Shell command

    
        flask run --reload

- That's it!
    to to see the survey form, visit this link in your browser
    http://127.0.0.1:5000/seller_intake_survey

    To see the survey results page visit:
    
    http://127.0.0.1:5000/seller_intake_survey_results


# How to run app with docker