from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def API():
	d = {}

	d['query'] = str(request.args['query'])

	return jsonify(d)


if __name__ == '__main__':
    app.run()