import multiprocessing
from typing import List, Tuple
from collections import Counter
import emoji
import json


# Function to process a chunk of tweet texts and count emojis


def count_top_emojis_time(json_file_path, num_processes=4) -> List[Tuple[str, int]]:

    def count_emojis_chunk(chunk:list) -> Counter:
        emoji_counter = Counter()
        for tweet_text in chunk:
            emoji_counter.update(emoji.distinct_emoji_list(tweet_text))
        return emoji_counter

    tweet_texts = []
    with open(json_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet_data = json.loads(line)
            tweet_texts.append(tweet_data['content'])

    # Split the data into chunks for multiprocessing
    chunk_size = len(tweet_texts) // num_processes
    chunks = [tweet_texts[i:i + chunk_size] for i in range(0, len(tweet_texts), chunk_size)]

    # Count emoji occurrences using multiprocessing
    with multiprocessing.Pool(processes=num_processes) as pool:
        emoji_counters = pool.map(count_emojis_chunk, chunks)

    # Combine results from different processes
    combined_counter = Counter()
    for emoji_counter in emoji_counters:
        combined_counter.update(emoji_counter)

    return combined_counter.most_common(10)



def count_top_emojis_memory(json_file_path) -> List[Tuple[str, int]]:    
    emoji_counter = Counter()

    def process_tweet(tweet_text:str):
        tweet_emoji_counter = Counter(emoji.distinct_emoji_list(tweet_text))
        emoji_counter.update(tweet_emoji_counter)

    with open(json_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet_data = json.loads(line)
            tweet_text = tweet_data['content']
            process_tweet(tweet_text)

    return emoji_counter.most_common(10)

if __name__ == '__main__':
    file_path = '/home/rodrigo/Proyectos_python/Data-Engineer-challenge-Rodrigo-Garcia/tweets/farmers-protest-tweets-2021-2-4.json'
    count_top_emojis_memory(file_path)
    count_top_emojis_time(file_path)