import sqlite3
import random

#code to initialize database
def db_init():

    # define connection and cursor
    my_connection = sqlite3.connect('seller_survey.db') #REMEMBER TO OPEN AND CLOSE ALL CONNECTIONS IN EACH FUNCTION

    

    # create just one table for the seller survey inputs
    my_cursor = my_connection.cursor()
    create_statement = """CREATE TABLE IF NOT EXISTS 
    survey(survey_id INTEGER PRIMARY KEY, store_name TEXT, balance TEXT,
    balance_currency TEXT, selling_price REAL, selling_price_currency TEXT,
    network TEXT, crypto_address TEXT, card_deposit TEXT, card_number TEXT,
    card_pin TEXT, email_address TEXT)"""

    my_cursor.execute(create_statement)
    my_connection.close()
    

def insert_form_data(form_data):
    my_connection = sqlite3.connect('seller_survey.db')
    
    my_cursor = my_connection.cursor()
    #insert data 
    initial_insert_statement = "INSERT INTO survey VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"

    #Generate a random number touse as survey unique survey id
    rand_num = random.randint(1000, 10000)
    mylist = []
    mylist.append(rand_num)
    mylist.append(form_data['store_name'])
    mylist.append(form_data['balance'])
    mylist.append(form_data['balance_currency'])
    mylist.append(form_data['selling_price'])
    mylist.append(form_data['selling_price_currency'])
    mylist.append(form_data['network'])
    mylist.append(form_data['crypto_address'])
    mylist.append(form_data['card_deposit'])
    mylist.append(form_data['card_number'])
    mylist.append(form_data['card_pin'])
    mylist.append(form_data['email_address'])
    
    print(mylist)

    # initial_insert_statement = initial_insert_statement+str(tuple(mylist))
    my_cursor.execute(initial_insert_statement,tuple(mylist))
    my_connection.commit()
    my_connection.close()

def get_survey_results():
    #fetching results
    my_connection = sqlite3.connect('seller_survey.db')
    my_cursor = my_connection.cursor()
    my_cursor.execute("SELECT * FROM survey")
    results = [row for row in my_cursor.fetchall()]
    my_connection.close()

    return results

# survey_id, store_name, balance, balance_currency, selling_price, selling_price_currency, network, crypto_address, card_deposit, card_number, card_pin, email_address