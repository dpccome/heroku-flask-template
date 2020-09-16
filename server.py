from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Flask APIs for Heroku',
    description='A base to build Flask APIs and run them on the Heroku Platform.',
)

PDFGENMODEL = api.model('PDFGen', {
    'template': fields.Integer,
    'filename': fields.String,
    'payload': fields.Raw
})

PDFMERGEMODEL = api.model('PDFMerge', {
    'filename': fields.String,
    'payload': fields.Raw
})

class PDFGen:
    def generate(self, payload):
        # Do Work for Generation from payload here
        result = payload
        return result
    
    def merge(self, payload):
        # Do work for merge with multiple documents and payload here
        result = payload
        return result


GENPDF = PDFGen()

@api.route('/pdfGen')
class generatePDF(Resource):
    @api.marshal_with(PDFGENMODEL)
    def post(self):
        return GENPDF.generate(api.payload), 201


@api.route('/pdfMerge')
class mergePDF(Resource):
    @api.marshal_with(PDFMERGEMODEL)
    def post(self):
        return GENPDF.merge(api.payload), 201


if __name__ == '__main__':
    app.run(debug=True)