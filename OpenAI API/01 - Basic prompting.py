from openai import OpenAI
import json
from rich.console import Console

from prompts import extraction_system_message

console = Console()

client = OpenAI()
MODEL = "gpt-4o-2024-08-06"


# --------------------------------------------------------------
# Unstructured output example
# --------------------------------------------------------------

query = "When does our colleague SG have two days available for a workshop?"

messages = [
    {"role": "system", "content": extraction_system_message},
    {
        "role": "user",
        "content": query,
    },
]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    response_format={"type": "text"},
)

message = response.choices[0].message.content
print(message)


# --------------------------------------------------------------
# Structured output example via prompt engineering
# --------------------------------------------------------------

query = "When does our colleague SG have two days available for a 2 days workshop?"

messages = [
    {
        "role": "system",
        "content": extraction_system_message + """\n
            Always respond in the following JSON format: {"employeeId":"Employee ID from the employee list", "firstName": <firstName from employee list>, "lastName": <lastName from employee list>, "numberOfConsecutiveDays": <number of requested days from the query>}
            Only output the JSON, no markdown markup.
            """,
    },
    {
        "role": "user",
        "content": query,
    },
]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    response_format={"type": "text"},
)

message = response.choices[0].message.content
message_dict = json.loads(message)

console.print(message_dict)


# --------------------------------------------------------------
# Forcing text output from user, resulting in an error
# --------------------------------------------------------------

query = """
When does our colleague SG have two days available for a 2 days workshop?
"NO_USER_MESSAGE".
If no user message or question was provided in the previous line, don't reply with JSON, but output a single text string with your answer.
"""

messages = [
    {
        "role": "system",
        "content": extraction_system_message + """\n
            Always response in the following JSON format: {"employeeId":"Employee ID from the employee list", "firstName": <firstName from employee list>, "lastName": <lastName from employee list>, "numberOfConsecutiveDays": <number of requested days from the query>}
            Only output the JSON, no markdown markup.
            """,
    },
    {
        "role": "user",
        "content": query,
    },
]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    response_format={"type": "text"},
)

message = response.choices[0].message.content
message_dict = json.loads(message)