import discord
import random

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if random.random() < 0.1:
        await message.channel.send("custom message here")

client.run("BOT-TOKEN-GOES-HERE")