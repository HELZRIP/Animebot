import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SkyzuRobot.events import register as MEMEK
from SkyzuRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/6a7f2ee2e7c7219df88cd.jpg"

@MEMEK(pattern=("/mhelp"))
async def awake(event):
  tai = event.sender.first_name
  SKYZU = "** ──「 Basic Guide 」── ** \n\n"
  SKYZU += "• /play **(song title) — To Play the song you requested via YouTube** \n"
  SKYZU += "• /search ** (song/video title) – To search for links on YouTube with details** \n"
  SKYZU += "• /playlist - **show the list song in queue** \n"
  SKYZU += "•/lyric - ** (song name) lyrics scrapper** \n\n"
  SKYZU += "** ──「 Admin CMD 」── ** \n\n"
  SKYZU += "• /pause - **To Pause Song playback** \n"
  SKYZU += "• /resume - **To resume playback of the paused Song** \n"
  SKYZU += "• /skip - **To Skip playback of the song to the next Song** \n"
  SKYZU += "• /end - **To Stop Song playback** \n"
  SKYZU  += "• /control - **open the player settings panel** \n"
  SKYZU += "• /reload - **To Refresh admin list** \n"

  BUTTON = [[Button.url("☎️ Support", "https://t.me/OkaeriUserbot"), Button.url("📡 Updates", "https://t.me/nbzoning")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
