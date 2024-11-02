class TalkToTTTechnicalExpert {
    firstName string @description("First name of the expert")
    lastName string @description("Last name of the expert")
    personId int @description("Person ID of the expert")
    skills string[] @description("List of skills of the expert")
}

class TalkToTTAvailabilityRequest {
    experts TalkToTTTechnicalExpert[] @description("List of technical experts to check availability for")
    startDate string @description("Start date for the availability check")
    endDate string? @description("End date for the availability check")
    numberOfConsecutiveDays int @description("Number of consecutive days of availability as requested by the user")
}

class TalkToTTMaybeAvailabilityRequest {
    result TalkToTTAvailabilityRequest? @description("The availability request result if successful")
    error bool
    note string?
    detectedLanguage string @description("The detected language of the input")
}

function ExtractTalkToTTAvailabilityRequest(request: string, date: string) -> TalkToTTMaybeAvailabilityRequest {
 client LMS
  prompt #"
    Today's date is {{date}}.

    You are a helpful assistant that matches data from the user message and extracts structured data based on the schema.
    The user message contains availability-related questions for one or multiple experts or for one or multiple skills.
    If you cannot extract the start date, use today.
    Note: You do NOT get any availability dates in this request.

    This is the list of experts with CSV format:
    initials|person ID|full name|skills:
    CW|1|Christian Weyer|Generative AI, AI, KI, Software Architecture, .NET, Python
    CL|2|Christian Liebel|Angular, PWA, Web Components, W3C, Generative AI
    KD|3|Konstantin Denerz|Angular, UX, UI, Design Systems
    MF|4|Marco Frodl|Generative AI, AI, KI
    MM|5|Max Marschall|Angular, 3D, Generative AI, Python
    NIS|6|Niklas Schubert|Angular, Node.js
    PG|7|Pawel Gerr|.NET, ASP.NET, Entity Framework, Identity and Access Management
    SL|8|Sascha Lehmann|Angular, UX, UI, Design Systems
    SG|9|Sebastian Gingter|Generative AI, AI, KI, .NET, Python
    TH|10|Thomas Hilzendegen|Angular, .NET, Software Architecture
    YB|11|Yannick Baron|Angular, Reactive Development, ngxStore, git, Python
    DS|12|Daniel Sogl|Angular, Node.js, Mobile Apps
    FS|13|Felix Schütz|Angular, Node.js, Python

    Schema:
    {{ ctx.output_format }}

    {{ _.role("user") }}
    {{ request }}
  "#
}

test TalkToTT_SG_two_days {
    functions [ExtractTalkToTTAvailabilityRequest]
    args {
        request #"
             When does our colleague SG have two days available for a 2 days workshop?
        "#
    }
}

test TalkToTT_Angular_three_days {
    functions [ExtractTalkToTTAvailabilityRequest]
    args {
        request #"
             When does an expert with Angular skills have three days available for a workshop?
        "#
    }
}