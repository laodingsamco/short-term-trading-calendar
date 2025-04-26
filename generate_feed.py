from datetime import datetime
import pytz

tz = pytz.timezone("US/Eastern")
today = datetime.now(tz)

items = [
    {
        "title": "Tesla 财报预期波动",
        "description": "根据期权隐含波动率，Tesla 盘前可能异动。建议留意 Q1 财报前后走势。",
        "guid": "tesla-2025-04-29"
    },
    {
        "title": "Intel 芯片新品动向",
        "description": "市场传闻 Intel 将发布 AI 芯片更新，引发板块异动。",
        "guid": "intel-2025-05-01"
    },
    {
        "title": "Apple 供应链风险提示",
        "description": "中国区代工厂近期面临出口压力，可能影响 Apple 下季度指引。",
        "guid": "apple-2025-05-02"
    }
]

rss_items = ""
for item in items:
    rss_items += f"""
    <item>
      <title>{item['title']}</title>
      <description>{item['description']}</description>
      <pubDate>{today.strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate>
      <guid>{item['guid']}</guid>
    </item>
    """

rss_feed = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>每周美股前瞻提醒</title>
    <link>https://laodingsamco.github.io/short-term-trading-calendar/feed.xml</link>
    <description>由 ChatGPT 自动生成的美股事件前瞻提醒</description>
    {rss_items}
  </channel>
</rss>
"""

with open("feed.xml", "w") as f:
    f.write(rss_feed)
