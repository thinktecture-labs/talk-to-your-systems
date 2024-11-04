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

function ExtractTalkToTTAvailabilityRequest(request: string, date: string, people: string) -> TalkToTTMaybeAvailabilityRequest {
 client GPT4o
  prompt #"
    Today's date is {{ date }}. Please consider this when processing the availability information.
    You are a helpful assistant that extracts information from a given text. The text contains booking availability information for one or multiple people.
    If you cannot extract the start date, use today.
    This is the list of employees, with the initials, employee ID, full name, and skills:
    {{ people }}
    
    DO NOT invent data. DO NOT hallucinate!
    {{ ctx.output_format }}

    NO QUOTES AROUND KEYS!

    {{ _.role("user") }}
    {{ request }}
  "#
}

test TalkToTT_SG_two_days {
    functions [ExtractTalkToTTAvailabilityRequest]
    args {
        request #"When does our colleague SG have two days available for a 2 days workshop?"#
        date #"2022-10-01"#
    }
}

test TalkToTT_Angular_three_days {
    functions [ExtractTalkToTTAvailabilityRequest]
    args {
        request #"When does an expert with Angular skills have three days available for a workshop?"#
        date #"2022-10-01"#
    }
}