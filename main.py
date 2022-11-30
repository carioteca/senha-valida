import json

from flask import Flask, jsonify, make_response, request

import func

app = Flask(__name__)

@app.route('/verify', methods=['POST'])
def my_def():
    
    func.no_match.clear()
    func.verify = 0
    data = request.get_json()
    for regras in data['rules']:

        if regras['rule'] == "minSize":
            func.min_size_def(data['password'], regras['value'])

        if regras['rule'] == "minUppercase":
            func.min_upper_def(data['password'], regras['value'])

        if regras['rule'] == "minLowercase":
            func.min_lower_def(data['password'], regras['value'])

        if regras['rule'] == "minDigit":
            func.min_dig_def(data['password'], regras['value'])

        if regras['rule'] == "minSpecialChars":
            func.min_special_def(data['password'], regras['value'])

        if regras['rule'] == "noRepeted":
            func.change_pos_def(data['password'])

    if func.verify == len(data['rules']):
        func.verify = True
    
    else:
        func.verify = False
    return make_response(
        jsonify(noMatch = str(func.no_match), verify = str(func.verify))
    )

if __name__ == '__main__':
     app.run(host='localhost', port=8080, debug=True)