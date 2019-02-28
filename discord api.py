import discord
import re

TOKEN = 'NTIxODQxODI4OTk2MzE3MTg0.DvCS8Q.zXwIvwsKP-vWl-M5K5SoF_KGh5k'

client = discord.Client()

def vulgar(msg):
    replace_with = '!@#$%^&*()\':;.,><UwU--_--=+`~\|][}{[/?'

    bad = False

    banned = """anal,anus,arse,ass,ballsack,balls,bastard,
    bitch,biatch,bloody,blowjob,blow job,bollock,bollok,
    boner,boob,bugger,bum,butt,buttplug,clitoris,cock,
    coon,crap,cunt,damn,dick,dildo,dyke,fag,faggot,faggy,feck,fellate,
    fellatio,felching,fuck,f u c k,fudgepacker,fudge packer,
    flange,Goddamn,God damn,hell,homo,jerk,jizz,knobend,knob end,
    labia,lmao,lmfao,muff,nigger,nigga,penis,piss,poop,prick,
    pube,pussy,queer,scrotum,sex,shit,s hit,sh1t,slut,smegma,spunk,
    tit,tosser,turd,twat,vagina,wank,whore"""
    banned = banned.split(',')
    clean_msg = None 
    temp_msg = msg.split(" ")

    for i in banned:
        if i in msg:
            pattern = r"\b" + re.escape(i) + r"\b"
            clean_msg = re.sub(pattern, replace_with[:len(i)-1],msg)
            bad = True



    if bad:
        return clean_msg

    return bad



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    cleaned_msg = vulgar(message.content.lower())
    if cleaned_msg:
        await client.delete_message(message)
        cleaned_msg = 'Watch your mouth! {0.author.mention}:\n <{1}>'.format(message,cleaned_msg)
        await client.send_message(message.channel, cleaned_msg)
    else:
        await client.send_message(message.channel, "No")
        



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)