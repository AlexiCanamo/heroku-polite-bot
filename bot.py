import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.event
async def on_message(message):
    if "Thank" in str(message.content) or 'thank' in str(message.content):
        return await bot.send_message(message.channel, f"Your welcome! {message.author.mention}")

    if "Night" in str(message.content) or 'night' in str(message.content):
        return await bot.send_message(message.channel, f"Have sweet dreams! {message.author.mention}")

    await bot.proccess_command()
        
@bot.command() # You don't need to pass context
async def wake_up(user: discord.Member):
    for i in range(100): # How often you want to send the message
        await bot.send_message(user, 'Wake up!')


bot.run("NDUxMzQ5MDU1MDMzODM1NTQw.DfApKg.bBC95C-Jr18G_P5TAUla5xglifc")

    
