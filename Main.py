
# https://discordapp.com/api/oauth2/authorize?client_id=545902063050031106&permissions=8&scope=bot
import DontStealMyToken
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print ("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Maximum Jebait"))

@client.event
async def on_message(message):
    print(f"{message.author} said '{message.content}'")
    await client.process_commands(message)
@client.event
async def on_message_delete(message):
    await client.send_message(message.channel, f"{message.author} deleted the message '{message.content}'")

@client.command()
async def ping():
    await client.say("Pong!")

@client.command()
async def echo(*args):
    output = "".join(args)
    await client.say(output)

@client.command(pass_context = True)
async def kick(username: discord.User):
    await client.kick(ctx, username)


client.run(DontStealMyToken.TOKEN)