import re

def email_sender():
    with open("email.txt", "r", encoding="utf-8") as f:
        content = f.read()
    sender_pattern = r"^From:\s*(.+)$"
    sender_match = re.search(sender_pattern, content, re.MULTILINE)
    if sender_match:
        return sender_match.group(1)
    else:
        return None


def email_recipient():
    with open("email.txt", "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"^To:\s*(.+)$", content)
    return match.group(1) if match else None


def email_subject():
    with open("email.txt", "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"^Subject:\s*(.+)$", content)
    return match.group(1) if match else None


def email_body():
    with open("email.txt", "r", encoding="utf-8") as f:
        content = f.read()

    # ciało maila zaczyna się po pustej linii
    match = re.search(r"^\n\n(.+)$", content, re.DOTALL)
    return match.group(1).strip() if match else None