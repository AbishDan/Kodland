import discord
from discord.ext import commands
from bot_logic import gen_pass, gen_image,get_duck_image_url,get_fox_image_url
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def make_a_password(ctx,length):
    await ctx.send(gen_pass(int(length)))
@bot.command()
async def mem(ctx):
    with open(f'images/{gen_image()}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)



@bot.command()
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def fox(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)
bot.run("MTEyMDY5MjI3MDQ2NzkxNTgxNg.G8QExd.EsnfUCWweZLnBDZhYVi7-20RdRwMNn-YpZAP8g")

