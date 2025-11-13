#!/usr/bin/python3
"""
Test file for error handling
"""
from task_00_intro import generate_invitations

print("=== Test 1: Template is not a string ===")
generate_invitations(123, [{"name": "Alice"}])

print("\n=== Test 2: Attendees is not a list ===")
generate_invitations("Hello {name}", "not a list")

print("\n=== Test 3: Empty template ===")
generate_invitations("", [{"name": "Alice"}])

print("\n=== Test 4: Empty attendees list ===")
generate_invitations("Hello {name}", [])

print("\n=== Test 5: Attendees is not a list of dictionaries ===")
generate_invitations("Hello {name}", ["Alice", "Bob"])

print("\n=== Test 6: Valid input with missing data ===")
attendees = [
    {"name": "Alice", "event_title": "Conference"},
    {"event_title": "Workshop", "event_date": "2023-08-20"},
]
with open('template.txt', 'r') as file:
    template_content = file.read()
generate_invitations(template_content, attendees)
