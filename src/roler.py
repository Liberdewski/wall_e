import discord
import asyncio

def RoleExists(roles, newRole):
    for role in roles:
        if role.name == newRole:
            return True
    return False

async def MakeNewRole(guild, newRole):
	role = await guild.create_role(name=newRole)
	await role.edit(mentionable=True)
