from flask import Flask
from flask_restful import Api, Resource


app=Flask(__name__)
api = Api(app)


class Test(Resource):
	def __init__(self):
		pass

	def get(self):
		return {
		"status":"success"
		}


api.add_resource(Test, '/Test')


if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		port=5998,
		debug=True)
