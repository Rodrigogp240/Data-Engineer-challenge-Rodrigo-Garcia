import json
from datetime import datetime
from collections import Counter
from typing import List, Tuple

def get_data(file_path: str) -> List[Tuple[datetime.date, str]]:
    data = []
    with open(file_path) as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = tweet['user']['displayname']
            data.append((date, user))
    return data

def get_top_10_users_for_top_10_dates(data: List[Tuple[datetime.date, str]]) -> List[Tuple[datetime.date, str]]:
    date_counter = Counter(date for date, _ in data)
    top_10_dates = [date for date, _ in date_counter.most_common(10)]
    
    top_10_users = [(date, user) for date, user in data if date in top_10_dates]
    
    user_counter = Counter(top_10_users)
    temp_top_10_users = user_counter.most_common(10)
    top_10_users = [(date, user) for (date, user), _ in temp_top_10_users]
    
    return top_10_users

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    data = get_data(file_path)
    top_10 = get_top_10_users_for_top_10_dates(data)
    return top_10

