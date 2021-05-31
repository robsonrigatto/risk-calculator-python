from flask import Flask,request
from .services import risk_service
import json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/risk/calculate', methods=['POST'])
def calculate():
    request_data = request.get_json()
    score = risk_service.calculate(request_data)

    return json.dumps(score, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

app.run()