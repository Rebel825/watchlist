from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to my watchlist!'

# @app.route('/<name>')
# def someone(name):
#     return u'Users Here!'

@app.route('/uesr/<name>')
def someonelse(name):
    return 'User: %s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('someonelse', name = 'Lw'))
    print(url_for('someonelse', name = 'somebody'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num = 2))
    return 'Test Page'