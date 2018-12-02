import discord
from discord.ext import commands
import youtube_dl
import time


TOKEN = 'NDg4MjgzNDU4NDQ0MTk3OTI5.DrjAQA.EBV3UvW-uOXBxCBPddqNVzL34C4'

client = commands.Bot(command_prefix='$')
client.remove_command('help')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(pass_context = True)
async def ping(ctx):
    msg = discord.Embed(title='Pong!', colour=0x66CC99)
    msg.set_author(name=client.user.display_name, icon_url=client.user.avatar_url)
    await client.say(embed=msg)

@client.command()
async def echo(*args):
    output = ''
    for words in args:
        output += words
        output += ' '
    await client.say(output)


@client.command(pass_context = True)
async def membre(ctx):
    msg = ctx.message.author.mention + ' voici les membre:'
    await client.say(msg)
    for server in client.servers:
        for member in server.members:
            await client.say(member)

@client.command(pass_context = True)
async def channels(ctx):
    msg = ctx.message.author.mention + ' voici les channels:'
    await client.say(msg)
    for server in client.servers:
        for channel in server.channels:
            await client.say(channel)

@client.command()
async def game(*args):
    output = ''
    for words in args:
        output += words
        output += ' '
    await client.change_presence(game=discord.Game(name = output))

@client.command(pass_context=True)
async def quickpoll(ctx, question, *options: str):

        if len(options) <= 1:
            await client.say('Vous avez besoin plus d une option pour faire un poll!')
            return
        if len(options) > 10:
            await client.say('Vous ne pouvez pas fair un poll avec plus de 10 réponses!')
            return

        if len(options) == 2 and options[0] == 'oui' and options[1] == 'non':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)


@client.command(pass_context=True)
async def tally(ctx, id):
    poll_message = await client.get_message(ctx.message.channel, id)
    if not poll_message.embeds:
        return
    embed = poll_message.embeds[0]
    if poll_message.author != ctx.message.server.me:
        return
    if not embed['footer']['text'].startswith('Poll ID:'):
        return
    unformatted_options = [x.strip() for x in embed['description'].split('\n')]
    opt_dict = {x[:2]: x[3:] for x in unformatted_options} if unformatted_options[0][0] == '1' \
        else {x[:1]: x[2:] for x in unformatted_options}
    # check if we're using numbers for the poll, or x/checkmark, parse accordingly
    voters = [ctx.message.server.me.id]  # add the bot's ID to the list of voters to exclude it's votes

    tally = {x: 0 for x in opt_dict.keys()}
    for reaction in poll_message.reactions:
        if reaction.emoji in opt_dict.keys():
            reactors = await client.get_reaction_users(reaction)
            for reactor in reactors:
                if reactor.id not in voters:
                    tally[reaction.emoji] += 1
                    voters.append(reactor.id)

    output = 'Résultats pour le poll "{}":\n'.format(embed['title']) + \
             '\n'.join(['{}: {}'.format(opt_dict[key], tally[key]) for key in tally.keys()])
    await client.say(output)

@client.command(pass_context = True)
async def color(ctx):
    colors = [0x9400D3, 0x0000FF, 0x00FF00, 0xFFFF00, 0xFF7F00, 0xFF0000]
    for colorss in colors:
        msg = discord.Embed(title='test', description='test', colour=colorss)
        msg.set_author(name=client.user.display_name, icon_url=client.user.avatar_url)
        await client.say(embed=msg)

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(title='Help', colour=discord.colour.Color.dark_blue(), description='<args>=pas obligatoire/ [args] obligatoire')
    embed.add_field(name='$ping', value=' Pong!', inline=False)
    embed.add_field(name='$echo <args>', value=' Echo', inline=False)
    embed.add_field(name='$membre', value=' Dit tout les membres', inline=False)
    embed.add_field(name='$channels', value=' Dit tout les channels', inline=False)
    embed.add_field(name='$game [args]', value=' Change le jeu auquel le bot joue', inline=False)
    embed.add_field(name='$quickpoll [question] [réponses]', value=' Fait un poll.Pour réponses: pas plus de 10 réponses ou yes no pour faire un yes no', inline=False)
    embed.add_field(name='$tally [ID]', value=' Dit les résultats du poll avec ID du poll', inline=False)
    embed.add_field(name='$color', value=' LSD ou just un test pour les embed de discord', inline=False)
    embed.add_field(name='$play [waves] ou [joe] ou [un custom RADIO url] ou [stop]', value=' Joue une radio. site pour url:http://fluxradios.blogspot.com', inline=False)
    embed.add_field(name='$playt [url] ou [stop]', value='Joue un link Youtube.', inline=False)
    embed.add_field(name='$help', value=' je sais pas', inline=False)
    embed.add_field(name=' fait par Pixelbo',value=' Thriller!' , inline=False)
    embed.set_thumbnail(url='https://media.giphy.com/media/Z4IXspU3iCHlK/giphy.gif')

    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def play(ctx, option, voice_channel: discord.Channel=None):
    server = ctx.message.server
    author = ctx.message.author
    if voice_channel == None:
        voice_channel = author.voice_channel
    if option == "waves":
        if client.is_voice_connected(server):
            await client.say("je suis deja connecté à un channel fait `{}play stop`".format(ctx.prefix))
        else:
            try:
                voice = await client.join_voice_channel(voice_channel)
                Channel = ctx.message.channel
                await client.send_typing(Channel)
                player = voice.create_ffmpeg_player('http://streaming.radionomy.com/DRIVE')
                player.start()
                await client.say(":green_heart: **Vous jouer la radio Waves!**")
            except InvalidArgument:
                await client.say("Vous n'etes pas sur un channel!")

    if option == "joe":
        if client.is_voice_connected(server):
            await client.say("je suis deja connecté à un channel fait `{}play stop`".format(ctx.prefix))
        else:
            try:
                voice = await client.join_voice_channel(voice_channel)
                Channel = ctx.message.channel
                await client.send_typing(Channel)
                player = voice.create_ffmpeg_player('http://icecast-qmusic.cdp.triple-it.nl/JOEfm_be_live_64.aac')
                player.start()
                await client.say(":green_heart: **Vous jouer la radio Joe!**")
            except InvalidArgument:
                await client.say("Vous n'etes pas sur un channel!")

    if option != "joe" and option != "waves" and option != "stop":
        if client.is_voice_connected(server):
            await client.say("je suis deja connecté à un channel fait `{}play stop`".format(ctx.prefix))
        else:
            try:
                voice = await client.join_voice_channel(voice_channel)
                Channel = ctx.message.channel
                await client.send_typing(Channel)
                player = voice.create_ffmpeg_player(option)
                player.start()
                await client.say(":green_heart: **Vous jouer la radio Custom!**")
            except InvalidArgument:
                await client.say("Vous n'etes pas sur un channel!")
            except:
                await client.say("Une érreur est apparue sur le link!")

    if option == "stop":
        for x in client.voice_clients:
            if (x.server == ctx.message.server):
                return await x.disconnect()

@client.command(pass_context=True)
async def playt(ctx, url,  voice_channel: discord.Channel=None):
    server = ctx.message.server
    author = ctx.message.author

    if voice_channel == None:
        voice_channel = author.voice_channel

    if url != "stop":
        if client.is_voice_connected(server):
            await client.say("je suis deja connecté à un channel fait `{}playt stop`".format(ctx.prefix))
        else:
            try:
                voice = await client.join_voice_channel(voice_channel)
                Channel = ctx.message.channel
                await client.send_typing(Channel)
                player = await voice.create_ytdl_player(url)
                time.sleep(1)
                player.start()
                await client.say(":green_heart: **Vous jouer une music YT**")

            except InvalidArgument:
                await client.say("Vous n'etes pas sur un channel!")
            except:
                await client.say("Une érreur est apparue sur le link!")

    if url == "stop":
        for x in client.voice_clients:
            if (x.server == ctx.message.server):
                return await x.disconnect()



client.run(TOKEN)
