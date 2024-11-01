from baml_client.sync_client import b
from baml_client.types import Resume

def example(raw_resume: str) -> Resume:
  response = b.ExtractResume(raw_resume)
  return response

def example_stream(raw_resume: str) -> Resume:
  stream = b.stream.ExtractResume(raw_resume)
  for msg in stream:
    print(msg)
  
  final = stream.get_final_response()

  return final

example("""
    Jason Doe
    Python, Rust
    Exp.: University of California, Berkeley, B.S. in Computer Science, 2020
    Also an expert in Tableau, SQL, and C++
    """)
