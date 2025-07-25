info = {
    "Name": "Nasar Ali",
    "Role": "Student",
    "Organization": "Skillbridge.pk",
    "Background": "BSCS",
}

md_output = f"""# About Me

| Field        | Details                      |
|--------------|-----------------------------|
| **Name**     | {info['Name']}              |
| **Role**     | {info['Role']}              |
| **Org**      | {info['Organization']}      |
| **Background** | {info['Background']}      |
"""

print(md_output)