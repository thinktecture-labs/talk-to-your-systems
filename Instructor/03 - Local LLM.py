from typing import List, Optional
import time

from openai import OpenAI
from prompts import extraction_system_message
from pydantic import BaseModel, Field
from rich.console import Console

import instructor

console = Console()

api_url = "http://localhost:1234/v1" #"http://localhost:8000/v1" #"http://localhost:11434/v1" #"http://localhost:12434/engines/v1"
MODEL = "qwen/qwen3-4b-2507" #"Qwen3-30B-A3B-Instruct-2507-MLX-4bit" #"Qwen3-30B-A3B-Instruct-2507-UD-Q8_K_XL" #"Qwen3-30B-A3B-Instruct-2507-Q4_K_S" #"qwen3:30b-a3b-instruct-2507-q4_K_M" #"gpt-oss:20b" #"ai/qwen2.5:7B-Q4_K_M"

client = instructor.from_openai(
    OpenAI(base_url=api_url), 
    mode=instructor.Mode.TOOLS)

class TechnicalExpert(BaseModel):
    first_name: str = Field(description="First name of the expert")
    last_name: str = Field(description="Last name of the expert")
    person_id: int = Field(description="Person ID of the expert")
    #skills: List[str] = Field(description="List of skills of the expert")

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


query = "When does SG have two days available for a workshop?"
query = "Wann sind CW und MF mal 3 Tage verfügbar?"
query = "When does an expert with Generative AI skills have 4 days available?"

print(query)

start_time = time.perf_counter()

response = client.chat.completions.create(
    model=MODEL,
    response_model=MaybeAvailabilityRequest,
    messages=[
        {
            "role": "system",
            "content": extraction_system_message
        },
        {"role": "user", "content": query}
    ],
)

end_time = time.perf_counter()
duration_ms = (end_time - start_time) * 1000

console.print(response)

if response.result:
    console.print(f"Number of experts: {len(response.result.experts)}")

console.print(f"[bold green]API call duration: {duration_ms:.2f} ms[/bold green]")
