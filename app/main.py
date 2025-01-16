from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route("/")
def get_current_time():
    current_time = time.strftime("%Y-%m%d %H:%M:%S", time.localtime())
    return f"The current time now is: {current_time}"


@app.route('/hello', methods=['GET'])
def hellowrld():
    if(request.method == 'GET'):
        data = {"data": "Hello World Application"}
        return jsonify(data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
