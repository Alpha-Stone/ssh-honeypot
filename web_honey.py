# libraries
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, redirect, url_for, request

# logging format
log_format = logging.Formatter('%(asctime)s %(message)s')

# HTTP logger
http_logger = logging.getLogger("http Logger")
http_logger.setLevel(logging.INFO)
http_handler = RotatingFileHandler("Http_audits.log", maxBytes=2000, backupCount=5)
http_handler.setFormatter(log_format)
http_logger.addHandler(http_handler)


# baseline honey
def web_honey(input_username = 'username', input_password = 'password'):

    app = Flask(__name__)

    @app.route('/')

    def index():
        print("index funct")
        return render_template('as-login.html')

    @app.route('/login', methods=['POST'])

    def login():
        user = request.form['username']
        pswd = request.form["password"]
        
        ip_addr = request.remote_addr

        http_logger.info(f"Client ip: {ip_addr} entered \n Username: {user}, password: {pswd}")

        if user == 'username' and pswd == 'password':
            return "Success but Trapped !!!"
        else:
            return 'Failed but Trapped ### (invalid username and password)'
    
    return app

def run_web_honey(port=5000, input_username = 'username', input_password = 'password'):

    run_web_honey_app = web_honey(input_username, input_password)
    run_web_honey_app.run(debug=True, port=port, host="0.0.0.0")

    return run_web_honey_app


""" this executes itself when the file gets imported to other files 
    to not execute itself use {if __name__ == '__main__':} """
# run_web_honey(port=5000, input_username="username", input_password="password")
