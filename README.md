# Talk-to-your-Systems - with LLMs and SLMs

This repository contains code examples and demonstrations for the talk "Talk to your systems" presented at various conferences. It showcases different approaches to working with Large Language Models (LLMs) and Structured Language Models (SLMs), focusing on OpenAI's GPT models and the Instructor library.

## Project Structure

```
.
├── LICENSE
├── README.md
├── requirements.txt
├── Instructor/
│   ├── 01 - Structured output.py
│   ├── 02 - Maybe pattern.py
│   ├── 03 - Local LLM.py
│   ├── employees.txt
│   ├── helpers.py
│   └── prompts.py
└── Open AI API/
    ├── 01 - Basic prompting.py
    ├── 02 - JSON Mode.py
    ├── 03 - Function Calling.py
    ├── 04 - Strict Structured Output.py
    ├── employees.txt
    ├── helpers.py
    └── prompts.py
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/talk-to-your-systems.git
   cd talk-to-your-systems
   ```

2. Set up a virtual environment (recommended):
   
   It's recommended to use a virtual environment to keep the project dependencies isolated. You can use either venv (built into Python) or conda.

   Using venv:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Using conda:
   ```
   conda create --name talk-to-your-systems python=3.11
   conda activate talk-to-your-systems
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Dependencies

The project relies on the following Python libraries:
- openai
- requests
- instructor
- langfuse (optional)
- rich

These dependencies are listed in the `requirements.txt` file.

## Usage

The project is divided into two main sections:

### 1. Open AI API

This section demonstrates various techniques for working directly with the OpenAI API:

- `01 - Basic prompting.py`: Illustrates basic prompting techniques and structured output via prompt engineering.
- `02 - JSON Mode.py`: Demonstrates how to use OpenAI's JSON mode for structured outputs.
- `03 - Function Calling.py`: Shows how to use OpenAI's function calling feature.
- `04 - Strict Structured Output.py`: Explores techniques for enforcing strict structured outputs.

To run any of these scripts:

```
python "Open AI API/01 - Basic prompting.py"
```

### 2. Instructor

This section showcases the use of the Instructor library, which provides additional tools for working with LLMs:

- `01 - Structured output.py`: Demonstrates structured output using Instructor.
- `02 - Maybe pattern.py`: Illustrates the Maybe pattern for handling uncertain outputs.
- `03 - Local LLM.py`: Shows how to use Instructor with local language models.

To run any of these scripts:

```
python "Instructor/01 - Structured output.py"
```

## Additional Files

- `employees.txt`: Contains sample employee data used in the demonstrations.
- `helpers.py`: Includes helper functions used across multiple scripts.
- `prompts.py`: Stores prompt templates used in the examples.

## License

This project is licensed under the terms of the LICENSE file included in the repository.

## Contributing

Contributions to this project are welcome. Please feel free to submit a Pull Request.

## Disclaimer

This project is for educational purposes only. Ensure you comply with OpenAI's use-case policy when using their API.
