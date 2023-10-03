from collections import Counter
import json


def count_top_mentions_time(json_file_path):
    mentions_list = []
    with open(json_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet_data = json.loads(line)
            if tweet_data['mentionedUsers']:
                mentions_list.extend([user['username'] for user in tweet_data['mentionedUsers']])
    mentions_counter = Counter(mentions_list)
    return mentions_counter.most_common(10)

def count_top_mentions_memory(json_file_path):
    mentions_counter = Counter()
    with open(json_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet_data = json.loads(line)
            if tweet_data['mentionedUsers']:
                for users in tweet_data['mentionedUsers']:
                    username = users['username']
                    mentions_counter[username] += 1
    
    return mentions_counter.most_common(10)

        
if __name__ == '__main__':
    file_path = '/home/rodrigo/Proyectos_python/Data-Engineer-challenge-Rodrigo-Garcia/tweets/farmers-protest-tweets-2021-2-4.json'
    count_top_mentions_memory(file_path)
    count_top_mentions_time(file_path)





    