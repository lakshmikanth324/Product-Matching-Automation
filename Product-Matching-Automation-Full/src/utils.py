
import re

def clean_text(x):
    return re.sub(r'[^a-zA-Z0-9 ]', '', x.lower())
