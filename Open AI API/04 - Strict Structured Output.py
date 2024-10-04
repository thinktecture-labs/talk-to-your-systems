from typing import List, Optional
from openai import OpenAI
from pydantic import BaseModel, Field
from rich.console import Console

from prompts import extraction_system_message


console = Console()

client = OpenAI()
MODEL = "gpt-4o-2024-08-06"

query = "When does our colleague SG have two days available for a 2 days workshop?"


# --------------------------------------------------------------
# Providing a JSON Schema
# --------------------------------------------------------------

def get_availability_request_json(query):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": extraction_system_message},
            {"role": "user", "content": query},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "availability_data",
                "schema": {
                    "type": "object",
                    "properties": {
                        "note": {
                            "type": "string",
                            "description": "Your reflection of the input.",
                        },
                        "employeeId":
                        {
                            "type": "integer",
                            "description": "Employee ID from the employee list."
                        },
                        "firstName": {
                            "type": "string",
                            "description": "First name of the employee from the employee list.",
                        },
                        "lastName": {
                            "type": "string",
                            "description": "Last name of the employee from the employee list.",
                        },
                        "numberOfConsecutiveDays": {
                            "type": "integer",
                            "description": "Number of requested days from the query."
                        },
                    },
                    "required": ["note", "employeeId", "firstName", "lastName", "numberOfConsecutiveDays"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        },
    )

    return response.choices[0].message

response = get_availability_request_json(query)
console.print(response.model_dump())


# --------------------------------------------------------------
# Using Pydantic
# --------------------------------------------------------------

class AvailabilityRequest(BaseModel):
    personIds: List[int] = Field(description="List of person IDs to check availability for")
    startDate: str = Field(description="Start date for the availability check")
    endDate: Optional[str] = Field(description="End date for the availability check")
    numberOfConsecutiveDays: int = Field(description="Number of consecutive days required")

def get_availability_request_pydantic(query: str):
    completion = client.beta.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": extraction_system_message},
            {"role": "user", "content": query},
        ],
        response_format=AvailabilityRequest,
    )

    return completion.choices[0].message.parsed

response_pydantic = get_availability_request_pydantic(query)
console.print(response_pydantic.model_dump())
