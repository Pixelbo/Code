




if message.content.startswith('!MDR'):

    await client.send_message(message.channel, 'Dit un nombre avec !num')

    def check(msg):
        return msg.content.startswith('!num')

    message = await client.wait_for_message(author=message.author, check=check)
    name = message.content[len('$name'):].strip()
    await client.send_message(message.channel, name)

    try:
        if int(name) > 20:
            raise NameError('alerte')

        num = int(name)
        await client.send_message(message.channel, 'MDR ' * num, tts=True)
        for i in range(num):
            await client.send_message(message.channel, '@everyone MDR')

    except NameError:
        await client.send_message(message.channel, 'MDR fais pas chier le monde')

    except:
        await client.send_message(message.channel, 'MDR ce n est pas un nombre')


if message.content.startswith('!help'):
    await client.send_message(message.channel, 'commandes:')
    await client.send_message(message.channel, '```!bonjour | qui permet de dire bonjour\n!membre | qui liste tout les membres du serv\n!channels | qui liste tout les channels du serv\n!react | pour avoir UNE réaction\n!MDR | JAJ\n!JAJ | MDR```')


if message.content.startswith('!JAJ'):
    await client.send_message(message.channel, 'Dit un nombre avec !num')
    def check1(msg):
        return msg.content.startswith('!num')

    message = await client.wait_for_message(author=message.author, check=check1)
    name = message.content[len('$name'):].strip()
    await client.send_message(message.channel, name)

    try:
        if int(name) > 20:
            raise NameError('alerte')
        num = int(name)

        await client.send_message(message.channel, 'JAJ '*num)
        await client.send_message(message.channel, 'JAJ '*num, tts=True)

    except NameError:
        await client.send_message(message.channel, 'JAJ fais pas chier le monde')

    except:
        await client.send_message(message.channel, 'JAJ ce n est pas un nombre')


if message.content.startswith('!music'):
    channel = client.get_channel('497061154363801610')

    if client.startswith('https://www.youtube.com/watch?v='):
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player(youtube_url)
        player.start()
    else:
        return 'URL_ERROR'