from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask API!'})

@app.route('/greet/<name>')
def greet(name):
    return jsonify({'greeting': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
