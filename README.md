### Scrapy for www.fang.com

#### Basic introduction

Use scrapy to crawl domestic cities' community data via www.fang.com

Currently, just some basic information about a specific community.

​It will crawl through 600+ cities. For a classic 1-level :arrow_up: city(like Shanghai, Nanjing), there are 1000+ community records.

FYI, the data is DIRTY.

#### Damn it….

👿With some ridiculous reason, if the city is in northern part of China, the crawler will show INFO:

`Connection to the other side was lost in a non-clean fashion: Connection lost.`

This conclusion is based on test for Beijing, Tianjin, Dalian, Shenyang, Harbin. **Maybe it's just not my day.**

Guess that it is caused by separation of servers, one group in north while another in south.

*Anyone who could handle this issue or help anything out, please leave a comment or issue* 👏

#### So, what I do…..

Due to the reason above, I only tested my crawler through some cities in Shanghai, Jiangsu, Zhejiang with a special URL file read by the crawler… :cry:

#### TODO: BUG FIXED

Still some internet problems.

e.g. `TCP connection timed out: 60: Operation timed out.`

I tried multiple user-agents and multiple proxies. It seemed multiple proxies didn't work for me.