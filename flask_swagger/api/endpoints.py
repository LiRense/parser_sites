# from flask import Flask
# from flask_restful import Api, Resource, reqparse,request
#
# ai_quotes = [
#     {
#         "id": 0,
#         "author": "Kevin Kelly",
#         "quote": "The business plans of the next 10,000 startups are easy to forecast: " +
#                  "Take X and add AI."
#     },
#     {
#         "id": 1,
#         "author": "Stephen Hawking",
#         "quote": "The development of full artificial intelligence could " +
#                  "spell the end of the human race… " +
#                  "It would take off on its own, and re-design " +
#                  "itself at an ever increasing rate. " +
#                  "Humans, who are limited by slow biological evolution, " +
#                  "couldn't compete, and would be superseded."
#     },
#     {
#         "id": 2,
#         "author": "Claude Shannon",
#         "quote": "I visualize a time when we will be to robots what " +
#                  "dogs are to humans, " +
#                  "and I’m rooting for the machines."
#     },
#     {
#         "id": 3,
#         "author": "Elon Musk",
#         "quote": "The pace of progress in artificial intelligence " +
#                  "(I’m not referring to narrow AI) " +
#                  "is incredibly fast. Unless you have direct " +
#                  "exposure to groups like Deepmind, " +
#                  "you have no idea how fast — it is growing " +
#                  "at a pace close to exponential. " +
#                  "The risk of something seriously dangerous " +
#                  "happening is in the five-year timeframe." +
#                  "10 years at most."
#     },
#     {
#         "id": 4,
#         "author": "Geoffrey Hinton",
#         "quote": "I have always been convinced that the only way " +
#                  "to get artificial intelligence to work " +
#                  "is to do the computation in a way similar to the human brain. " +
#                  "That is the goal I have been pursuing. We are making progress, " +
#                  "though we still have lots to learn about " +
#                  "how the brain actually works."
#     },
#     {
#         "id": 5,
#         "author": "Pedro Domingos",
#         "quote": "People worry that computers will " +
#                  "get too smart and take over the world, " +
#                  "but the real problem is that they're too stupid " +
#                  "and they've already taken over the world."
#     },
#     {
#         "id": 6,
#         "author": "Alan Turing",
#         "quote": "It seems probable that once the machine thinking " +
#                  "method had started, it would not take long " +
#                  "to outstrip our feeble powers… " +
#                  "They would be able to converse " +
#                  "with each other to sharpen their wits. " +
#                  "At some stage therefore, we should " +
#                  "have to expect the machines to take control."
#     },
#     {
#         "id": 7,
#         "author": "Ray Kurzweil",
#         "quote": "Artificial intelligence will reach " +
#                  "human levels by around 2029. " +
#                  "Follow that out further to, say, 2045, " +
#                  "we will have multiplied the intelligence, " +
#                  "the human biological machine intelligence " +
#                  "of our civilization a billion-fold."
#     },
#     {
#         "id": 8,
#         "author": "Sebastian Thrun",
#         "quote": "Nobody phrases it this way, but I think " +
#                  "that artificial intelligence " +
#                  "is almost a humanities discipline. It's really an attempt " +
#                  "to understand human intelligence and human cognition."
#     },
#     {
#         "id": 9,
#         "author": "Andrew Ng",
#         "quote": "We're making this analogy that AI is the new electricity." +
#                  "Electricity transformed industries: agriculture, " +
#                  "transportation, communication, manufacturing."
#     }
# ]
#
# app = Flask(__name__)
# api = Api(app)
#
# class Quote(Resource):
#     def get(self,id=0):
#         if id == 0:
#             return ai_quotes[0], 200
#         for quote in ai_quotes:
#             if quote["id"] == id:
#                 return quote,200
#         return 'Not found', 404
#
#     # @app.route('/add_data', methods=['POST'])
#     def post(self):
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             data = request.get_json()
#             end_id = ai_quotes[-1]["id"] + 1
#             print(data.get('author'))
#             quote = {
#                 "id": int(end_id),
#                 "author": data.get("author"),
#                 "quote": data.get("quote")
#             }
#             ai_quotes.append(quote)
#             return quote, 201
#         else:
#             return "Content type is not supported.",400
# @app.route('/change_data', methods=['PUT'])
# def put(id):
#     content_type = request.headers.get('Content-Type')
#     if (content_type == 'application/json'):
#         if id != None:
#             for idd, quote in enumerate(ai_quotes):
#                 if quote["id"] == id:
#                     data = request.get_json()
#                     ai_quotes[idd]["author"] = data.get("author")
#                     ai_quotes[idd]["quote"] = data.get("quote")
#                     return ai_quotes[idd], 200
#                 else:
#                     return "Not Found", 404
#         else:
#             return "Null value", 404
#     else:
#         return "Content type is not supported.", 400
#
#
# api.add_resource(Quote,"/ai-quotes", "/ai-quotes/")
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from flask_restful import Api, request
from flask_swagger_ui import get_swaggerui_blueprint
import quotes
from pathlib import Path
BASE_PATH = Path(__file__).resolve().parent

app = Flask(__name__)
api = Api(app)
# SWAGGER_URL = '/api'
# API_URL = '/static/swagger.yaml'
# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
#     API_URL,
#     config={  # Swagger UI config overrides
#         'app_name': "Test application"
#     },
#     # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
#     #    'clientId': "your-client-id",
#     #    'clientSecret': "your-client-secret-if-required",
#     #    'realm': "your-realms",
#     #    'appName': "your-app-name",
#     #    'scopeSeparator': " ",
#     #    'additionalQueryStringParams': {'test': "hello"}
#     # }
# )
#
# app.register_blueprint(swaggerui_blueprint,url_prefix=SWAGGER_URL)

# curl -X GET http://127.0.0.1:5000/get_data?id=5
@app.route('/api/get_data', methods=['GET'])
def get():
    ai_quotes = quotes.read_all()
    id = request.args.get('id')
    id = int(id)
    if id == 0:
        return ai_quotes[0], 200
    for quote in ai_quotes:
        if quote["id"] == id:
            return quote,200
    return 'Not found', 404

# curl -X POST "http://127.0.0.1:5000/change_data?id=5" -H "Content-Type: application/json" -d "{\"author\":\"salem\",\"quote\":\"WOW, im added new\"}"
@app.route('/api/add_data', methods=['POST'])
def post():
    ai_quotes = quotes.read_all()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        end_id = ai_quotes[-1]["id"] + 1
        print(data.get('author'))
        quote = {
            "id": int(end_id),
            "author": data.get("author"),
            "quote": data.get("quote")
        }
        ai_quotes.append(quote)
        return quote, 200
    else:
        return "Content type is not supported.",400

# curl -X PUT "http://127.0.0.1:5000/change_data?id=5" -H "Content-Type: application/json" -d "{\"author\":\"salem\",\"quote\":\"WOW, im added new\"}"
@app.route('/api/change_data', methods=['PUT'])
def put():
    ai_quotes = quotes.read_all()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        print(data)
        id = int(data.get('id'))
        print(id)
        if id != None:
            for idd,quote in enumerate(ai_quotes):
                print(idd, quote)
                if quote["id"] == id:
                    print(quote)
                    ai_quotes[idd]["author"] = data.get("author")
                    ai_quotes[idd]["quote"] = data.get("quote")
                    return f"CHANGED {ai_quotes[idd]}", 200

        else:
            return "Null value", 203
    else:
        return "Content type is not supported.", 400
    return "Not Found", 404

# curl -X DELETE http://127:5000/delete_data?id=5
@app.route('/api/delete_data',methods=["DELETE"])
def delete():
    ai_quotes = quotes.read_all()
    id = request.args.get('id')
    if id != None:
        id = int(id)
        for idd, quote in enumerate(ai_quotes):
            if quote["id"] == id:
                del ai_quotes[idd]
                return f"Deleted {quote}", 200
    elif id == None:
        return "Null value", 203
    else:
        return "Not found value", 404


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)