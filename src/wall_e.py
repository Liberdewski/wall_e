# Module
import config
import constants
import roler
from constants import ROLE_ADDED, ROLE_ALREADY_EXISTS
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
# FUNCTIONS
########################################################

def wrap(message):
    return "```" + message + "```"

async def send(ctx, output):
    await ctx.send(wrap(output))


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
async def newrole(ctx, role):
    if RoleExists(ctx.guild.roles, role):
        await send(ctx, ROLE_ALREADY_EXISTS.format(role))
    else:
        await MakeNewRole(ctx.guild, role)
        await send(ctx, ROLE_ADDED.format(role))


########################################################
# RUN THE BOT
########################################################
bot.run(config.token)
