import os
import flask
from flask import Flask
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import reservation
from collections import defaultdict

MAIL_FROM = "sys@site.com"
MAIL_TO = "admin@site.com"
MAIL_SUBJECT = "Gracias por reservar con nosotros!"

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,template_folder="templates",static_folder="static")
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def index():
        return flask.render_template('main_page.html')

    @app.route('/Reservas')
    def res():
        return flask.render_template('reservas.html')
    @app.route("/Reservas",methods=["POST"])
    def book():
        resv_data = dict(flask.request.form)
        print(resv_data)
        reservation.add_reservation(resv_data['name'],resv_data['ciudad'],resv_data['Telefono'],resv_data['email'],0,0,resv_data['start_date'],resv_data['end_date'],resv_data['number'])

    return app
app = create_app()
if __name__ == '__main__':
    app.run(host = "0.0.0.0", threaded= True)