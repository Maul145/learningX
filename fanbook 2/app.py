from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://maulana:n1qN5w52LPcfvXpZ@cluster0.bekirsw.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp')
db = client.maulana
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST request!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    return jsonify({'msg':'GET request!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

    # n1qN5w52LPcfvXpZ