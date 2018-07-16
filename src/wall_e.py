# Module
import config
import bot_formatter
from roler import RoleExists, MakeNewRole

# Packages
import asyncio
import discord
from discord.ext import commands


########################################################
# VARS
########################################################
bot = commands.Bot(command_prefix=config.prefix)

########################################################
# BOT EVENTS
########################################################

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


########################################################
# BOT COMMANDS
########################################################

@bot.command()
async def ping(ctx):
    await ctx.send(bot_formatter.format("pong!"))

@bot.command()
async def newrole(ctx, newRole):
    if RoleExists(ctx.guild.roles, newRole):
        await ctx.send(bot_formatter.format("already exists"))
    else:
        await MakeNewRole(ctx.guild, newRole)
        await ctx.send(bot_formatter.format("Added new role"))


########################################################
# RUN THE BOT
########################################################
bot.run(config.token)
