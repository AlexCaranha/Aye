
from fuzzywuzzy import fuzz
import re

def iif(condition:bool, then_value, else_value):    
    return then_value if condition else else_value

def is_the_question_with_sentence(pattern, input: str):
    match = re.search(pattern, input, re.IGNORECASE)
    output = match.group('sentence') if match is not None else None
    return output

def is_the_question(pattern, input: str, threshold = 85):
    ratio = fuzz.token_set_ratio(pattern, input)
    return ratio > threshold

def set_rate(engine, rate, rate_variation=None):
    if not rate is None:
        rate = rate
        engine.setProperty('rate', rate)
        return

    rate *= (1 + rate_variation)
    engine.setProperty('rate', rate)