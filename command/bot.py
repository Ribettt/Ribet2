import discord

from discord.ext import commands
from discord.ext.commands import command, Cog

class _Bot(Cog):
	
	def __init__(self, bot):
		
		self.bot = bot
		self.bot.remove_command('help')
		
	@Cog.listener()
	async def on_ready(self):
		
		print("Loaded cog..")
		
	@Cog.listener()
	async def on_command_error(self, ctx, error):
		
		if isinstance(error, commands.CommandNotFound):
			
			return
		
		else:
			
			print(error)
		
def setup(bot):
	
	bot.add_cog(_Bot(bot))