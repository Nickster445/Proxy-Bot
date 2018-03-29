# Proxy bot by Nickster445

import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def firstcommand(ctx):
    await bot.say("You've run the first command!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Serverinfo")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info(ctx):
    await bot.say("This is the bot that will take care of your server! Join the development discord: https://discord.gg/uczTyDT!")
    print ("Someone used -info")

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say("Welp, there goes {}...".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
async def unban(ctx, user: discord.Member):
    await bot.say("{} Has been banned.".format(user.name))
    await bot.unban(user)

bot.run("NDIwNTc5NzM3MDIzMjgzMjAw.DZ6mJQ.YSZoq7BuYQSImJO5Seew_UniHkA")
