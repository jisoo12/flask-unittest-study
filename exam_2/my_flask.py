from flask import Flask
from flask_restful import reqparse, Resource, Api


parser = reqparse.RequestParser()
parser.add_argument('id')

class HealthCheck(Resource):
  def post(self):
    args = parser.parse_args()
    if args == None or args.get("id", None) == None:
      return {"status": "error"}
    else:
      return {"status": "ok"}
  def get(self):
    return {"status": "error"}


app = Flask(__name__)
api = Api(app)

api.add_resource(HealthCheck, '/')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)