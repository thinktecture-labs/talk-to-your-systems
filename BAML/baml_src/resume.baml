class Resume {
  name string @description("full name")
  email string?
  experience string[]
  skills string[]
}

function ExtractResume(resume: string) -> Resume {
  client "LMSLlama32" //"OllamaQwen25"
  prompt #"
    DO NOT invent any data that is not in the request!

    Extract all available fields from this content:
    {{ resume }}

    {{ ctx.output_format }}

    DO NOT hallucinate!!!
  "#
}

test vaibhav_resume {
  functions [ExtractResume]
  args {
    resume #"
      Vaibhav Gupta
      vbv@boundaryml.com

      Experience:
      - Founder at BoundaryML
      - CV Engineer at Google
      - CV Engineer at Microsoft

      Skills:
      - Rust
      - C++
    "#
  }
}
