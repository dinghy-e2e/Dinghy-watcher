# from random import randint
from cgitb import reset
import re
from time import sleep
from traceback import print_tb
from urllib import response
import requests
from flask import Flask
from flask.templating import render_template
import json
import datetime
# import urllib.request 

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

with open('test.json', 'r') as f:
    data_json = json.loads(f.read())
# data_json = [
#     "https://walla.co.il",
#     "https://surecomp.com/",
#     "https://www.viagogo.com/il/Concert-Tickets/World-Music/Eyal-Golan-Tickets/E-150257809",  
#   ]

# accessed via <HOST>:<PORT>/app.route path
# Global vars. 
# read from json file.
# file = open('test.json', mode='r+', encoding='UTF-8')
# load = json.loads( file.read() )
# data = requests.get(load)



app = Flask(__name__)
#@@@ITAY-TEST@@@#
# @app.route("/get_random")
# def random():
#     random_number = randint(1, 10)
#     return {'random': random_number}, 200 # status code
#@@@ITAY-TEST@@@#


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", utc_dt=datetime.datetime.utcnow())


# check flask(welcompage)
@app.route('/itay')
def hello_user():
    return 'Watcher', 200 # status code

# <create json file local>
# add urls from web TODO
@app.route("/register")
def welcome():
    with open("test.txt", 'a+') as test:
        test.write("hello")
    return "success", 201 # status code


        
@app.route("/status" , methods=['GET', 'POST'])       
def status():
 with open('test.json', 'r') as f:
    data_json = json.loads(f.read())
    return render_template("index.html", url=(data_json), responses = get_status())



def get_status():
    resps = []
    for url in data_json["URLS"]:
        try:
            response = requests.get(url)
            resps.append(response.status_code)
        except:
            resps.append("Error")    
    return resps    
    
         
app.run(host='127.0.0.1', debug=True, port=30000)