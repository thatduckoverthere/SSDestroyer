from flask import Flask, render_template, request, jsonify 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST']) 
def process(): 
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    result = data['value']
    print(result)
    return jsonify(result=result) # return the result to JavaScript 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
