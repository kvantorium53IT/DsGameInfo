import urllib.request
import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])
@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def sales(ctx): # Создаём функцию и передаём аргумент ctx.

    await ctx.send() # 
    # Выводим сообщение с упоминанием автора, обращаясь к переменной author.