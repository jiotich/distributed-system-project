import os
import json

class Configs:
    config = json.load(open(os.getcwd() + "/../config.json"))
        
    
    