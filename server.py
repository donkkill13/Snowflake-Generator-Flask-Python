from flask import Flask, jsonify
from snowflake import SnowflakeGenerator

app = Flask(__name__)

generator = SnowflakeGenerator(1, 1)

@app.route("/", methods=['GET'])
def index():
  load = {'snowflake': generator.generateID(), 'epoch_offset': generator.epoch_offset}
  return jsonify(load)

if __name__ == "__main__":
  context = ('certificate.crt', 'certificate.key')
  app.run(host='0.0.0.0', port=443, ssl_context=context)