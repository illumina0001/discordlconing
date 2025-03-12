import asyncio
import aiohttp
import discord
from discord.ext import commands

TOKEN = "user bot token"
SOURCE_GUILD_ID = 1231233123 #the server you want to clone the channels OF
RECEIVER_GUILD_ID = 123123213 #server you want to clone to channels TO

bot = commands.Bot(command_prefix="!")
webhook_map = {}

def save():
    try:
        with open("webhooks.txt", "w") as file:
            for chan_id, wh_url in webhook_map.items():
                file.write(f'{chan_id}: "{wh_url}"\n')
        print("wh saved to webhooks.txt")
    except Exception as e:
        print(f"cant write webhooks.txt: {e}")

@bot.event
async def on_ready():
    print(f"Bot up as {bot.user}")
    source_guild = bot.get_guild(SOURCE_GUILD_ID)
    receiver_guild = bot.get_guild(RECEIVER_GUILD_ID)

    if not source_guild:
        print(f"cant find source guild {SOURCE_GUILD_ID}")
        return
    if not receiver_guild:
        print(f"cant find receiver guild {RECEIVER_GUILD_ID}")
        return

    print("cloning cats")
    category_map = {}
    for source_category in sorted(source_guild.categories, key=lambda c: c.position):
        try:
            new_cat = await receiver_guild.create_category(name=source_category.name, position=source_category.position)
            category_map[source_category.id] = new_cat
            print(f"made category: {new_cat.name}")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"couldn't make category '{source_category.name}': {e}")

    print("cloning channels and making whs")
    for source_channel in sorted(source_guild.channels, key=lambda c: c.position):
        if isinstance(source_channel, discord.CategoryChannel):
            continue
        try:
            new_parent = category_map.get(source_channel.category.id) if source_channel.category else None
            if isinstance(source_channel, discord.TextChannel):
                new_channel = await receiver_guild.create_text_channel(name=source_channel.name, category=new_parent, position=source_channel.position)
                print(f"made text ch: {new_channel.name}")
                try:
                    webhook = await new_channel.create_webhook(name=f"{source_channel.name}_webhook")
                    webhook_map[source_channel.id] = webhook.url
                    print(f"wh made for {new_channel.name}")
                except Exception as wh_e:
                    print(f"wh creation error in {new_channel.name}: {wh_e}")
            elif isinstance(source_channel, discord.VoiceChannel):
                await receiver_guild.create_voice_channel(name=source_channel.name, category=new_parent, position=source_channel.position)
                print(f"made voice channel: {source_channel.name}")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"couldn't make channel '{source_channel.name}': {e}")
    save()

bot.run(TOKEN)
