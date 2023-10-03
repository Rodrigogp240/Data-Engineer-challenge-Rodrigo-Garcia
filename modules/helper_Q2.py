import multiprocessing
from collections import Counter
import emoji
import json


# Function to process a chunk of tweet texts and count emojis
def count_emojis_chunk(chunk:list):
    emoji_counter = Counter()
    for tweet_text in chunk:
        emoji_counter.update(emoji.distinct_emoji_list(tweet_text))
    return emoji_counter

def count_top_emojis_time(json_file_path:str, num_processes=4):
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



def count_top_emojis_memory(json_file_path):

    
    emoji_counter = Counter()

    def process_tweet(tweet_text):
        tweet_emoji_counter = Counter(emoji.distinct_emoji_list(tweet_text))
        emoji_counter.update(tweet_emoji_counter)

    with open(json_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet_data = json.loads(line)
            tweet_text = tweet_data['content']
            process_tweet(tweet_text)

    return emoji_counter.most_common(10)
