import json
import re
from collections import Counter
import multiprocessing

def get_data(file_path: str):
    data = []
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            data.append(tweet['content'])
    return data

def find_emojis(tweet_text):
    emoji_pattern = re.compile(r"[\U0001F600-\U0001F64F"
                            r"\U0001F300-\U0001F5FF"
                            r"\U0001F680-\U0001F6FF"
                            r"\U0001F700-\U0001F77F"
                            r"\U0001F780-\U0001F7FF"
                            r"\U0001F800-\U0001F8FF"
                            r"\U0001F900-\U0001F9FF"
                            r"\U0001FA00-\U0001FA6F"
                            r"\U0001FA70-\U0001FAFF"
                            r"\U0001F004-\U0001F0CF"
                            r"\U0001F170-\U0001F251]+", flags=re.UNICODE)
    
    emojis = emoji_pattern.findall(tweet_text)
    return emojis

def count_top_emojis(json_file_path, num_processes=4, top_n=10):
    # Open and read the JSON file
    tweet_texts = get_data(json_file_path)
    # Count emoji occurrences using multiprocessing
    emoji_counter = Counter()
    with multiprocessing.Pool(processes=num_processes) as pool:
        emoji_lists = pool.map(find_emojis, tweet_texts)
        for emojis in emoji_lists:
            emoji_counter.update(emojis)

    # Get the top N most common emojis
    top_n_emojis = emoji_counter.most_common(top_n)

    return top_n_emojis

if __name__ == '__main__':
    file_path = '/home/rodrigo/Proyectos_python/Data-Engineer-challenge-Rodrigo-Garcia/tweets/farmers-protest-tweets-2021-2-4.json'
    top_10_emojis = count_top_emojis(file_path)