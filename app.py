from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"name": "hamid"})

@app.route('/user')
def user():
    return jsonify({"user": "john"})

    
if __name__ == '__main__':
    app.secret_key='my456samplesecret'
    app.run(debug=False)