###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

file_map = {
    
    "availability.baml": "class AvailabilityRequest {\n    personIds int[] @description(\"List of person IDs to check availability for\")\n    startDate string @description(\"Start date for the availability check\")\n    endDate string? @description(\"Optional end date for the availability check\")\n    numberOfConsecutiveDays int @description(\"Final number of consecutive days requested\")\n}\n\nclass MaybeAvailabilityRequest {\n    result AvailabilityRequest? @description(\"The availability request result if successful\")\n    error bool @description(\"Whether an error occurred\")\n    message string? @description(\"Error message if applicable\")\n}\n\nfunction ExtractAvailabilityRequest(request: string) -> MaybeAvailabilityRequest {\n  client \"Ollama\"\n  prompt #\"\n    Today's date is 2024-11-01.\n    You are a helpful assistant that extracts information from a given text.\n    The text contains booking availability information for one or multiple people.\n    If you cannot extract the start date, use today.\n    This is the list of employees, with the initials, employee ID, full name, and skills:\n    CW|1|Christian Weyer|Business Level Generative AI, Generative AI, AI, KI, Software Architecture, .NET, Python\n    CL|2|Christian Liebel|Angular, PWA, Web Components, W3C, .NET, Gen AI, Web AI\n    KD|3|Konstantin Denerz|UX, UI, Design Systems, Angular\n    MF|4|Marco Frodl|Business Level Generative AI, Generative AI, AI, KI\n    MM|5|Max Marschall|Angular, 3D, Gen AI, Python\n    NIS|6|Niklas Schubert|Angular, Node.js\n    PG|7|Pawel Gerr|.NET, ASP.NET, Entity Framework, Identity and Access Management\n    SL|8|Sascha Lehmann|Angular, UX, UI, Design Systems\n    SG|9|Sebastian Gingter|.NET, Generative AI, AI, KI, Python\n    TH|10|Thomas Hilzendegen|Angular, .NET\n    YB|11|Yannick Baron|Angular, Reactive Development, ngxStore, git, Python\n    DS|12|Daniel Sogl|Angular, Node.js, Mobile Apps\n    FS|13|Felix Schütz|Angular, Node.js, Python\n\n    Extract all available fields from this content:\n    {{ request }}\n\n    {{ ctx.output_format }}\n  \"#\n}\n\ntest SG_two_days {\n  functions [ExtractAvailabilityRequest]\n  args {\n    request #\"\n      When does our colleague SG have two days available for a 2 days workshop?\n    \"#\n  }\n}",
    "clients.baml": "// Learn more about clients at https://docs.boundaryml.com/docs/snippets/clients/overview\n\nclient<llm> CustomGPT4o {\n  provider openai\n  options {\n    model \"gpt-4o-2024-08-06\"\n    api_key env.OPENAI_API_KEY\n  }\n}\n\nclient<llm> CustomGPT4oMini {\n  provider openai\n  retry_policy Exponential\n  options {\n    model \"gpt-4o-mini\"\n    api_key env.OPENAI_API_KEY\n  }\n}\n\nclient<llm> Ollama {\n  provider \"openai-generic\"\n  options {\n    base_url \"http://localhost:11434/v1\"\n    model qwen2.5:3b-instruct-q4_K_M\n    temperature 0.0\n  }\n}\n\nclient<llm> LMS {\n  provider \"openai-generic\"\n  options {\n    base_url \"http://localhost:1234/v1\"\n    model smollm2-1.7b-instruct\n    temperature 0.0\n  }\n}\n\nclient<llm> CustomSonnet {\n  provider anthropic\n  options {\n    model \"claude-3-5-sonnet-20241022\"\n    api_key env.ANTHROPIC_API_KEY\n  }\n}\n\n// https://docs.boundaryml.com/docs/snippets/clients/round-robin\nclient<llm> CustomFast {\n  provider round-robin\n  options {\n    // This will alternate between the two clients\n    strategy [CustomGPT4oMini, CustomHaiku]\n  }\n}\n\n// https://docs.boundaryml.com/docs/snippets/clients/fallback\nclient<llm> OpenaiFallback {\n  provider fallback\n  options {\n    // This will try the clients in order until one succeeds\n    strategy [CustomGPT4oMini, CustomGPT4oMini]\n  }\n}\n\n// https://docs.boundaryml.com/docs/snippets/clients/retry\nretry_policy Constant {\n  max_retries 3\n  // Strategy is optional\n  strategy {\n    type constant_delay\n    delay_ms 200\n  }\n}\n\nretry_policy Exponential {\n  max_retries 2\n  // Strategy is optional\n  strategy {\n    type exponential_backoff\n    delay_ms 300\n    mutliplier 1.5\n    max_delay_ms 10000\n  }\n}",
    "generators.baml": "// This helps use auto generate libraries you can use in the language of\n// your choice. You can have multiple generators if you use multiple languages.\n// Just ensure that the output_dir is different for each generator.\ngenerator target {\n    // Valid values: \"python/pydantic\", \"typescript\", \"ruby/sorbet\", \"rest/openapi\"\n    output_type \"python/pydantic\"\n\n    // Where the generated code will be saved (relative to baml_src/)\n    output_dir \"../\"\n\n    // The version of the BAML package you have installed (e.g. same version as your baml-py or @boundaryml/baml).\n    // The BAML VSCode extension version should also match this version.\n    version \"0.65.0\"\n\n    // Valid values: \"sync\", \"async\"\n    // This controls what `b.FunctionName()` will be (sync or async).\n    default_client_mode sync\n}\n",
    "talktott_availability.baml": "class TalkToTTTechnicalExpert {\n    firstName string @description(\"First name of the expert\")\n    lastName string @description(\"Last name of the expert\")\n    personId int @description(\"Person ID of the expert\")\n    skills string[] @description(\"List of skills of the expert\")\n}\n\nclass TalkToTTAvailabilityRequest {\n    experts TalkToTTTechnicalExpert[] @description(\"List of technical experts to check availability for\")\n    startDate string @description(\"Start date for the availability check\")\n    endDate string? @description(\"End date for the availability check\")\n    numberOfConsecutiveDays int @description(\"Number of consecutive days of availability as requested by the user\")\n}\n\nclass TalkToTTMaybeAvailabilityRequest {\n    result TalkToTTAvailabilityRequest? @description(\"The availability request result if successful\")\n    error bool\n    note string?\n    detectedLanguage string @description(\"The detected language of the input\")\n}\n\nfunction ExtractTalkToTTAvailabilityRequest(request: string) -> TalkToTTMaybeAvailabilityRequest {\n client CustomGPT4o\n  prompt #\"\n    Today's date is 2024-11-01.\n\n    You are a helpful assistant that matches data from the user message and extracts structured data based on the schema.\n    The user message contains availability-related questions for one or multiple experts or for one or multiple skills.\n    If you cannot extract the start date, use today.\n    Note: You do NOT get any availability dates in this request.\n\n    This is the list of experts with CSV format:\n    initials|person ID|full name|skills:\n    CW|1|Christian Weyer|Generative AI, AI, KI, Software Architecture, .NET, Python\n    CL|2|Christian Liebel|Angular, PWA, Web Components, W3C, Generative AI\n    KD|3|Konstantin Denerz|Angular, UX, UI, Design Systems\n    MF|4|Marco Frodl|Generative AI, AI, KI\n    MM|5|Max Marschall|Angular, 3D, Generative AI, Python\n    NIS|6|Niklas Schubert|Angular, Node.js\n    PG|7|Pawel Gerr|.NET, ASP.NET, Entity Framework, Identity and Access Management\n    SL|8|Sascha Lehmann|Angular, UX, UI, Design Systems\n    SG|9|Sebastian Gingter|Generative AI, AI, KI, .NET, Python\n    TH|10|Thomas Hilzendegen|Angular, .NET, Software Architecture\n    YB|11|Yannick Baron|Angular, Reactive Development, ngxStore, git, Python\n    DS|12|Daniel Sogl|Angular, Node.js, Mobile Apps\n    FS|13|Felix Schütz|Angular, Node.js, Python\n\n    Schema:\n    {{ ctx.output_format }}\n\n    {{ _.role(\"user\") }}\n    {{ request }}\n  \"#\n}\n\ntest TalkToTT_SG_two_days {\n    functions [ExtractTalkToTTAvailabilityRequest]\n    args {\n        request #\"\n             When does our colleague SG have two days available for a 2 days workshop?\n        \"#\n    }\n}\n\ntest TalkToTT_Angular_three_days {\n    functions [ExtractTalkToTTAvailabilityRequest]\n    args {\n        request #\"\n             When does an expert with Angular skills have three days available for a workshop?\n        \"#\n    }\n}",
}

def get_baml_files():
    return file_map