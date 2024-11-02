from dotenv import load_dotenv

load_dotenv()

from datetime import date
from baml_client.sync_client import b
from baml_client.types import TalkToTTMaybeAvailabilityRequest

def extract(query: str, date: str) -> TalkToTTMaybeAvailabilityRequest:
  response = b.ExtractTalkToTTAvailabilityRequest(query, date)
  return response

def extract_stream(query: str, date: str) -> TalkToTTMaybeAvailabilityRequest:
  stream = b.stream.ExtractTalkToTTAvailabilityRequest(query, date)
  for msg in stream:
    print(msg)
  
  final = stream.get_final_response()

  return final

query = "When does our colleague SG have two days available for a 2 days workshop?"
#query = "When does an expert with Angular skills have two days available for a workshop?"

extract(query,
        date.today().strftime("%Y-%m-%d"))
