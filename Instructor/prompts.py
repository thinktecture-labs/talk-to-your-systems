from datetime import date
from helpers import read_employees

today_date = date.today().strftime("%Y-%m-%d")
employees = read_employees()

extraction_system_message = (f"Today's date is {today_date}. Please consider this when processing the availability information.\n"
            "You are a helpful assistant that extracts information from a given text.\n"
            "The text contains questions or inquiries about booking availability information for one or multiple experts.\n"
            "It does not contain the availability information itself. You need to extract the data based on the schema below.\n"
            "Extract all the experts that exactly fulfill the query.\n"
            "If you cannot extract the start date, use today. If no end date is specified, use null.\n"
            "Double-check you really have exactly ALL the experts from the list below that match the query.\n"
            "This is the list of experts, with the employee ID, initials, first name, last name,and skills:\n"
            f"{employees}\n")
