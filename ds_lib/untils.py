import re
from datetime import datetime, timedelta

def camel_to_snake(data: str) -> str:
    _name = re.sub("(.)[(]A-Z][a-z]")