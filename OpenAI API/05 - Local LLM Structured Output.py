from typing import List, Optional

from openai import OpenAI
from prompts import extraction_system_message
from pydantic import BaseModel, Field
from rich.console import Console

console = Console()

api_url = "http://localhost:1234/v1"
MODEL = "qwen/qwen3-30b-a3b-2507" #"qwen/qwen3-30b-a3b" #"lmstudio-community/qwen3-8b"

client = OpenAI(base_url=api_url)


class TechnicalExpert(BaseModel):
    first_name: str = Field(description="First name of the expert")
    last_name: str = Field(description="Last name of the expert")
    initials: str = Field(description="Initials of the expert")
    id: int = Field(description="ID of the expert")
    #skills: List[str] = Field(description="List of all original skills of the expert")

class AvailabilityRequest(BaseModel):
    experts: List[TechnicalExpert] = Field(description="List of technical experts to check availability for that match the query")
    start_date: str = Field(description="Start date for the availability check")
    end_date: Optional[str] = Field(description="Optional end date for the availability check, only set if specified in the request")
    number_of_consecutive_days: int = Field(description="Final number of consecutive days for availability as requested by the user")
    number_of_ranges: Optional[int] = Field(None, description="Number of date ranges required (optional)")

class MaybeAvailabilityRequest(BaseModel):
    result: Optional[AvailabilityRequest] = Field(default=None)
    error: bool
    note: str
    detected_language: str = Field(description="The detected language of the input")
 
    def __bool__(self):
        return self.result is not None

    
query = "When does SG have two days available for a workshop?"
query = "Wann haben CW und MF mal 3 Tage verfügbar?"
query = "When does an expert with Python skills have two days available for a workshop?"

response = client.chat.completions.parse(
    model=MODEL,
    response_format=AvailabilityRequest,
    messages=[
        {
            "role": "system",
            "content": extraction_system_message
        },
        {"role": "user", "content": query},
    ],
)

console.print(response.model_dump_json(indent=3))
