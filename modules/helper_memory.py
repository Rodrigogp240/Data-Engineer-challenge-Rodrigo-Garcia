from collections import Counter
import json
from typing import List, Tuple
from datetime import datetime

def get_data(file_path: str) -> List[Tuple[datetime.date, str]]:
    data = []
    date_counter = Counter()
    
    with open(file_path) as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = tweet['user']['displayname']
            data.append((date, user))
            date_counter[date] += 1
    
    top_10_dates = date_counter.most_common(10)
    
    top_10_users = [(date, user) for date, user in data if date in (date for date, _ in top_10_dates)]
    
    user_counter = Counter(top_10_users)
    top_10_users = user_counter.most_common(10)
    
    return top_10_users

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    top_10 = get_data(file_path)
    return top_10

print(q1_memory(r'tweets\farmers-protest-tweets-2021-2-4.json'))


