import discord
from discord.ext import commands

import json

config_file_path = './config/main.json'
config_file = open(config_file_path, 'r')
config = json.load(config_file)

indents = discord.Indents.all()
bot = commands.Bot(command_prefix = str(config['prefix']), indents = indents)
#bot.remove_command('help') #Uncomment when using an external Help command (official WIP)

bot.run(str(config['api_key']))