from flask import Flask, render_template, Blueprint
from flask_bootstrap import Bootstrap
import DatabaseUtil as databaseUtil

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


@main.route('/pre_miha')
def pre_miha():
    conn = databaseUtil.create_connection("PredictedMiHA.db")
    rows = databaseUtil.get_miha_rows(conn, 50, 1)
    return render_template('databaseViewer.html', data=rows)


@main.route('/known_miha')
def known_miha():
    conn = databaseUtil.create_connection("PredictedMiHA.db")
    rows = databaseUtil.get_known_miha(conn, 50, 1)
    return render_template('knownMiHA.html', data=rows)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.register_blueprint(main)
    app.run(debug=True)