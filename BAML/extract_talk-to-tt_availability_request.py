from dotenv import load_dotenv


load_dotenv()

from datetime import date
from baml_client.sync_client import b
from baml_client.types import TalkToTTMaybeAvailabilityRequest
from helpers import read_employees

employees = read_employees()

def extract(query: str, date: str) -> TalkToTTMaybeAvailabilityRequest:
  response = b.ExtractTalkToTTAvailabilityRequest(query, date,  employees)
  return response

def extract_stream(query: str, date: str) -> TalkToTTMaybeAvailabilityRequest:
  stream = b.stream.ExtractTalkToTTAvailabilityRequest(query, date, employees)
  for msg in stream:
    print(msg)
  
  final = stream.get_final_response()

  return final

#query = "When does our colleague SG have two days available for a 2 days workshop?"
query = "When does an expert with Angular skills have two days available for a workshop?"

def eval():
  extract(query, date.today().strftime("%Y-%m-%d"))


import timeit

if __name__ == "__main__":
  print(timeit.timeit(eval, number=5))