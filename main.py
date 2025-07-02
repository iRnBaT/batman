
from telethon import TelegramClient, events, Button
from utils import check_proxy
import re, random, os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
target_channel = os.getenv("TARGET_CHANNEL")
source_channels = os.getenv("SOURCE_CHANNELS").split(',')

client = TelegramClient('proxybot', api_id, api_hash).start(bot_token=bot_token)
proxy_regex = re.compile(r'(t\.me/proxy\?server=[^\s&]+&port=\d+&secret=[^\s]+)')

fun_texts = [
    "🔥 پروکسی خفنم آماده‌ست!",
    "🚀 به سرعت اینترنت موشک!",
    "💥 آماده برای وصل شدن!",
    "🛡️ فیلترشکنِ قوی!",
    "🌪 بدون تأخیر وصل شو!"
]

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    links = proxy_regex.findall(event.raw_text)
    for link in links:
        ok = await check_proxy(link)
        if not ok:
            continue
        text = random.choice(fun_texts)
        btn = Button.url("🔗 وصل کن", link)
        await client.send_message(target_channel, f"{text}\n", buttons=btn)

print("🚀 Bot is running...")
client.run_until_disconnected()
