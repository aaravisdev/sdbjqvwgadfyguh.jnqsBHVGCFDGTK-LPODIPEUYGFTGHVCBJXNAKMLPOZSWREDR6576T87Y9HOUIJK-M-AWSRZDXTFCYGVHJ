from discord.ext import commands
import discord
from time import sleep, time
import uuid
import random

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

yourrole = 'Buyer'

@client.event
async def on_ready():
    print("Bot is online and ready")

@client.command()
async def gen(ctx, amount):
    start_time = time()
    key_amt = range(int(amount))
    f = open("keys.txt", "a")
    show_key = ''
    for x in key_amt:
        key = str(uuid.uuid4())
        show_key += "\n" + key
        f.write(key)
        f.write("\n")

    if len(str(show_key)) == 37:
        show_key = show_key.replace('\n', '')
        await ctx.send(f"Key: {show_key}")
        end_time = time()
        await ctx.send(f"Generation Time: {end_time - start_time:.2f} seconds")
        return 0
    if len(str(show_key)) > 37:
        await ctx.send(f"Keys: {show_key}")
        end_time = time()
        await ctx.send(f"Generation Time: {end_time - start_time:.2f} seconds")
    else:
        await ctx.send("Somethings wrong")

@client.command()
async def redeem(ctx, key):
    start_time = time()
    if len(key) == 36:
        with open("used keys.txt") as f:
            if key in f.read():
                em = discord.Embed(color=0xff0000)
                em.add_field(name="Invalid Key", value="Inputed key has already been used!")
                await ctx.send(embed=em)
                return 0
        with open("keys.txt") as f:
            if key in f.read():
                role = discord.utils.get(ctx.guild.roles, name=yourrole)
                await ctx.author.add_roles(role)
                em = discord.Embed(color=0x008525)
                em.add_field(name="Key Redeemed", value="Key has now been redeemed")
                await ctx.send(embed=em)
                f = open("used keys.txt", "w")
                f.write(key)
                f.write('\n')
                end_time = time()
                await ctx.send(f"Redemption Time: {end_time - start_time:.2f} seconds")
            else:
                em = discord.Embed(color=0xff0000)
                em.add_field(name="Invalid Key", value="Inputed key has already been used!")
                await ctx.send(embed=em)
                end_time = time()
                await ctx.send(f"Redemption Time: {end_time - start_time:.2f} seconds")
    else:
        em = discord.Embed(color=0xff0000)
        em.add_field(name="Invalid Key", value="Inputed key has already been used!")
        await ctx.send(embed=em)
        end_time = time()
        await ctx.send(f"Redemption Time: {end_time - start_time:.2f} seconds")

@client.command()
async def mines(ctx, tile_amt: int, round_id: str):
    start_time = time()
    if len(round_id) == 64:
        grid = ['❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌']
        already_used = []

        count = 0
        while tile_amt > count:
            a = random.randint(0, 24)
            if a in already_used:
                continue
            already_used.append(a)
            grid[a] = '✅'
            count += 1
        
        chance = random.randint(45, 95)
        if tile_amt < 4:
            chance = chance - 15

        em = discord.Embed(color=0xff8c00)  # Changed color to a shade of orange
        em.add_field(name='Grid', value="\n" + "```"+grid[0]+grid[1]+grid[2]+grid[3]+grid[4]+"\n"+grid[5]+grid[6]+grid[7]+grid[8]+grid[9]+"\n"+grid[10]+grid[11]+grid[12]+grid[13]+grid[14]+"\n"+grid[15]+grid[16]+grid[17] \
            +grid[18]+grid[19]+"\n"+grid[20]+grid[21]+grid[22]+grid[23]+grid[24] + "```\n" + f"**Accuracy**\n```{chance}%```\n**Round ID**\n```{round_id}```\n**Response Time:**\n```{time() - start_time:.2f} seconds```")
        em.set_footer(text='made by Aarav')
        await ctx.send(embed=em)
    else:
        em = discord.Embed(color=0xff0000)
        em.add_field(name='Error', value="Invalid round id")
        await ctx.send(embed=em)

client.run('MTI0MDMxNjQ0OTA1NTA1MTg3Nw.Gk2ZiV.yQQVXZfd6ON0KtXmMZpc3n6QKw6ebBo51lRIUI')
