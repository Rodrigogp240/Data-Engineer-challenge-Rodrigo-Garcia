# Latam Data Engineering Challenge

Table of Contents
- [Question 1](#question-1)
- [Question 2](#question-2)
- [Question 3](#question-3)


---

## Question 1

### Implementation Details
For this part of the challenge, the code between the runtime and memory-optimized versions is quite similar since the best method I could come up with reduced both runtime and memory usage. The code is almost the same except for the method I used in the return value. In my testing, using the approach from q1_memory reduced memory consumption by approximately 23% compared to q1_time and increased runtime by about 6%.

### Performance Metrics
|          |   Time        |  Memory   |
|:---------|:------------:|:---------:|
| Q1_time  |  3.35 seconds |  6.8 MiB |
| Q1_memory| 3.55 seconds  |   4.1 MiB |

### Conclusion
In Question 1, we compared the time and memory performance of two implementations. While the memory-optimized version significantly reduced memory usage, it slightly increased runtime. The choice between the two versions depends on the specific requirements of the use case.

---

## Question 2

### Implementation Details
In this question, I took a different approach for the time-sensitive version. By using chunking and multiprocessing, I achieved a significant reduction in runtime. Another optimization I wanted to implement was using Regex instead of the emoji library, but I couldn't find the right one. Since the Emoji library is just a wrapper with a JSON file that contains the encoding for the emojis, I suspect I could reduce both runtime and memory usage if I were to find the correct regex or wildcard expression.

### Performance Metrics
|          |   Time        |  Memory   |
|:---------|:------------:|:---------:|
| Q2_time  |  3.07 seconds |  41.3 MiB |
| Q2_memory| 11.02 seconds |   2.1 MiB |

### Conclusion
In Question 2, we significantly improved time performance by using chunking and multiprocessing. However, memory usage increased due to these optimizations. Further exploration of Regex-based emoji extraction may yield better results in terms of both time and memory efficiency.

---

## Question 3

### Implementation Details
Just like the first one, the code is pretty much identical, except for the fact that in the memory-conscious function, I process the file tweet by tweet to save on storing the whole file in memory.

### Performance Metrics
|          |   Time        |  Memory   |
|:---------|:------------:|:---------:|
| Q3_time  |  3.07 seconds |  7.7 MiB  |
| Q3_memory|  3.6 seconds  |   1 MiB   |

### Conclusion
In Question 3, we compared the time and memory performance of two implementations, with the memory-optimized version processing the file tweet by tweet to reduce memory usage. Both versions showed similar time performance, but the memory-optimized version is more memory-efficient.

---

## Final Thought

While optimizing for runtime and memory is always a good practice, I personally would not take it to the extreme if it sacrifices the readability of the code in most circumstances.






