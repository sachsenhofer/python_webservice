from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><head></head><body>SUCCESS: This Flask application is dockerized.</body></html>'

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
