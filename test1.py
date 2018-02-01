import os, werkzeug, json
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('Picture',type=werkzeug.datastructures.FileStorage, location='files')

class UpPicture(Resource):
	def post(self):
		args=parser.parse_args()
		pic = args['Picture']
		pic.save("received_image/"+pic.filename)
		return {"code":"200", "desc":"success"}

api.add_resource(UpPicture,'/UploadPic')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5500)
