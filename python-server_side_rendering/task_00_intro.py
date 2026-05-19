#!/usr/bin/python3
"""
Simple templating program.
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template.
    """

    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Invalid input: attendees must be a list of dictionaries.")
            return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        invitation = template.replace("{name}", name)
        invitation = invitation.replace("{event_title}", event_title)
        invitation = invitation.replace("{event_date}", event_date)
        invitation = invitation.replace("{event_location}", event_location)

        filename = "output_{}.txt".format(index)

        with open(filename, "w") as file:
            file.write(invitation)