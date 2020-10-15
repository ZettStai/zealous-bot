# main.py
# Main code for the bot to receive events

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# client = discord.Client()

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():

  for guild in client.guilds:
    if guild.name == GUILD:
      break

  print(
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})'
  )
  #print(f'{client.user} has connected to Discord!')

  members = '\n - '.join([member.name for member in guild.members])
  print(f'Guild Members:\n - {members}')


@client.command()
async def ping(ctx):
  await ctx.send('Pong!')

## @client.event
# async def on_message(message):

#   if message.author == client.user:
#     return

#   if 'wynonna earp' in message.content.lower():
#     await message.channel.send('😒🍍')

#   if message.content.startswith('z!'):
#     await message.channel.send('Hello ' + str(message.author))

client.run(TOKEN)


#  Imports
# const Discord = require('discord.js');
# const FileStream = require('fs');
# const Configuration = require('./config.json');

# // Variables
# const client = new Discord.Client();

# // Things to do on start
# setCommands(client);
# client.login(Configuration.token);

# // Events to listen on
# client.once('ready', () => onReady());
# client.on('message', message => onMessage(message));

# // Functions
# function setCommands(client) {
#     client.commands = new Discord.Collection();

#     const commandFiles = FileStream.readdirSync('./commands').filter(file => file.endsWith('.js'));

#     for (const file of commandFiles) {
#         const command = require(`./commands/${file}`);
#         client.commands.set(command.name, command);
#     }
# }

# function onReady() {
#     console.log('Ready!');
# }

# function onMessage(message) {
#     if (isValidCommand(message.author, message.content)) {
#         const command = getCommand(message.content, Configuration.prefix);
#         const args = getArgs(message.content);

#         if (client.commands.has(command)) {
#             try {
#                 const module = client.commands.get(command);
#                 module.execute(message, args);
#             } catch (error) {
#                 console.error(error);
#             }
#         }
#     }
# }

# function isValidCommand(user, string) {
#     return !user.bot && string.startsWith(Configuration.prefix);
# }

# function getCommand(string, prefix) {
#     var words = string.split(/\s+/);
#     var command = words.shift();
#     return command.slice(prefix.length);
# }

# function getArgs(string) {
#     var words = string.split(/\s+/);
#     words.shift();
#     return words;
# }