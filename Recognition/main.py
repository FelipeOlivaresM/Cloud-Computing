from flask import Flask
from flask_restful import Resource,Api, reqparse
import Main
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)
api = Api(app)

class Parking(Resource):

    
    parser = reqparse.RequestParser()
    parser.add_argument('imagencod', type=str, required=True, help="Image codificated is required")
    def post(self):
        
        data = Parking.parser.parse_args()
        codimg = data.imagencod    
        print("Imagen en Bytes \n")
        print(codimg)
        img = Main.main(codimg)
        
        return {
            'status': True,
            'answer': img
        }

api.add_resource(Parking, '/inf')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)