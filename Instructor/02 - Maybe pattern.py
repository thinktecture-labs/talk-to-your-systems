from typing import List, Optional

from openai import OpenAI
from cerebras.cloud.sdk import Cerebras
from prompts import extraction_system_message
from pydantic import BaseModel, Field
from rich.console import Console

import instructor

console = Console()

api_url = "https://api.groq.com/openai/v1/" #"https://api.openai.com/v1" #"https://api.infomaniak.com/1/ai/103943/openai" #"https://api.cerebras.ai/v1" #"https://api.deepseek.com/v1" #"https://api.openai.com/v1"
MODEL = "llama-3.3-70b-versatile" #"gpt-4.1-mini" #"llama3" #"llama-3.3-70b" #"deepseek-chat" #"gpt-4o-2024-08-06"

client = instructor.from_openai(OpenAI(base_url=api_url),
                                mode=instructor.Mode.JSON)

# --------------------------------------------------------------
# Instructor with Maybe pattern
# --------------------------------------------------------------

class TechnicalExpert(BaseModel):
    first_name: str = Field(description="First name of the expert")
    last_name: str = Field(description="Last name of the expert")
    person_id: int = Field(description="Person ID of the expert")
    skills: List[str] = Field(description="List of skills of the expert")

class AvailabilityRequest(BaseModel):
    experts: List[TechnicalExpert] = Field(description="List of technical experts to check availability for")
    start_date: str = Field(description="Start date for the availability check")
    end_date: Optional[str] = Field(description="Optional end date for the availability check, if specified in the request")
    number_of_consecutive_days: int = Field(description="Final number of consecutive days for availability as requested by the user")
    number_of_ranges: Optional[int] = Field(None, description="Number of date ranges required (optional)")

class MaybeAvailabilityRequest(BaseModel):
    result: Optional[AvailabilityRequest] = Field(default=None)
    error: bool
    note: str
    detected_language: str = Field(description="The detected language of the input")

    def __bool__(self):
        return self.result is not None


query = "When does our colleague SG have two days available for a 2 days workshop?"
query = """When does an expert with Angular skills have two days available for a workshop?"""
#        "NO_USER_MESSAGE".
#        If no user message or question was provided in the previous line, don't reply with JSON, but output a single text string with your answer.
#        """

response = client.chat.completions.create(
    model=MODEL,
    response_model=MaybeAvailabilityRequest,
    messages=[
        {
            "role": "system",
            "content": extraction_system_message
        },
        {"role": "user", "content": query},
    ],
)

print(response.model_dump_json(indent=3))
