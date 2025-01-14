import os
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# import blueprints
from _code.blueprints.banking_system import bankingsystem
from _code.blueprints.shipping_system import shippingsystem
from _code.blueprints.currency_exchange import currencyexchange
from _code.blueprints.university_enrollment import universityenrollment

# register blueprints
app.register_blueprint(bankingsystem)
app.register_blueprint(shippingsystem)
app.register_blueprint(currencyexchange)
app.register_blueprint(universityenrollment)


@app.route('/')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()