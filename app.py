
import time
import uuid
from dataclasses import dataclass
from flask import Flask, render_template, request
from faker import Faker

app = Flask(__name__)


@dataclass
class Dinger:
	dinger_id: str
	name: str
	address: str
	email: str

dingers = []

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data/')
def data():
	f = Faker()
	for x in range(1, 750):
		time.sleep(0.001)
		d = Dinger(dinger_id=str(uuid.uuid4()), 
				   name=f.name(), 
				   address=f.address(), 
				   email=f.email())
		dingers.append(d)
	return render_template("data.html", dingers=dingers)
