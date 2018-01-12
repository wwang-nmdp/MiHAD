from flask import Flask, render_template, Blueprint
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)
main = Blueprint('main', __name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/QA')
def qAndA():
    return render_template('QandA.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.register_blueprint(main)
    app.run(debug=True)