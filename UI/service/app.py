from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib
import sklearn
import pickle
import numpy as np
import sys


flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Fake News Detection", 
		  description = "Identify the truthfulness of the given news")

name_space = app.namespace('prediction', description='Prediction APIs')

model = app.model('Prediction params', 
				  {'NewsBody': fields.String(required = True, 
				  							   description="News Body", 
    					  				 	   help="News Body cannot be blank"),
				  })
'''
'textField2': fields.String(required = True, 
				  							   description="Text Field 2", 
    					  				 	   help="Text Field 2 cannot be blank"),
				  'select1': fields.Integer(required = True, 
				  							description="Select 1", 
    					  				 	help="Select 1 cannot be blank"),
				  'select2': fields.Integer(required = True, 
				  							description="Select 2", 
    					  				 	help="Select 2 cannot be blank"),
				  'select3': fields.Integer(required = True, 
				  							description="Select 3", 
    					  				 	help="Select 3 cannot be blank")
'''
logreg = joblib.load('lr1.joblib')

#load dic
inp = open("dict.pkl","rb")
bow = pickle.load(inp)

#Define BOW Function
def sentence2bow(sentence, bow):
    sentence_bow = [0 for i in range(len(bow))]
    words = sentence.split(' ')
    for word in words:
        if word in bow:
            sentence_bow[bow[word]] += 1
    return sentence_bow

@name_space.route("/")
class MainClass(Resource):

	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	@app.expect(model)		
	def post(self):
		try: 
			formData = request.json
			data = [val for val in formData.values()]
			res = sentence2bow(data[0],bow)
			prediction = logreg.predict(np.array(res).reshape(1,-1))
			#types = {0: "False", 1: "True"}
			response = jsonify({
				"statusCode": 200,
				"status": "Prediction made",
				"result": "Prediction: " + prediction[0]
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			return response
		except Exception as error:
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})