import os

import discord
from dotenv import load_dotenv

import Commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def get_username(member):
    try:
        if member.nick:
            return member.nick
        else:
            return member.name
    except AttributeError:
        return member.name
        return "None"

@client.event
async def on_ready():
    print("Connected")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.send(f"Hi {member.name}, welcome to Geo-Clash Dev \U0001F36A!\n\nPlease create a GitHub account and post it in chat.\n\nPlease also ask for role(s)")

@client.event
async def on_message(message):
    # If it is a massage from itself then don't do anything
    if message.author == client.user:   return

    text = message.content.lower()
    username = get_username(message.author)
    user_id = str(message.author.id)

    await Commands.check_cookie(text, message, username, user_id)
    await Commands.check_clear(text, message, username, user_id)
    await Commands.check_cookies(text, message, username, user_id)
    await Commands.check_cheese(text, message, username, user_id)
    await Commands.check_count_cheese(text, message, username, user_id)

print("Connecting")
client.run(TOKEN)
