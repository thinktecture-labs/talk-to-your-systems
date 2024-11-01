from baml_client.sync_client import b
from baml_client.types import MaybeAvailabilityRequest

def example(query: str) -> MaybeAvailabilityRequest:
  response = b.ExtractAvailabilityRequest(query)
  return response

def example_stream(query: str) -> MaybeAvailabilityRequest:
  stream = b.stream.ExtractAvailabilityRequest(query)
  for msg in stream:
    print(msg)
  
  final = stream.get_final_response()

  return final

example("""
        When does our colleague SG have two days available for a 2 days workshop?
        """)
