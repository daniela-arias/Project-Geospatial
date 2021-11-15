import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
from functools import reduce
import operator


def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def type_point(lista):
    return {"type":"Point", "coordinates": lista}

import re
def extraetodo(json):
    todo = {"nombre": ["name"], "latitud": ["location", "lat"], "longitud": ["location", "lng"]} 
    total = []
    for elemento in json:
        libre = {key: getFromDict(elemento, value) for key,value in todo.items()}
        libre["location"] = type_point([libre["latitud"], libre["longitud"]])
        total.append(libre)
    return total