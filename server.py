from flask import Flask, Response
from snowflake import SnowflakeGenerator
import json
app = Flask(__name__)

generator = SnowflakeGenerator(1, 1)

@app.route("/", methods=['GET'])
def index():
	resp = Response(json.dumps({'snowflake': generator.generateID(), 'epoch_offset': generator.epoch_offset}))
	resp.headers['Content-Type'] = 'application/json'
	return resp

if __name__ == "__main__":
	context = ('certificate.crt', 'certificate.key')
	app.run(host='0.0.0.0', port=443, ssl_context=context)
