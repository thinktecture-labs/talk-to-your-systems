from baml_client.sync_client import b
from baml_client.types import TalkToTTMaybeAvailabilityRequest

def extract(query: str) -> TalkToTTMaybeAvailabilityRequest:
  response = b.ExtractTalkToTTAvailabilityRequest(query)
  return response

def extract_stream(query: str) -> TalkToTTMaybeAvailabilityRequest:
  stream = b.stream.ExtractTalkToTTAvailabilityRequest(query)
  for msg in stream:
    print(msg)
  
  final = stream.get_final_response()

  return final

extract_stream("""
        When does our colleague SG have two days available for a 2 days workshop?
        """)
