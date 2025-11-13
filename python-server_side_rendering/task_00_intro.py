#!/usr/bin/python3
"""
Module for generating personalized invitation files from a template.
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendees list.
    """
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees is not a list")
        return

    if not template or template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees is not a list of dictionaries")
            return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        name = attendee.get("name")
        if name is None or name == "":
            name = "N/A"

        event_title = attendee.get("event_title")
        if event_title is None or event_title == "":
            event_title = "N/A"
        
        event_date = attendee.get("event_date")
        if event_date is None or event_date == "":
            event_date = "N/A"

        event_location = attendee.get("event_location")
        if event_location is None or event_location == "":
            event_location = "N/A"

        invitation = invitation.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace("{event_location}", str(event_location))

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
