import json
from typing import List, Optional

from openai import OpenAI
from prompts import extraction_system_message
from pydantic import BaseModel, Field

import instructor

# --------------------------------------------------------------
# Instructor with Maybe pattern
# --------------------------------------------------------------

api_url = "https://api.openai.com/v1/" #"http://localhost:11434/v1"
MODEL = "gpt-4o-2024-08-06" #"qwen2.5:7b-instruct-fp16"

client = instructor.from_openai(OpenAI(base_url=api_url)) #, mode=instructor.Mode.JSON)


class AvailabilityRequest(BaseModel):
    personIds: List[int] = Field(description="List of person IDs to check availability for")
    startDate: str = Field(description="Start date for the availability check")
    endDate: Optional[str] = Field(description="End date for the availability check")
    numberOfConsecutiveDays: int = Field(description="Number of consecutive days required")

class MaybeAvailabilityRequest(BaseModel):
    result: Optional[AvailabilityRequest] = Field(default=None)
    error: bool = Field(default=False)
    message: Optional[str] = Field(default=None)

    def __bool__(self):
        return self.result is not None


query = "When does our colleague CW have two days available for a 2 days workshop?"
#query = "F U!"

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
