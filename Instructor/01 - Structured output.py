from typing import List, Optional
from openai import OpenAI
from pydantic import BaseModel, Field
from rich.console import Console
import instructor

from prompts import extraction_system_message


console = Console()

client = instructor.from_openai(OpenAI())
MODEL = "gpt-4o-2024-08-06"


# --------------------------------------------------------------
# Instructor structured output example
# --------------------------------------------------------------

class AvailabilityRequest(BaseModel):
    personIds: List[int] = Field(description="List of person IDs to check availability for")
    startDate: str = Field(description="Start date for the availability check")
    endDate: Optional[str] = Field(description="End date for the availability check")
    numberOfConsecutiveDays: int = Field(description="Number of consecutive days required")


query = "When does our colleague SG have two days available for a 2 days workshop?"

response = client.chat.completions.create(
    model=MODEL,
    response_model=AvailabilityRequest,
    messages=[
        {
            "role": "system",
            "content": extraction_system_message
        },
        {"role": "user", "content": query},
    ],
)

console.print(response.model_dump_json(indent=3))



# --------------------------------------------------------------
# Streaming structured output example
# --------------------------------------------------------------
'''
response_stream = client.chat.completions.create_partial(
    model=MODEL,
    response_model=AvailabilityRequest,
    messages=[
        {
            "role": "system",
            "content": extraction_system_message
        },
        {"role": "user", "content": query},
    ],
)

for user in response_stream:
    console.print(user)
'''