# All imports
from pymongo import MongoClient
from flask import Flask, jsonify, render_template


# configuration
MONGODB_DATABASE_NAME = 'zipcode'
client = MongoClient()

# little app
app = Flask(__name__)
app.config.from_object(__name__)

db = client.zipcode


@app.route('/')
def index_view():
  cities = list(
    db.cities.find().sort('pop', -1).limit(20)
  )
  return render_template('index.html', cities=cities)


@app.route('/get-cities', methods=['GET'])
def rating_of_cities():
  query = list(
    db.cities.find().sort('pop', -1).limit(20)
  )
  return jsonify({'cities': query})


if __name__ == '__main__':
  app.run()
