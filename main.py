import asyncio
import aiohttp
import discord
from discord import Webhook
from discord.ext import commands

token = "your SELFbot token here"
bot = commands.Bot(command_prefix="!")

channels = {
# paste your webhooks.txt here (make sure its formatted correctly)
}

@bot.event
async def on_ready():
    print(f"Bot up at {bot.user.name}")

@bot.event
async def on_message(msg):
    try:
        if msg.channel.id in channels:
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(channels[msg.channel.id], session=session)
                files = []
                for i in msg.attachments:
                    f = await i.to_file()
                    files.append(f)

                content = msg.clean_content

                if msg.reference and msg.reference.resolved:
                    replied_message = msg.reference.resolved.content
                    replied_author = msg.reference.resolved.author.name
                    if msg.reference.resolved.stickers or msg.reference.resolved.attachments:
                        content = f"-# <:Reply_msg:1349104162436288512> **{replied_author} |** This message contains something I cannot attach.\n\n{content}"
                    else:
                        content = f"-# <:Reply_msg:1349104162436288512> **{replied_author} |** {replied_message}\n\n{content}"

                await webhook.send(content, embeds=msg.embeds, username=msg.author.display_name, avatar_url=msg.author.avatar.url, files=files)
        await bot.process_commands(msg)
    except Exception as e:
        print(f"An error occurred: {e}")

bot.run(token)
