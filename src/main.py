import os
from datetime import datetime
from dotenv import load_dotenv
from sanic import Sanic, response
from sanic.response import json
from motor import motor_asyncio

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)
SIGNING_SECRET = os.environ.get('SECRET_KEY')
app = Sanic(__name__)
client = motor_asyncio.AsyncIOMotorClient(os.environ.get("MONGODB_URI"))
db = client[os.environ.get("MONGODB_DATABASE")]
collection = db[os.environ.get("MONGODB_COLLECTION")]



@app.route('/pray', methods=['POST'])
async def pray(request):
  # response = request.form
  # command = response['command']
  # res_text = response['text']
  # if request.form['token'] != SIGNING_SECRET:
  #   return response.HTTPResponse(status=400)
  # prayer = {
  #   "user_id":request.form['user_id'],
  #   "when":datetime.utcnow(),
  #   "text":res_text
  # }
  # await prayer.commit()
  # await json.dumps(prayer)
  response_url = request.form.get('response_url')
  return json({
    "response_type":'in_channel',
    "text": "prayer added"},status=200, content_type="application/json"),
  


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)