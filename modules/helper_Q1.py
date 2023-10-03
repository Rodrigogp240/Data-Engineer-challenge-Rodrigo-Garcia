import json
from datetime import datetime
from collections import Counter
from typing import List, Tuple

## reading json file, sorting key information, populating date_counter
def get_data(file_path: str) -> (List[Tuple[datetime.date, str]],Counter):
    data = []
    date_counter = Counter()
    with open(file_path,encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = tweet['user']['username']
            data.append((date, user))
            date_counter[date] += 1
    return data,date_counter

def get_top_10_users_for_top_10_dates_time(file_path:str) -> List[Tuple[datetime.date, str]]:
    data,date_counter = get_data(file_path)
    top_10_dates = [date for date, _ in date_counter.most_common(10)]
    
    top_10_users = [(date, user) for date, user in data if date in top_10_dates]
    
    user_counter = Counter(top_10_users)
    temp_top_10_users = user_counter.most_common(10)
    top_10_users = [(date, user) for (date, user), _ in temp_top_10_users]
    
    return top_10_users

def get_top_10_users_for_top_10_dates_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    user_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            record = json.loads(line)
            date = datetime.strptime(record['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = record['user']['username']
            user_counter[(date, user)] += 1

    return [item for item, _ in user_counter.most_common(10)]

if __name__ == '__main__':
    file_path = '/home/rodrigo/Proyectos_python/Data-Engineer-challenge-Rodrigo-Garcia/tweets/farmers-protest-tweets-2021-2-4.json'
    get_top_10_users_for_top_10_dates_time(file_path)
