class AvailabilityRequest {
    personIds int[] @description("List of person IDs to check availability for")
    startDate string @description("Start date for the availability check")
    endDate string? @description("Optional end date for the availability check")
    numberOfConsecutiveDays int @description("Final number of consecutive days requested")
}

class MaybeAvailabilityRequest {
    result AvailabilityRequest? @description("The availability request result if successful")
    error bool @description("Whether an error occurred")
    message string? @description("Error message if applicable")
}

function ExtractAvailabilityRequest(request: string) -> MaybeAvailabilityRequest {
  client "Ollama"
  prompt #"
    Today's date is 2024-11-01.
    You are a helpful assistant that extracts information from a given text.
    The text contains booking availability information for one or multiple people.
    If you cannot extract the start date, use today.
    This is the list of employees, with the initials, employee ID, full name, and skills:
    CW|1|Christian Weyer|Business Level Generative AI, Generative AI, AI, KI, Software Architecture, .NET, Python
    CL|2|Christian Liebel|Angular, PWA, Web Components, W3C, .NET, Gen AI, Web AI
    KD|3|Konstantin Denerz|UX, UI, Design Systems, Angular
    MF|4|Marco Frodl|Business Level Generative AI, Generative AI, AI, KI
    MM|5|Max Marschall|Angular, 3D, Gen AI, Python
    NIS|6|Niklas Schubert|Angular, Node.js
    PG|7|Pawel Gerr|.NET, ASP.NET, Entity Framework, Identity and Access Management
    SL|8|Sascha Lehmann|Angular, UX, UI, Design Systems
    SG|9|Sebastian Gingter|.NET, Generative AI, AI, KI, Python
    TH|10|Thomas Hilzendegen|Angular, .NET
    YB|11|Yannick Baron|Angular, Reactive Development, ngxStore, git, Python
    DS|12|Daniel Sogl|Angular, Node.js, Mobile Apps
    FS|13|Felix Schütz|Angular, Node.js, Python

    Extract all available fields from this content:
    {{ request }}

    {{ ctx.output_format }}
  "#
}

test SG_two_days {
  functions [ExtractAvailabilityRequest]
  args {
    request #"
      When does our colleague SG have two days available for a 2 days workshop?
    "#
  }
}