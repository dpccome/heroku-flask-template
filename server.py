from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Flask APIs for Heroku',
    description='A base to build Flask APIs and run them on the Heroku Platform.',
)

pdfGenModel = api.model('PDFGen', {
    'template': fields.Integer,
    'filename': fields.String,
    'payload': fields.Raw
})

pdfMergeModel = api.model('PDFMerge', {
    'filename': fields.String,
    'payload': fields.Raw
})

class PDFGen:
    def generate(self, payload):
        result = payload
        return result
    
    def merge(self, payload):
        result = payload
        return result

@api.route('/pdfGen')
class generatePDF(Resource):
    @api.marshal_with(pdfGenModel)
    def post(self):
        return PDFGen.generate(api.payload), 201

@api.route('/pdfMerge')
class mergePDF(Resource):
    @api.marshal_with(pdfMergeModel)
    def post(self):
        return PDFGen.merge(api.payload), 201

if __name__ == '__main__':
    app.run(debug=True)