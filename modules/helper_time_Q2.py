import re
import json
from collections import Counter
from typing import List, Tuple

emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F700-\U0001F77F"  # alchemical symbols
                           u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                           u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                           u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                           u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                           u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                           u"\U0001F004-\U0001F0CF"  # CJK Compatibility Ideographs
                           u"\U0001F170-\U0001F251"  # Enclosed Ideographic Supplement
                           "]+", flags=re.UNICODE)

def get_data(file_path: str):
    data = []
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            text = tweet['text']
    return data

def q2_time(file_path: str):
    data = get_data(file_path)
    return data

if __name__ == '__main__':
    file_path = '/home/rodrigo/Proyectos_python/Data-Engineer-challenge-Rodrigo-Garcia/tweets/farmers-protest-tweets-2021-2-4.json'
    q2_time(file_path)