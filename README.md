# Latam Data Engineering Challenge

## Question 1

For this part of the challenge, the code between the runtime and memory-optimized versions is pretty similar since the best method I could come up with reduced the runtime and memory usage. So, the code is pretty much the same except for the method I used in the return value. In my testing, using the approach from q1_memory reduced the consumption of memory by approximately 23% compared to q1_time and increased runtime by about 6%.

|          |   Time        |  Memory   |
|:---------|:------------:|:---------:|
| Q1_time  |  3.35 seconds |  6.8 MiB |
| Q1_memory| 3.55 seconds |   4.1 MiB |

## Question 2

In this question, I took a different approach for the time-sensitive version. By using chunking and multiprocessing, I made a significant reduction in runtime. Another optimization I wanted to implement was using Regex instead of the emoji library, but I couldn't find the right one. Since the Emoji library is just a wrapper with a JSON file that contains the encoding for the emojis, I suspect I could reduce both runtime and memory usage if I were to find the correct regex or wildcard expression.

|          |   Time        |  Memory   |
|:---------|:------------:|:---------:|
| Q2_time  |  3.07 seconds |  41.3 MiB |
| Q2_memory| 11.02 seconds |   2.1 MiB |


## Question 3

Just like the first one, the code is pretty much identical, except for the fact that in the memory-conscious function, I process the file tweet by tweet to save on storing the whole file in memory.

|          |   Time        |  Memory   |
|:---------|:------------:|:---------:|
| Q3_time  |  3.07 seconds |  7.7 MiB  |
| Q3_memory|  3.6 seconds  |   1 MiB   |





