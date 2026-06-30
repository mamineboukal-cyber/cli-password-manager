import re

def validate_email(email):
    pattern = r'\w+@gmail\.com'
    if re.match(pattern, email):
        return True
    else:
        return False