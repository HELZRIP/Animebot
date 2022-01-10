import random
from SkyzuRobot.events import register
from SkyzuRobot import telethn

APAKAH_STRING = [
    "Iya",
    "Tidak",
    "Mungkin",
    "Mungkin Tidak",
    "Bisa jadi",
    "Mungkin Tidak",
    "Tidak Mungkin",
    "YNTKTS",
    "Ya gk Tau Kok Tanya Saya",
    "Apa iya?",
    "Tanya aja sama mamak kau tu pler",
]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply("Berikan saya pertanyaan paham 😑😑")
        return
    await event.reply(random.choice(APAKAH_STRING))
