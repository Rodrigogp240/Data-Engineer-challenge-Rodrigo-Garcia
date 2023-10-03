import json
from datetime import datetime
from collections import Counter
from typing import List, Tuple


def get_top_10_users_for_top_10_dates_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    user_counter = Counter()
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.strptime(
                tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = tweet['user']['username']
            user_counter[(date, user)] += 1

    top_10_items = user_counter.most_common(10)
    return [item[0] for item in top_10_items]


def get_top_10_users_for_top_10_dates_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    user_counter = Counter()
    with open(file_path, 'r') as file:
        for line in file:
            record = json.loads(line)
            date = datetime.strptime(
                record['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = record['user']['username']
            user_counter[(date, user)] += 1

    return [item for item, _ in user_counter.most_common(10)]


if __name__ == '__main__':
    file_path = '/home/rodrigo/Proyectos_python/Data-Engineer-challenge-Rodrigo-Garcia/tweets/farmers-protest-tweets-2021-2-4.json'
    get_top_10_users_for_top_10_dates_memory(file_path)
    get_top_10_users_for_top_10_dates_time(file_path)
