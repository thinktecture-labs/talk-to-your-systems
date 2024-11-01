from datetime import date
from baml_client.sync_client import b
from baml_client.types import TalkToTTMaybeAvailabilityRequest

def extract(query: str, date: str) -> TalkToTTMaybeAvailabilityRequest:
  response = b.ExtractTalkToTTAvailabilityRequest(query)
  return response

def extract_stream(query: str, date: str) -> TalkToTTMaybeAvailabilityRequest:
  stream = b.stream.ExtractTalkToTTAvailabilityRequest(query)
  for msg in stream:
    print(msg)
  
  final = stream.get_final_response()

  return final

extract("""
        When does an expert with Angular skills have two days available for a workshop?
        """,
        date.today().strftime("%Y-%m-%d"))
