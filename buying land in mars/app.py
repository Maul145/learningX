from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://yusuf:yusuf123@cluster0.trndiac.mongodb.net/?retryWrites=true&w=majority')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    doc = {
        'name' : name_receive,
        'address' : address_receive,
        'size' : size_receive
    }
    return jsonify({'msg': 'POST request!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    return jsonify({'msg': 'GET request!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)