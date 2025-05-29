from typing import List, Optional

from openai import OpenAI
from prompts import extraction_system_message
from pydantic import BaseModel, Field
from rich.console import Console

import instructor

console = Console()

api_url = "http://localhost:12434/engines/v1"
MODEL = "ai/qwen2.5:7B-Q4_K_M"

client = instructor.from_openai(
    OpenAI(base_url=api_url), 
    mode=instructor.Mode.TOOLS)

class TechnicalExpert(BaseModel):
    first_name: str = Field(description="First name of the expert")
    last_name: str = Field(description="Last name of the expert")
    person_id: int = Field(description="Person ID of the expert")
    skills: List[str] = Field(description="List of skills of the expert")

class AvailabilityRequest(BaseModel):
    experts: List[TechnicalExpert] = Field(description="List of technical experts to check availability for")
    start_date: str = Field(description="Start date for the availability check")
    end_date: Optional[str] = Field(description="Optional end date for the availability check, if specified in the request - otherwise null")
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
#query = "When does an expert with Angular skills have two days available for a workshop?"

response = client.chat.completions.create(
    model=MODEL,
    response_model=MaybeAvailabilityRequest,
    messages=[
        {
            "role": "system",
            "content": extraction_system_message + " /no_think"
        },
        {"role": "user", "content": query + " /no_think"}
    ],
)

console.print(response.model_dump_json(indent=3))
