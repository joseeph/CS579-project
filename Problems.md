# The problems


arxiv problems：
1. searching by name for papers and authors sometimes response nothing. So I search the paper with paper ID, but I haven't found a good way to search authors except their names.
2. Sometimes the arxiv's connection is refused. But it is very rare. So I save the crawled result frequently. Next time it continues crawling the arxiv based on the saved result.


stanford high energy physics theory citation dataset problems:
1. About 20000+ paper ids can't be found in the abstract directory, I need to crawl them from arxiv
2. Some paper ids are wrong. For example, 1001 should be 0001001. 119912033 should be 9912033. There are 7 digits for each paper.
3. 