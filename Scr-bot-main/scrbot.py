import nextcord
from nextcord.ui import Button, View 
from nextcord.utils import get
from nextcord.ext import commands
import os
from dotenv import load_dotenv
import wikipedia
import smtplib
import datetime
import webbrowser
import youtube_dl
import humanfriendly
import time
import random
import asyncio
import asyncpraw

reddit = asyncpraw.Reddit(client_id= "poL3KE8PgI8doxJB7-aYGw",
                     client_secret = "2aSpJ5aiEmLHKwvkTGE61DblaIM-aw",
                     username = "Advanced_Daikon756",
                     password = "#noobpookveduki1234",
                     user_agent = "scrbot")

intents=nextcord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="*", help_command=None, intents=intents)

@client.event
async def on_ready():
    print("Bot just landed on the server!")
  
@client.event
async def on_member_join(member):
    myEmbed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description="Welcome to the Server!", color=0xffff00)
    myEmbed.add_field(name="🤖" ,value = member.mention, inline=False)
    myEmbed.add_field(name="Description:-",value="The Offical Server of -SCRUNCHY- channel on youtube!", inline=False)
    myEmbed.set_footer(text="Explore outside while being inside \n #DISCORD😎")
    myEmbed.set_author(name="Scrbot#9523")
    chn = client.get_channel(970680080168783902)
    await chn.send(embed=myEmbed)
    
@client.event
async def on_member_remove(member):
    mem_rol = member.roles
    mem_id = member.id
    myEmbed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description=f"{member} has just left the server!", color=0xffff00)
    myEmbed.add_field(name= "ROLES:-" ,value=('\n'.join(map(str, mem_rol))), inline=False)
    myEmbed.add_field(name="❌",value="The above user with the concerned roles have left the server!", inline=False)
    myEmbed.set_author(name="Scrbot#9523")
    chn = client.get_channel(970680080168783902)
    await chn.send(embed=myEmbed)
    
@client.command()
async def private(ctx):
    myEmbed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description=f"Hello there {ctx.author.mention}\n In Private!", color=0xffff00)
    myEmbed.set_author(name="Scrbot#9523")
    await ctx.author.send(embed=myEmbed)
    
@client.command()
async def wiki(ctx, *, arg):
    mes_1 = await ctx.reply("Searching Google!")
    try:
        results = wikipedia.summary(arg, sentences = 10)
        await mes_1.edit(content="According to SCRUNCHY, "+results)
    except Exception as e:
        await mes_1.edit(content="Could not search what you were looking for!")
        
@client.command()
async def luckyroles(ctx, role_id :int):
    user_give = ctx.author
    user_rol = get(user_give.guild.roles, id=882402406804103168)#Owner Role
    if user_rol in user_give.roles or user_give == await client.fetch_user(763676643356835840):
        guild_mem = user_give.guild
        mem_list = []
        for member in guild_mem.members:
            mem_list.append(member)
            
        giveaway_mem = random.choice(mem_list)
        giv_role = get(user_give.guild.roles, id=role_id)
        await giveaway_mem.add_roles(giv_role)
        give_embed = nextcord.Embed(title="-SCRUNCHYPLANET🌎-", description = f"**{giveaway_mem.mention} \n You have just won the giveaway held by {ctx.author.mention}**\n You have got the *{giv_role.mention} !🎆🎊🎉*", color=0xffff00)
        await ctx.send(embed=give_embed)
        try:
            await giveaway_mem.send(embed=give_embed)
        except:
            await message.author.send("Cannot send message to the user who won the giveaway!")
    else:
        await ctx.send("Cannot send message as you don't have necessary role to start a giveaway!\nGo, get a role NOOB!")
        
@client.command()
async def admin(ctx, pas:int , chn_id:int, *, arg):
    if pas == 9523:
        try:
            chn = client.get_channel(chn_id)
            admin_ctx = await ctx.author.send("Sending your message!")
            await chn.send(arg)
            await admin_ctx.edit(content=f"Your message has been sent successfully to this channel {chn.mention}")
        except Exception as e:
            await admin_ctx.edit(content=f"Your message could not be delivered to the channel!\n Here is why {e}")
    else:
        await ctx.send(f"The above password is Wrong {ctx.author.mention}!\nTry again!")
        
@client.command()
async def selfrole(ctx):
    button = Button(label="Fans", style=nextcord.ButtonStyle.green, emoji="🙋‍♂️")
    button2 = Button(label="Ultimate Gamer Fan", style=nextcord.ButtonStyle.red, emoji="🎮")
    button3 = Button(label="Small Artist", style=nextcord.ButtonStyle.blurple, emoji="🖥")
    button4 = Button(label="Anime Fan", style=nextcord.ButtonStyle.blurple, emoji="🦸‍♂️")
    button5 = Button(label="Simp",style=nextcord.ButtonStyle.green, emoji="👦")
    button6 = Button(label="OG Dude", style=nextcord.ButtonStyle.grey, emoji="🤵")
    view = View(timeout=10)
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    view.add_item(button6)
    main = ctx.author
    role = get(main.guild.roles, id=962870754234466304)#Fans role
    role2 = get(main.guild.roles, id=969236228123815947)#Ultimate Gamer Fan role
    role3 = get(main.guild.roles, id=969236370503639071)#Small Artist role
    role4 = get(main.guild.roles, id=969238867645464616)#Anime role
    role5 = get(main.guild.roles, id=969239009001873418)#Simp roles
    role6 = get(main.guild.roles, id=969239180859293696)#OG Dude
    async def button_callback(interaction):
        author = interaction.user
        await interaction.user.add_roles(role)
        if role2 in author.roles:
            await interaction.user.remove_roles(role2)
        elif role3 in author.roles:
            await interaction.user.remove_roles(role3)
        elif role4 in author.roles:
            await interaction.user.remove_roles(role4)
        elif role5 in author.roles:
            await interaction.user.remove_roles(role5)
        elif role6 in author.roles:
            await interaction.user.remove_roles(role6)
        Rembed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description=f"{interaction.user.mention} have applied for the **Fans Role** in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button.callback = button_callback 
    async def button_callback(interaction):
        await interaction.user.add_roles(role2)
        if role in author.roles:
            await interaction.user.remove_roles(role)
        elif role3 in author.roles:
            await interaction.user.remove_roles(role3)
        elif role4 in author.roles:
            await interaction.user.remove_roles(role4)
        elif role5 in author.roles:
            await interaction.user.remove_roles(role5)
        elif role6 in author.roles:
            await interaction.user.remove_roles(role6)
        Rembed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description=f"{interaction.user.mention} have applied for the **Ultimate Gamer Fan Role** in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button2.callback = button_callback 
    async def button_callback(interaction):
        author = interaction.user
        await interaction.user.add_roles(role3)
        if role2 in author.roles:
            await interaction.user.remove_roles(role2)
        elif role in author.roles:
            await interaction.user.remove_roles(role)
        elif role4 in author.roles:
            await interaction.user.remove_roles(role4)
        elif role5 in author.roles:
            await interaction.user.remove_roles(role5)
        elif role6 in author.roles:
            await interaction.user.remove_roles(role6)
        Rembed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description=f"{interaction.user.mention} have applied for the **Small Artist Role** in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button3.callback = button_callback 
    async def button_callback(interaction):
        author = interaction.user
        await interaction.user.add_roles(role4)
        if role2 in author.roles:
            await interaction.user.remove_roles(role2)
        elif role3 in author.roles:
            await interaction.user.remove_roles(role3)
        elif role in author.roles:
            await interaction.user.remove_roles(role)
        elif role5 in author.roles:
            await interaction.user.remove_roles(role5)
        elif role6 in author.roles:
            await interaction.user.remove_roles(role6)
        Rembed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description=f"{interaction.user.mention} have applied for the **Anime Fan Role in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button4.callback = button_callback
    async def button_callback(interaction):
        author = interaction.user
        await interaction.user.add_roles(role5)
        if role2 in author.roles:
            await interaction.user.remove_roles(role2)
        elif role3 in author.roles:
            await interaction.user.remove_roles(role3)
        elif role in author.roles:
            await interaction.user.remove_roles(role)
        elif role4 in author.roles:
            await interaction.user.remove_roles(role4)
        elif role6 in author.roles:
            await interaction.user.remove_roles(role6)
        Rembed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description=f"{interaction.user.mention} have applied for the **SIMP Role** in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button5.callback = button_callback
    async def button_callback(interaction):
        author = interaction.user
        await interaction.user.add_roles(role6)
        if role2 in author.roles:
            await interaction.user.remove_roles(role2)
        elif role3 in author.roles:
            await interaction.user.remove_roles(role3)
        elif role in author.roles:
            await interaction.user.remove_roles(role)
        elif role4 in author.roles:
            await interaction.user.remove_roles(role4)
        elif role6 in author.roles:
            await interaction.user.remove_roles(role5)
        Rembed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description=f"{interaction.user.mention} have applied for the **OG Dude Role** in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button6.callback = button_callback
    await ctx.reply("Here are the various roles! \n Choose What you want to be!", view=view)

@client.command()
async def meme(ctx):
    all_subs = []
    subreddit = await reddit.subreddit("memes")
    top_red = subreddit.top("year", limit=50)
    print("Running!")
    async for top_hot in top_red:
        all_subs.append(top_hot)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    memEmbed = nextcord.Embed(title= name)
    memEmbed.set_image(url = url)
    ctx_mem = await ctx.send(embed = memEmbed)
    await meme_but(ctx,ctx_mem)
        
async def meme_but(ctx,ctx_mem):
    button = Button(label="Yes", style=nextcord.ButtonStyle.green, emoji="🤚")
    view = View(timeout=100)
    view.add_item(button)
    async def button_callback(interaction):
        await mem_rep(ctx,ctx_mem)
    button.callback = button_callback
    await ctx.reply(view = view)
        
async def mem_rep(ctx,ctx_mem):
    all_subs = []
    subreddit = await reddit.subreddit("memes")
    top_red = subreddit.top("year", limit=50)
    async for top_hot in top_red:
        all_subs.append(top_hot)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    memEmbed = nextcord.Embed(title= name)
    memEmbed.set_image(url = url)
    await ctx_mem.edit(embed = memEmbed)
 
@client.command()
async def help(ctx):
    help_embed = nextcord.Embed(title = "**-SCRUNCHYPLANET-**", description = "Here are the various cmds to help you out!", color=0xffff00)
    help_embed.add_field(name="**🤖COMMANDS🤖**", value=f"1.**\*private**: Opens a dm with the user. \n2.**\*wiki [subject]**: Gives Information about the concerned subject. \n3.**\*luckyroles [role_id]**: Makes a giveaway of the mentioned role if the user has suitable permissions.\n4.**\*admin [password] [channel_id] [content]**: Sends the content matter to the described channel through the bot.\n5.**\*selfrole**: Send various options available for roles in the server.\n6.**\*meme**:Gives memes from reddit.",inline = True)
    help_embed.set_author(name = "Scrbot#9523")
    await ctx.reply(embed = help_embed)
            
client.run("*****BOT-TOKEN*****")
