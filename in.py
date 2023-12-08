from flask import Flask,jsonify,request
from flask_cors import CORS  
from utils import *
app = Flask(__name__)
CORS(app)

@app.route('/classify', methods=['POST'])
def classify_api():
    your_instance = YourClass()
    data = request.get_json()
    post_text = data['post_text']
    result = your_instance.classify(post_text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=3000)
    