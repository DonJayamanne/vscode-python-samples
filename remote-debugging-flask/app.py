import ptvsd
address = ('0.0.0.0', 3000)
ptvsd.enable_attach('my_secret', address)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
