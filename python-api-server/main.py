from cgitb import reset
import re
from time import sleep
from traceback import print_tb
from urllib import response
from flask import Flask, request, jsonify
from flask.templating import render_template
import json
import datetime
import utils
import time
  


app = Flask(__name__)
agentsData = [[]]
ec2 = utils.ec2()
@app.route('/statso/', methods=['GET'])
def deep_stats():
    ol = []
    for j in agentsData:
        lastTen = j[-10:]
        id = j[0]["id"]
        totalRam = j[0]["totalmem"]
        name = j[0]["name"]

        avgo = []
        cpuo = []

        for i in lastTen:
            avgo.append((i["freemem"]/totalRam)*100)
            cpuo.append(i["cpuprecent"])

        avg = sum(avgo) / len(avgo)
        avgc = sum(cpuo) / len(cpuo)

        o = {}
        o["id"] = id
        o["ramUtil"] = avg
        o["cpuUtil"] = avgc
        o["name"] = name
        # for i in ec2:
        #     if i["name"] == name :
        #         o["state"] = i["state"]
        ol.append(o)
    return jsonify(ol) 

@app.route('/stats/', methods=['GET'])
def get_stats():
    return jsonify(agentsData)


@app.route('/api/', methods=['GET', 'POST'])
def get_data():
    data = request.json
    data["ts"] = int(time.time())
    index = data["id"] - 1
    agentsData[index].append(data)
    
    return 'OK', 200 

@app.route('/', methods=['GET', 'POST'])
def ec2():
    ec2 = utils.ec2()
    return jsonify(ec2)
    
app.run(host='0.0.0.0', debug=True, port=3000)