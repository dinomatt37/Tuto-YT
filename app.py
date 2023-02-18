import discord
import random
from discord.ext import commands
import asyncio

client = commands.Bot(
  command_prefix='/', # Le préfix pour les commandes est "/"
  case_insensitive=False,
  description=None,
  intents=discord.Intents.all(),
  help_command=None
)

@client.command()
async def abo(ctx):
    await ctx.send(f"N'oubliez pas de vous abonner à ma chaîne YouTube : https://www.youtube.com/@dinomatt37/")

client.run("Votre clé")