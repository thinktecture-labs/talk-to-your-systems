from datetime import date
from helpers import read_employees

today_date = date.today().strftime("%Y-%m-%d")
employees = read_employees()

extraction_system_message = (f"Today's date is {today_date}. Please consider this when processing the availability information.\n"
            "You are a helpful assistant that extracts information from a given text.\n"
            "The text contains questions or inquiries about booking availability information for one or multiple experts.\n"
            "It does not contain the availability information itself. You need to extract the data based on the schema below.\n"
            "Extract all the experts that fulfill the query.\n"
            "Double-check you really have found and extracted ALL the experts from the list below that match the query exactly - especially the skill.\n"
            "If you cannot extract the start date, use today. If no end date is specified, use null.\n"
            "This is the list of experts in JSON format, with the ID, initials, first name, last name, and skills:\n"
            f"{employees}\n"
            """This is an example result from the list when asking about Python as a skill:
            [
                {
                    "ID": 1,
                    "Initials": "CW",
                    "FirstName": "Christian",
                    "LastName": "Weyer",
                    "Skills": ["Generative AI", "AI", "KI", "Software Architecture", ".NET", "Python"]
                },
                {
                    "ID": 5,
                    "Initials": "MM",
                    "FirstName": "Max",
                    "LastName": "Marschall",
                    "Skills": ["Angular", "3D", "Generative AI", "Python"]
                },
                {
                    "ID": 9,
                    "Initials": "SG",
                    "FirstName": "Sebastian",
                    "LastName": "Gingter",
                    "Skills": ["Generative AI", "AI", "KI", ".NET", "Python"]
                },
                {
                    "ID": 11,
                    "Initials": "YB",
                    "FirstName": "Yannick",
                    "LastName": "Baron",
                    "Skills": ["Angular", "Reactive Development", "ngxStore", "git", "Python"]
                },
                {
                    "ID": 13,
                    "Initials": "FS",
                    "FirstName": "Felix",
                    "LastName": "Schütz",
                    "Skills": ["Angular", "Node.js", "Python"]
                }
            ]
            """)
