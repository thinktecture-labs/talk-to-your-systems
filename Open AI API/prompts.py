from datetime import date
from helpers import read_employees

today_date = date.today().strftime("%Y-%m-%d")
employees = read_employees()

extraction_system_message = (f"Today's date is {today_date}. Please consider this when processing the availability information.\n"
            "You are a helpful assistant that extracts information from a given text. The text contains booking availability information for one or multiple people.\n"
            "If you cannot extract the start date, use today.\n"
            "This is the list of employees, with the initials, employee ID, full name, and skills:\n"
            f"{employees}\n\n"
            "There has to be at least one personID - otherwise this is an error."
            "DO NOT invent data. DO NOT hallucinate!")
