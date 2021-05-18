from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"code":200, "message":"ok!", "data":'Hello World 世界 ！！！'})

if __name__ == '__main__':
    app.run(debug=True)