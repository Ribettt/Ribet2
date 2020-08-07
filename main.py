import discord, os
from discord.ext import commands

bot = commands.AutoShardedBot(
	command_prefix = "ai!", 
	shard_count = 5
	)

@bot.event
async def on_ready():
	
	print("Repl.it turn on.")
	print("{} ready.".format(bot.user.name))
	
@bot.event
async def on_shard_ready(shard_id):
	
	print(shard_id)
	
for file in os.listdir('./command'):
	
	if file.endswith('.py'):
		
		bot.load_extension(f'command.{file[:-3]}')

bot.run(os.environ.get("Token"))