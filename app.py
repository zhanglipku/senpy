#!/usr/bin/python
# -*- coding: utf-8 -*-
#    Copyright 2014 J. Fernando Sánchez Rada - Grupo de Sistemas Inteligentes
#                                                       DIT, UPM
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
'''
Simple Sentiment Analysis server for EUROSENTIMENT
'''
from flask import Flask
from random import random
from nif_server import *
import config

app = Flask(__name__)

def hard_analysis(params):
    response = basic_analysis(params)
    response["analysis"][0]["marl:algorithm"] = "SimpleAlgorithm"
    for i in response["entries"]:
        polValue = random()
        if polValue > 0.5:
            pol = "marl:Positive"
        elif polValue == 0.5:
            pol = "marl:Neutral"
        else:
            pol = "marl:Negative"
        i["opinions"] = [{"marl:polarityValue": polValue,
                          "marl:hasPolarity": pol

                          }]
    return response

app.analyse = hard_analysis
app.register_blueprint(nif_server)

if __name__ == '__main__':
    app.debug = config.DEBUG
    app.run()
