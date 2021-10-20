import discord
import random

# define stuff needed for commands
coffee_images = ["https://www.clipartkey.com/mpngs/m/101-1015553_coffee-cute-tumblr-coffee-sticker.png",
                 "https://www.kindpng.com/picc/m/280-2806365_transparent-cute-coffee-cup-clipart-donuts-and-coffee.png",
                 "https://png.pngtree.com/png-clipart/20190912/ourlarge/pngtree-hand-drawn-iced-coffee-png-image_1728464.jpg",
                 "https://i.pinimg.com/564x/f8/e0/8d/f8e08db7cc89fcc898999eb5a8612ace.jpg",
                 "https://www.pinclipart.com/picdir/big/558-5588571_strawberry-sticker-pink-starbucks-drink-starbucks-new-logo.png",
                 "https://i.pinimg.com/originals/d9/8c/4c/d98c4c8ff9d3e6e259a467677f32f92c.jpg",
                 "https://www.clipartmax.com/png/middle/11-116158_starbucks-clipart-cute-cartoon-green-tea-clip-art.png",
                 "https://previews.123rf.com/images/djvstock/djvstock1809/djvstock180903018/110346978-kawaii-coffee-cup-and-coffee-over-white-background-vector-illustration.jpg",
                 "https://www.meme-arsenal.com/memes/8ed0850a0390e4c9fb9c949b7b5afc6c.jpg",
                 "https://cdn.shopify.com/s/files/1/0300/9124/7748/products/mockup-32199a74_1200x1200.jpg?v=1581907571",
                 "https://i.pinimg.com/736x/a3/17/08/a317085b479e7cdff35a3c69f0d57b02.jpg"
                 "https://img.icons8.com/plasticine/2x/kawaii-coffee.png"]
affirmations = ["you're amazing,and you deserve a treat. have a coffee!",
                "i love you! hold on, yeah?",
                "thanks for being my friend, i love you",
                "you're really strong, keep going! things will get better",
                "you're not alone, you can always talk to your loved ones :)",
                "go drink a glass of resfreshingly cool, crisp water! have a nice day!",
                "go eat something! don't forget to have a meal today, you should stay healthy :D!",
                "coffee isn't a meal, please get something to eat. everyone deserves to stay healthy",
                "tomorrow will be better than today, and every day we get closer to happiness :) hold out for the future!",
                "you're perfect the way you are, don't ever change :)"]

ball_responses = ["certainly!", "ofc dude", "you may rely on it",
"yes defo", "decidedly so", "imo, yes", "most likely", "yupp",
"outlook good", "signs point to yes", "reply hazy try later lol",
"trust me you dont wanna know rn", "sorry im napping ask later", "cant predict rn",
"how would i know im just a bot", "dont count on it", "outlook NOT so good",
"a little birdie told me no", "doubtful", "lol no", "dude just go to therapy", "TAKE A NAP JESUS",
"piss off", "go touch some grass", "how about no", "i rlly don't want to tell you"]

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='Fall Out Boy'))


@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    # if called by a member
    if message.content.startswith(">"):
        # hello
        if message.content.lower().startswith(">hello"):
            hellousr = str(message.author)
            hellousr = hellousr.split('#')
            hellousr = hellousr[0]
            await message.channel.send(
                "Hello, " + hellousr + "! I am your friendly neighbourhood bot awaiting your command :)")
        # test command - image
        if message.content.lower().startswith(">coffee"):
            coffee_int = random.randint(0, len(coffee_images) - 1)
            await message.channel.send(coffee_images[coffee_int])
            await message.channel.send("Enjoy your coffee, and have a nice day!")
        if message.content.lower().startswith(">pronouns"):
            await message.channel.send("My pronouns are they/them. Thank you for asking! What are yours? :)")
            # add code for asking original author for pronouns, and responding to it
        if message.content.lower().startswith(">affirm"):
            affirmusr = str(message.author)
            affirmusr = affirmusr.split('#')
            affirmusr = affirmusr[0]
            affirm_int = random.randint(0, len(affirmations) - 1)
            await message.channel.send(affirmusr + ", " + affirmations[affirm_int])
        if message.content.lower().startswith(">send affirm"):
            msg = str(message.content.lower()).split(' ')
            usr = msg[-1]
            affirm_int = random.randint(0, len(affirmations) - 1)
            await message.channel.send(usr + ", " + affirmations[affirm_int])
            # looks like >send affirm @user
        #add 8ball command
        if message.content.lower().startswith(">8ball"):
            ball_int = random.randint(0, len(ball_responses) - 1)
            await message.channel.send(ball_responses[ball_int])
        if message.content.lower().startswith(">music"):
            await message.channel.send("https://www.youtube.com/watch?v=A67ZkAd1wmI")
        if message.content.lower().startswith(">repeat"):
            msgstring = message.content[7:]
            i = 20
            while i >= 0:
                await message.channel.send(msgstring)
                i -= 1
        # help
        if message.content.lower().startswith(">help"):
            await message.channel.send('''
`Hello! I am BeepBoop, or BB. Here is my list of commands.
>help - For bot help
>hello - I will respond with a greeting, addressed to you!
>coffee - I will send you a coffee, but not the drinkable kind, for i am a discord bot.
>pronouns - Ask me for my pronouns!
>affirm - Because everyone needs love, even you.
>send affirm @user - Because sometimes we don't know how to communicate our appreciation for our loved ones
>music - I will send you a music suggestion!
>8ball - Do not take this command seriously! It's just for fun
more commands in progress!`
''')
    if 'beepboop' in message.content.lower():
        await message.channel.send(message.author.mention + " Call me BB! :)")
    if 'gay' in message.content.lower():
        emoji = '🌈'
        await message.add_reaction(emoji)
    if 'bb' in message.content.lower():
        emoji = '🍑'
        await message.add_reaction(emoji)
    if '<3' in message.content.lower():
        emoji = '♥'
        await message.add_reaction(emoji)

    #new
    if 'no u' in message.content.lower():
        await message.channel.send('no u')
    if ':(' in message.content.lower():
        await message.channel.send('pat pat')
    

client.run('Nzg5NDgwMTQ4MTE4MTQzMDA3.X9yqrw.d7PaQs-hIwHsKX72q-85j6RP-Vc')
