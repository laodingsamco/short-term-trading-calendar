from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

# 设置美东时区
tz = pytz.timezone("US/Eastern")

# 获取本周一
today = datetime.now(tz)
monday = today - timedelta(days=today.weekday())

# 创建日历
calendar = Calendar()

# 构造本周的事件（每次生成内容不同，避免重复）
for i, stock in enumerate(["Tesla", "Intel", "Apple"]):
    event = Event()
    event.name = f"{stock} 本周事件 - {monday.strftime('%Y-%m-%d')}"
    event.begin = tz.localize(datetime(monday.year, monday.month, monday.day + i, 9, 30))
    event.end = event.begin + timedelta(minutes=30)
    event.description = f"{stock} 自动生成的观察事件（{today.strftime('%Y-%m-%d %H:%M:%S')}）"
    calendar.events.add(event)

# 写入文件
with open("short_term_trading.ics", "w") as f:
    f.writelines(calendar.serialize_iter())
