import os
from asyncio.events import get_event_loop
from asyncio.tasks import ensure_future
from datetime import datetime
from dotenv import load_dotenv
from sanic import Sanic, response
from sanic.response import dumps, json
from pymongo import MongoClient

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)
client = MongoClient(os.environ.get('MONGODB_URI'))
db = client.ccprayer
app = Sanic(__name__)


async def respond():
  return json({
    "response_type":'in_channel',
    "text": "Humans require ice cream"})

@app.route('/pray', methods=['POST'])
async def pray(request):
  if not res['token']:
    return response.HTTPResponse(status=400)
  prayer = db.prayer.insert_one({
    "user_id":request.form['user_id'],
    "when":datetime.utcnow(),
    "text": request.form['text']
  })
  
  

if __name__ == "__main__":
  asyncio.run()